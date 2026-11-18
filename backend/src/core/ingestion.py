import os
import re
import glob
import json
from langchain_qdrant import QdrantVectorStore, RetrievalMode, FastEmbedSparse
from langchain_text_splitters import RecursiveCharacterTextSplitter, MarkdownHeaderTextSplitter

from src import config
from src.utils.text_utils import protect_math_blocks, restore_math_blocks

def load_or_build_vectorstore(embeddings):
    file_paths = sorted(
        glob.glob(os.path.join(config.DATA_DIR, "trang_*.md")),
        key=lambda p: int(os.path.basename(p)[6:9])
    )

    current_signature = {
        "num_files": len(file_paths),
        "total_size": sum(os.path.getsize(p) for p in file_paths),
        "chunk_size": config.CHUNK_SIZE,
        "chunk_overlap": config.CHUNK_OVERLAP,
        "embed_model": config.EMBEDDING_MODEL_NAME,
        "method": config.METHOD_SIGNATURE,
        "storage": "qdrant_cloud_hybrid", # Đánh dấu đã chuyển sang Qdrant để lần đầu tự động rebuild
    }

    # Khởi tạo Sparse Embedding (BM25) của Qdrant để chạy Hybrid Search
    sparse_embeddings = FastEmbedSparse(model_name="Qdrant/bm25")

    need_rebuild = True
    if os.path.exists(config.SIGNATURE_FILE):
        try:
            with open(config.SIGNATURE_FILE, "r", encoding="utf-8") as f:
                saved_sig = json.load(f)
            if isinstance(saved_sig, dict) and all(saved_sig.get(k) == v for k, v in current_signature.items()):
                need_rebuild = False
        except Exception:
            need_rebuild = True

    if not need_rebuild:
        print("[Ingestion] Cấu hình khớp. Đang kết nối tới Collection sẵn có trên Qdrant Cloud...")
        try:
            return QdrantVectorStore.from_existing_collection(
                embedding=embeddings,
                sparse_embedding=sparse_embeddings,
                url=config.QDRANT_URL,
                api_key=config.QDRANT_API_KEY,
                collection_name=config.QDRANT_COLLECTION_NAME,
                retrieval_mode=RetrievalMode.HYBRID,
                timeout=60,
            )
        except Exception as e:
            print(f"[Ingestion] Không tìm thấy Collection trên Qdrant Cloud ({e}). Tiến hành build lại...")
            need_rebuild = True

    print("[Ingestion] Phát hiện thay đổi dữ liệu hoặc chưa có index. Bắt đầu đẩy dữ liệu lên Qdrant Cloud...")
    headers_to_split_on = [("#", "Header 1"), ("##", "Header 2"), ("###", "Header 3")]
    markdown_splitter = MarkdownHeaderTextSplitter(
        headers_to_split_on=headers_to_split_on,
        strip_headers=False
    )
    markdown_separators = ["\n#{1,6} ", "```\n", "\n\\*\\*\\*+\\n", "\n---+\\n", "\n___+\\n", "\n\n", "\n", " ", ""]
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=config.CHUNK_SIZE,
        chunk_overlap=config.CHUNK_OVERLAP,
        add_start_index=True,
        strip_whitespace=True,
        is_separator_regex=True,
        separators=markdown_separators,
        keep_separator=True
    )

    full_text_parts = []
    for path in file_paths:
        with open(path, encoding="utf-8") as f:
            content = f.read().strip()
        source_name = os.path.basename(path)
        number_page = int(source_name[6:9])
        page_marker = f"\n\n<!-- PAGE_MARKER:{number_page}:{source_name} -->\n\n"
        full_text_parts.append(page_marker + content)

    raw_full_text = "".join(full_text_parts)
    protected_full_text, math_blocks = protect_math_blocks(raw_full_text)

    md_header_splits = markdown_splitter.split_text(protected_full_text)
    raw_chunks = text_splitter.split_documents(md_header_splits)

    final_chunks = []
    current_page = "N/A"
    current_source = "unknown"
    marker_pattern = re.compile(r'<!-- PAGE_MARKER:(\d+):([^\s>]+) -->')

    for ch in raw_chunks:
        markers_found = marker_pattern.findall(ch.page_content)
        if markers_found:
            last_page, last_src = markers_found[-1]
            current_page = int(last_page)
            current_source = last_src

        cleaned_content = marker_pattern.sub("", ch.page_content).strip()
        restored_content = restore_math_blocks(cleaned_content, math_blocks)

        headers = [ch.metadata.get(h) for h in ["Header 1", "Header 2", "Header 3"] if ch.metadata.get(h)]
        muc_str = " > ".join(headers) if headers else "Chung"

        if muc_str != "Chung" and not restored_content.startswith(f"[{muc_str}]"):
            ch.page_content = f"[{muc_str}]\n{restored_content}"
        else:
            ch.page_content = restored_content

        ch.metadata["chunk_id"] = len(final_chunks)
        ch.metadata["source"] = config.DOCUMENT_NAME
        ch.metadata["page_file"] = current_source
        ch.metadata["pdf_page"] = current_page
        ch.metadata["muc"] = muc_str

        final_chunks.append(ch)

    # Đẩy cả Dense Vector + Sparse Vector (BM25) lên Qdrant Cloud
    vectorstore = QdrantVectorStore.from_documents(
        documents=final_chunks,
        embedding=embeddings,
        sparse_embedding=sparse_embeddings,
        url=config.QDRANT_URL,
        api_key=config.QDRANT_API_KEY,
        collection_name=config.QDRANT_COLLECTION_NAME,
        retrieval_mode=RetrievalMode.HYBRID,
        force_recreate=True,
        batch_size=32,
        timeout=60,
    )

    os.makedirs(os.path.dirname(config.SIGNATURE_FILE), exist_ok=True)
    current_signature["so_chunk"] = len(final_chunks)
    with open(config.SIGNATURE_FILE, "w", encoding="utf-8") as f:
        json.dump(current_signature, f, ensure_ascii=False, indent=2)

    print(f"[Ingestion] Đã index thành công {len(final_chunks)} chunks lên Qdrant Cloud.")
    return vectorstore