"""FastAPI backend cho chatbot. Chạy từ thư mục gốc dự án:
    uvicorn src.api.app:app --port 8000
"""
import json
import threading
from collections import OrderedDict
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_openai import ChatOpenAI
from src import config
from src.schemas.schemas import ChatRequest
from src.core.ingestion import load_or_build_vectorstore
from src.core.retrieval import build_retriever_pipeline
from src.services.rag_service import RAGService

MAX_HISTORY = 3          # số lượt hội thoại gửi vào bước viết lại câu hỏi
MAX_SESSIONS = 200       # demo: giữ lịch sử trong RAM, bỏ phiên cũ nhất khi vượt mức
SHORT_ANSWER_CHARS = 300


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("[API] Đang nạp mô hình, vui lòng đợi...")
    embeddings = HuggingFaceEmbeddings(
        model_name=config.EMBEDDING_MODEL_NAME,
        model_kwargs={"device": config.DEVICE},
        encode_kwargs={"normalize_embeddings": True},
    )
    # llm = ChatGoogleGenerativeAI(model=config.LLM_MODEL_NAME, temperature=0.0)

    llm = ChatOpenAI(
        base_url=config.ROUTER_BASE_URL,
        api_key=config.ROUTER_API_KEY,
        model=config.JUDGE_MODEL_NAME,
        temperature=0.0
    )
    retriever = build_retriever_pipeline(load_or_build_vectorstore(embeddings))

    app.state.rag = RAGService(llm=llm, retriever=retriever)
    app.state.sessions = OrderedDict()
    app.state.lock = threading.Lock()
    print("[API] Sẵn sàng.")
    yield


app = FastAPI(title="Chatbot Lý thuyết thông tin", lifespan=lifespan)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_methods=["*"],
    allow_headers=["*"],
)


def _event(type_: str, **data) -> str:
    return json.dumps({"type": type_, **data}, ensure_ascii=False) + "\n"


def _get_history(session_id: str) -> list:
    with app.state.lock:
        return list(app.state.sessions.get(session_id, []))


def _save_turn(session_id: str, question: str, answer: str) -> None:
    short = answer[:SHORT_ANSWER_CHARS] + "..." if len(answer) > SHORT_ANSWER_CHARS else answer
    with app.state.lock:
        sessions = app.state.sessions
        history = sessions.setdefault(session_id, [])
        history.append((question, short))
        del history[:-MAX_HISTORY]
        sessions.move_to_end(session_id)
        while len(sessions) > MAX_SESSIONS:
            sessions.popitem(last=False)


@app.get("/api/health")
def health():
    return {"status": "ok"}


# Dùng `def` (không phải `async def`): generator đồng bộ bên dưới được Starlette chạy
# trong threadpool, nên không chặn event loop.
@app.post("/api/chat")
def chat(req: ChatRequest):
    rag = app.state.rag
    history = _get_history(req.session_id)

    def event_stream():
        try:
            standalone = rag.rewrite_question(req.message, history) or req.message
            yield _event("rewrite", text=standalone)

            full = ""
            for piece in rag.stream_answer(standalone):
                full += piece
                yield _event("token", text=piece)

            _save_turn(req.session_id, standalone, full)
            yield _event("done")
        except Exception as e:
            yield _event("error", message=f"{type(e).__name__}: {e}")

    return StreamingResponse(
        event_stream(),
        media_type="application/x-ndjson",
        headers={"Cache-Control": "no-cache", "X-Accel-Buffering": "no"},
    )


@app.delete("/api/sessions/{session_id}")
def reset_session(session_id: str):
    with app.state.lock:
        app.state.sessions.pop(session_id, None)
    return {"status": "cleared"}

