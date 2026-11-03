from langchain_huggingface import HuggingFaceEmbeddings
from langchain_google_genai import ChatGoogleGenerativeAI

from src import config
from src.core.ingestion import load_or_build_vectorstore
from src.core.retrieval import build_retriever_pipeline
from src.services.rag_service import RAGService


def main():
    print("[Khởi động] Đang thiết lập môi trường và mô hình...")

    embeddings = HuggingFaceEmbeddings(
        model_name=config.EMBEDDING_MODEL_NAME,
        model_kwargs={'device': 'cpu'},
        encode_kwargs={'normalize_embeddings': True}
    )

    llm = ChatGoogleGenerativeAI(
        model=config.LLM_MODEL_NAME,
        temperature=0.0
    )

    # 1. Nạp/Build Data (Ingestion)
    vectorstore = load_or_build_vectorstore(embeddings)

    # 2. Xây dựng Pipeline Retrieval (Hybrid + Reranker)
    retriever = build_retriever_pipeline(vectorstore)

    # 3. Khởi tạo Service RAG
    rag_service = RAGService(llm=llm, retriever=retriever)

    # 4. Giao diện Chatbot CLI
    chat_history = []
    print("\nChatbot Lý thuyết thông tin đã sẵn sàng! Gõ 'thoát' để dừng.")

    while True:
        question = input("\nQuestion: ").strip()
        if not question:
            continue
        if question.lower() == "thoát":
            break

        try:
            standalone_question = rag_service.rewrite_question(question, chat_history)
            print(f"-> [Truy vấn tối ưu]: {standalone_question}")

            full_answer = ""
            print("Answer: ", end="")
            for piece in rag_service.stream_answer(standalone_question):
                print(piece, end="", flush=True)
                full_answer += piece
            print()

            short_answer = full_answer[:300] + "..." if len(full_answer) > 300 else full_answer
            chat_history.append((standalone_question, short_answer))

            if len(chat_history) > 3:
                chat_history.pop(0)

        except Exception as e:
            print(f"\n[Cảnh báo] Đã xảy ra lỗi: {e}")
            print("Vui lòng đợi vài giây rồi thử lại.")


if __name__ == "__main__":
    main()