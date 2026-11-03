import os
import re
import glob
import json
import unicodedata
from dotenv import load_dotenv

# Phải gọi load_dotenv() trước khi import các thư viện LangChain
load_dotenv()



from langchain_community.retrievers import BM25Retriever
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_text_splitters import RecursiveCharacterTextSplitter, MarkdownHeaderTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.vectorstores.utils import DistanceStrategy
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_core.documents import Document
from langchain_classic.retrievers import EnsembleRetriever
from langchain_classic.retrievers import ContextualCompressionRetriever
from langchain_classic.retrievers.document_compressors import CrossEncoderReranker
from langchain_community.cross_encoders import HuggingFaceCrossEncoder




# =========================================================
# CÁC HÀM TIỆN ÍCH
# =========================================================
DOCUMENT_NAME = "Giao_trinh_Ly_thuyet_thong_tin.pdf"

def bo_dau(text: str) -> str:
    t = unicodedata.normalize("NFD", text.lower().replace("đ", "d"))
    return "".join(c for c in t if unicodedata.category(c) != "Mn")


def protect_math_blocks(text: str):
    math_blocks = []

    def replacer(match):
        math_blocks.append(match.group(0))
        # Luôn luôn có độ dài cố định là 22 ký tự, bất kể index là 0 hay 999
        return f"__MATH_BLOCK_{len(math_blocks) - 1:06d}__"

    protected_text = re.sub(r'\$\$.*?\$\$', replacer, text, flags=re.DOTALL)
    return protected_text, math_blocks


def restore_math_blocks(text: str, math_blocks: list) -> str:
    def replacer(match):
        idx = int(match.group(1))
        if 0 <= idx < len(math_blocks):
            return math_blocks[idx]
        return match.group(0)

    return re.sub(r'__MATH_BLOCK_(\d{6})__', replacer, text)


# =========================================================
# 1. KHỞI TẠO EMBEDDING & LLM
# =========================================================
embeddings = HuggingFaceEmbeddings(
    model_name="BAAI/bge-m3",
    model_kwargs={'device': 'cpu'},
    encode_kwargs={'normalize_embeddings': True}
)

# Khai báo LLM 1 lần duy nhất để dùng chung cho cả Rewrite và QA
llm = ChatGoogleGenerativeAI(
    model="gemini-3-flash-preview",
    temperature=0.0
)

# =========================================================
# 2. XÂY DỰNG HOẶC TẢI KHO DỮ LIỆU FAISS (BATCHING)
# =========================================================
file_paths = sorted(glob.glob("../data/md/trang_*.md"), key=lambda p: int(os.path.basename(p)[6:9]))
INDEX_DIR = "../storage/faiss_index"
SIGNATURE_FILE = os.path.join(INDEX_DIR, "index_signature.json")

current_signature = {
    "num_files": len(file_paths),
    "total_size": sum(os.path.getsize(p) for p in file_paths),
    "chunk_size": 1000,
    "chunk_overlap": 150,
    "embed_model": "BAAI/bge-m3",
    "method": "section_markers_v2",      # đổi tên mỗi khi bạn đổi cách xử lý
}

need_rebuild = True
if os.path.exists(INDEX_DIR) and os.path.exists(SIGNATURE_FILE):
    with open(SIGNATURE_FILE, "r", encoding="utf-8") as f:
        saved_sig = json.load(f)
    if isinstance(saved_sig, dict) and all(saved_sig.get(k) == v for k, v in current_signature.items()):
        need_rebuild = False

if not need_rebuild:
    print("Đang tải kho dữ liệu FAISS từ ổ cứng (Cấu hình khớp)...")
    vectorstore = FAISS.load_local(
        INDEX_DIR, embeddings, allow_dangerous_deserialization=True
    )
