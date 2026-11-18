import os
from pathlib import Path
import torch
from dotenv import load_dotenv

load_dotenv()

os.environ["HF_HUB_OFFLINE"] = "1"
os.environ["TRANSFORMERS_OFFLINE"] = "1"

# config.py nằm ở D:\ChatBot\src\config.py  ->  parents[1] là D:\ChatBot

BACKEND_DIR = Path(__file__).resolve().parents[1]
ROOT_DIR = Path(__file__).resolve().parents[2]

DOCUMENT_NAME = "Giao_trinh_Ly_thuyet_thong_tin.pdf"
DATA_DIR = str(BACKEND_DIR / "data" / "md")                   # SỬA cho đúng nơi chứa trang_*.md
SIGNATURE_FILE = str(BACKEND_DIR / "index_signature.json")

# Cấu hình Model
EMBEDDING_MODEL_NAME = "BAAI/bge-m3"
RERANKER_MODEL_NAME = "BAAI/bge-reranker-v2-m3"
LLM_MODEL_NAME = "gemini-flash-latest"
EVAL_LLM_MODEL_NAME = "gemini-flash-latest"
ROUTER_BASE_URL = os.getenv("ROUTER_BASE_URL", "http://localhost:20128/v1")
ROUTER_API_KEY = os.getenv("ROUTER_API_KEY", "none")
JUDGE_MODEL_NAME = os.getenv("JUDGE_MODEL_NAME", "rag-judge-combo")
# Thiết bị thực thi (Tự động chọn CUDA nếu có, ngược lại dùng CPU)
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

# Tham số Chunking & Retrieval
CHUNK_SIZE = 1000
CHUNK_OVERLAP = 150
RETRIEVER_K = 10
RERANKER_TOP_N = 3
METHOD_SIGNATURE = "page_markers_v3"  # đổi từ section_markers_v2 để index được dựng lại

# Cấu hình Qdrant Cloud
QDRANT_URL = os.getenv("QDRANT_URL")
QDRANT_API_KEY = os.getenv("QDRANT_API_KEY")
QDRANT_COLLECTION_NAME = "info_theory_docs"

# Cấu hình Exa AI Web Search
EXA_API_KEY = os.getenv("EXA_API_KEY")
EXA_URL = os.getenv("EXA_URL", "https://api.exa.ai/search")
EXA_NUM_RESULTS = 3
EXA_MAX_CHARACTERS = 1500
