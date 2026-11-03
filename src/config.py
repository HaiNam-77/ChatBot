import os
from pathlib import Path
import torch
from dotenv import load_dotenv

load_dotenv()

# config.py nằm ở D:\ChatBot\src\config.py  ->  parents[1] là D:\ChatBot
PROJECT_ROOT = Path(__file__).resolve().parents[1]

DOCUMENT_NAME = "Giao_trinh_Ly_thuyet_thong_tin.pdf"
DATA_DIR = str(PROJECT_ROOT / "data" / "md")                   # SỬA cho đúng nơi chứa trang_*.md
INDEX_DIR = str(PROJECT_ROOT / "storage" / "faiss_index")
SIGNATURE_FILE = os.path.join(INDEX_DIR, "index_signature.json")

# Cấu hình Model
EMBEDDING_MODEL_NAME = "BAAI/bge-m3"
RERANKER_MODEL_NAME = "BAAI/bge-reranker-v2-m3"
LLM_MODEL_NAME = "gemini-3-flash-preview"

# Thiết bị thực thi (Tự động chọn CUDA nếu có, ngược lại dùng CPU)
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

# Tham số Chunking & Retrieval
CHUNK_SIZE = 1000
CHUNK_OVERLAP = 150
RETRIEVER_K = 10
RERANKER_TOP_N = 3
METHOD_SIGNATURE = "page_markers_v3"        # đổi từ section_markers_v2 để index được dựng lại