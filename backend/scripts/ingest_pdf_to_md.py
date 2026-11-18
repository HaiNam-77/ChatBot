"""Script OCR chuyển đổi các trang sách từ file PDF sang định dạng Markdown.
Chạy trực tiếp từ thư mục backend:
    python scripts/ingest_pdf_to_md.py
"""
import base64
import os
import time
from pathlib import Path
from dotenv import load_dotenv
import pymupdf
from langchain_core.messages import HumanMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI

# Đường dẫn thư mục chuẩn
BACKEND_DIR = Path(__file__).resolve().parents[1]
ROOT_DIR = BACKEND_DIR.parent

# Load biến môi trường (.env ở backend hoặc root)
load_dotenv(BACKEND_DIR / ".env")
load_dotenv(ROOT_DIR / ".env")

PDF_PATH = BACKEND_DIR / "data" / "GT Ly thuyet thong tin 2013.pdf"
OUTPUT_DIR = BACKEND_DIR / "data" / "md"

# Khởi tạo mô hình Gemini 2.0 Flash (miễn phí, tốc độ cao, hỗ trợ LaTeX xuất sắc)
llm = ChatGoogleGenerativeAI(
    model="gemini-flash-latest",
    temperature=0.0,
    max_retries=3,
    timeout=120,
)
chain = llm | StrOutputParser()

PROMPT = (
    "Chép lại trang sách này thành Markdown. "
    "Công thức viết bằng LaTeX, đặt trong $...$ hoặc $$...$$. "
    "Giữ tiêu đề mục. Bảng viết bằng bảng Markdown. "
    "Với sơ đồ, hãy mô tả ngắn trong [Hình: ...]. "
    "Bỏ header, footer, số trang và watermark. Không thêm bình luận."
)

DELAY_BETWEEN_PAGES = 5.0  # Nghỉ 5s giữa các trang (đạt ~11 trang/phút, luôn an toàn dưới mức 15 RPM)
MAX_PAGE_RETRIES = 5       # Thử lại tối đa 5 lần nếu gặp lỗi mạng hoặc 429


def process_page(pdf_doc, page_index: int, total_pages: int, file_out: Path):
    page_num = page_index + 1
    # Chụp ảnh trang PDF ở độ phân giải 150 DPI
    pix = pdf_doc[page_index].get_pixmap(dpi=150)
    img_bytes = pix.tobytes("png")
    img_b64 = base64.b64encode(img_bytes).decode("utf-8")

    message = HumanMessage(
        content=[
            {"type": "text", "text": PROMPT},
            {
                "type": "image_url",
                "image_url": {"url": f"data:image/png;base64,{img_b64}"},
            },
        ]
    )

    for attempt in range(1, MAX_PAGE_RETRIES + 1):
        try:
            markdown_text = chain.invoke([message])
            with open(file_out, "w", encoding="utf-8") as f:
                f.write(markdown_text)
            print(f"   Đã lưu: {file_out.name}")
            return True
        except Exception as e:
            err_msg = str(e)
            if "429" in err_msg or "RESOURCE_EXHAUSTED" in err_msg:
                wait_time = 15 * attempt
                print(f"   [Rate Limit 429] Chạm giới hạn phút, tự động nghỉ {wait_time}s rồi thử lại (lần {attempt}/{MAX_PAGE_RETRIES})...")
                time.sleep(wait_time)
            else:
                print(f"   [Lỗi mạng] {e}, chờ 10s rồi thử lại (lần {attempt}/{MAX_PAGE_RETRIES})...")
                time.sleep(10)

    print(f"   ❌ Không thể xử lý trang {page_num} sau {MAX_PAGE_RETRIES} lần thử.")
    return False


def main():
    if not PDF_PATH.exists():
        print(f"[LỖI] Không tìm thấy file PDF tại: {PDF_PATH}")
        return

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    pdf = pymupdf.open(str(PDF_PATH))
    total_pages = len(pdf)
    print(f"📄 Mở file PDF thành công: {PDF_PATH.name} ({total_pages} trang)")

    # Bắt đầu quét từ trang 10 (index 9) đến hết cuốn sách
    for i in range(9, total_pages):
        page_num = i + 1
        file_out = OUTPUT_DIR / f"trang_{page_num:03d}.md"

        # Bỏ qua nếu trang đã có file và không rỗng
        if file_out.exists() and file_out.stat().st_size > 50:
            continue

        print(f"⏳ Đang OCR trang {page_num}/{total_pages}...")
        success = process_page(pdf, i, total_pages, file_out)

        if success:
            time.sleep(DELAY_BETWEEN_PAGES)

    print("\n🎉 Hoàn tất quá trình chuyển đổi toàn bộ PDF sang Markdown!")


if __name__ == "__main__":
    main()