else:
    print("Đang xử lý file .md theo từng cụm (Batching) và khởi tạo FAISS...")

    headers_to_split_on = [("#", "Header 1"), ("##", "Header 2"), ("###", "Header 3")]
    markdown_splitter = MarkdownHeaderTextSplitter(
        headers_to_split_on=headers_to_split_on,
        strip_headers=False
    )
    MARKDOWN_SEPARATORS = ["\n#{1,6} ", "```\n", "\n\\*\\*\\*+\\n", "\n---+\\n", "\n___+\\n", "\n\n", "\n", " ", ""]
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=150,
        add_start_index=True,
        strip_whitespace=True,
        is_separator_regex=True,
        separators=MARKDOWN_SEPARATORS,
        keep_separator=True
    )

    final_chunks = []

    # Tạo chuỗi văn bản gộp có chèn marker định danh từng trang
    full_text_parts = []
    for path in file_paths:
        with open(path, encoding="utf-8") as f:
            content = f.read().strip()

        source_name = os.path.basename(path)
        number_page = int(source_name[6:9])

        # Chèn marker rõ ràng ở đầu mỗi trang
        page_marker = f"\n\n<!-- PAGE_MARKER:{number_page}:{source_name} -->\n\n"
        full_text_parts.append(page_marker + content)

    raw_full_text = "".join(full_text_parts)
    protected_full_text, math_blocks = protect_math_blocks(raw_full_text)

    md_header_splits = markdown_splitter.split_text(protected_full_text)
    raw_chunks = text_splitter.split_documents(md_header_splits)

    final_chunks = []
    current_page = "N/A"
    current_source = "unknown"

    # Regex nhận diện marker
    marker_pattern = re.compile(r'<!-- PAGE_MARKER:(\d+):([^\s>]+) -->')

    for ch in raw_chunks:
        # 1. Kiểm tra xem chunk này có chứa marker ranh giới trang hay không
        markers_found = marker_pattern.findall(ch.page_content)
        if markers_found:
            # Nếu có marker mới, cập nhật trang hiện tại (lấy marker xuất hiện cuối cùng trong chunk)
            last_page, last_src = markers_found[-1]
            current_page = int(last_page)
            current_source = last_src

        # 2. Xóa sạch marker khỏi nội dung chunk để văn bản sạch đẹp
        cleaned_content = marker_pattern.sub("", ch.page_content).strip()

        # 3. Khôi phục công thức toán học
        restored_content = restore_math_blocks(cleaned_content, math_blocks)

        # 4. Trích xuất mục lục
        headers = [ch.metadata.get(h) for h in ["Header 1", "Header 2", "Header 3"] if ch.metadata.get(h)]
        muc_str = " > ".join(headers) if headers else "Chung"

        # 5. Tiêm ngữ cảnh mục lục vào đầu văn bản
        if muc_str != "Chung" and not restored_content.startswith(f"[{muc_str}]"):
            ch.page_content = f"[{muc_str}]\n{restored_content}"
        else:
            ch.page_content = restored_content

        # 6. Gán metadata chuẩn xác 100%
        ch.metadata["chunk_id"] = len(final_chunks)
        ch.metadata["source"] = DOCUMENT_NAME
        ch.metadata["page_file"] = current_source
        ch.metadata["pdf_page"] = current_page
        ch.metadata["muc"] = muc_str

        final_chunks.append(ch)

    vectorstore = FAISS.from_documents(
        documents=final_chunks,
        embedding=embeddings,
        distance_strategy=DistanceStrategy.COSINE
    )
    vectorstore.save_local(INDEX_DIR)

    current_signature["so_chunk"] = len(final_chunks)
    with open(SIGNATURE_FILE, "w", encoding="utf-8") as f:
        json.dump(current_signature, f, ensure_ascii=False, indent=2)

# =========================================================
# 3. THIẾT LẬP HYBRID SEARCH
# =========================================================
all_chunks = list(vectorstore.docstore._dict.values())

bm25_retriever = BM25Retriever.from_documents(
    all_chunks,
    preprocess_func=lambda t: bo_dau(t).split()
)
bm25_retriever.k = 10

faiss_retriever = vectorstore.as_retriever(
    search_type="similarity",
    search_kwargs={"k": 10}
)

hybrid_retriever = EnsembleRetriever(
    retrievers=[bm25_retriever, faiss_retriever],
    weights=[0.5, 0.5]
)

reranker_model = HuggingFaceCrossEncoder(
    model_name = "BAAI/bge-reranker-v2-m3",
    model_kwargs = {'device': 'cuda'}
)

