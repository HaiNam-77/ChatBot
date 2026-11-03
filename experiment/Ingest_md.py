from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
import os
import pymupdf
import base64
from langchain_core.messages import HumanMessage

load_dotenv()

llm = ChatGoogleGenerativeAI(model = "gemini-3-flash-preview",temperature = 0)
chain = llm | StrOutputParser()

prompt = (
    "Chép lại trang sách này thành Markdown. "
    "Công thức viết bằng LaTeX, đặt trong $...$ hoặc $$...$$. "
    "Giữ tiêu đề mục. Bảng viết bằng bảng Markdown. "
    "Với sơ đồ, hãy mô tả ngắn trong [Hình: ...]. "
    "Bỏ header, footer, số trang và watermark. Không thêm bình luận."
)

os.makedirs("../data/md", exist_ok = True)
pdf = pymupdf.open("../data/GT Ly thuyet thong tin 2013.pdf")

for i in range(9,len(pdf)):
    number_page = i + 1
    file_out = f"../data/md/trang_{number_page:03d}.md"

    if os.path.exists(file_out):
        continue

    picture = pdf[i].get_pixmap(dpi=150).tobytes("png")
    picture_base64 = base64.b64encode(picture).decode()

    message = HumanMessage(content=[
        {"type": "text","text":prompt},
        {"type": "image_url", "image_url": {"url": f'data:image/png;base64,{picture_base64}'}},
    ])

    text = chain.invoke([message])

    with open(file_out,"w",encoding="utf-8") as f:
        f.write(text)

