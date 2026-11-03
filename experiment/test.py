from google import genai
from google.genai import types
from pydantic import BaseModel


class ThongTinTraCuu(BaseModel):
    ma_sinh_vien: str
    gpa: str
    trang_thai: str
    danh_gia_hoc_luc: str


def tra_cuu_diem_thi(ma_sinh_vien: str) -> str:
    """Hàm dùng để tra cứu điểm tổng kết (GPA) của sinh viên dựa trên mã sinh viên."""


    # Giả lập Database chứa dữ liệu
    db = {
        "B24DCCN418": "3.44/4.0",
        "B24DCCN123": "2.80/4.0",
        "B24DCCN999": "3.95/4.0"
    }

    diem = db.get(ma_sinh_vien.upper())
    if diem:
        return f"Dữ liệu từ Database: Sinh viên {ma_sinh_vien} có điểm GPA là {diem}"
    return "Lỗi: Mã sinh viên không tồn tại trong hệ thống."



client = genai.Client()  # Thay API Key của bạn vào nhé

# Khởi tạo phiên chat tự động quản lý lịch sử
chat = client.chats.create(
    model="gemini-3-flash-preview",
    config=types.GenerateContentConfig(
        tools=[tra_cuu_diem_thi],
        temperature=0.2
    )
)

print("Bot đã sẵn sàng! Hãy thử hỏi điểm của một mã sinh viên (ví dụ: B24DCCN418) hoặc hỏi thời tiết xem sao.")
print("-" * 50)


while True:
    user_input = input("Bạn: ")
    if user_input.lower() == 'thoát':
        break


    response = chat.send_message(user_input)
    print(f"Bot: {response.text}\n")