compressor = CrossEncoderReranker(
    model = reranker_model,
    top_n = 3
)

final_retriever = ContextualCompressionRetriever(
    base_compressor = compressor,
    base_retriever = hybrid_retriever
)
# =========================================================
# 4. ĐỊNH DẠNG ĐẦU RA VÀ CẤU HÌNH CHUỖI RAG
# =========================================================
def format_docs(docs):
    return "\n\n---\n\n".join(
        f"[{d.metadata.get('source', 'N/A')}:trang {d.metadata.get('pdf_page', 'N/A')} | Mục: {d.metadata.get('muc', 'Chung')}]\n{d.page_content}"
        for d in docs
    )


rewrite_template = """Dựa vào Lịch sử trò chuyện bên dưới, hãy viết lại Câu hỏi mới của người dùng thành một câu hỏi hoàn chỉnh, độc lập và rõ nghĩa nhất.
Nhiệm vụ:
- LUÔN LUÔN thêm đầy đủ dấu tiếng Việt chuẩn xác nếu câu hỏi bị gõ không dấu hoặc viết tắt.

- Thay thế các đại từ (nó, phần này, cái đó...) bằng danh từ/chủ đề cụ thể trong Lịch sử trò chuyện.

- CHỈ trả về đúng 1 câu hỏi đã được viết lại, KHÔNG giải thích thêm.


Lịch sử trò chuyện:
{chat_history}

Câu hỏi mới: {question}
Câu hỏi hoàn chỉnh:"""
rewrite_prompt = ChatPromptTemplate.from_template(rewrite_template)
rewrite_chain = rewrite_prompt | llm | StrOutputParser()

template = (
    "Bạn là trợ lý tra cứu giáo trình Lý thuyết thông tin.\n"
    "QUY TẮC:\n"
    "1) CHỈ dùng thông tin trong ngữ cảnh giáo trình bên dưới, không dùng kiến thức bên ngoài, không tự suy đoán.\n"
    "2) Nếu ngữ cảnh có thông tin liên quan, hãy trả lời chi tiết dựa trên đó và giữ nguyên các ký hiệu công thức toán học LaTeX.\n"
    "3) Chỉ khi ngữ cảnh hoàn toàn không liên quan đến câu hỏi mới trả lời chính xác: "
    "\"Tôi không tìm thấy thông tin này trong giáo trình được cung cấp.\"\n"
    "4) Trích nguồn cuối câu trả lời theo dạng (tên_file:trang X, Mục: ...) dựa vào nhãn ở đầu mỗi đoạn.\n\n"
    "Ngữ cảnh:\n{context}\n\n"
    "Câu hỏi: {question}"
)
prompt = ChatPromptTemplate.from_template(template)

rag_chain = (
        {"context": final_retriever | format_docs, "question": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
)

# =========================================================
# 5. VÒNG LẶP HỎI ĐÁP AN TOÀN
# =========================================================
chat_history = []

print("\nChatbot Lý thuyết thông tin đã sẵn sàng! Gõ 'thoát' để dừng.")
while True:
    question = input("\nQuestion: ").strip()

    if not question:
        continue
    if question.lower() == "thoát":
        break

    try:
        if len(chat_history) > 0:
            formatted_history = "\n".join([f"User: {q}\nAI: {a}" for q, a in chat_history])
        else:
            formatted_history = "(chưa có)"

        standalone_question = rewrite_chain.invoke({
            "chat_history": formatted_history,
            "question": question
        }).strip()

        print(f"-> [Truy vấn tối ưu]: {standalone_question}")

        full_answer = ""
        print("Answer: ", end="")
        for piece in rag_chain.stream(standalone_question):
            print(piece, end="", flush=True)
            full_answer += piece
        print()

        short_answer = full_answer[:300] + "..." if len(full_answer) > 300 else full_answer
        chat_history.append((standalone_question, short_answer))

        if len(chat_history) > 3:
            chat_history.pop(0)

    except Exception as e:
        print(f"\n[Cảnh báo] Đã xảy ra lỗi kết nối API: {e}")
        print("Vui lòng đợi vài giây rồi đặt lại câu hỏi nhé.")