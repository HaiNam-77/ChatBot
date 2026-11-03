import os
from dotenv import load_dotenv
from google import genai

# Nạp các biến môi trường từ file .env
load_dotenv()

api_key = os.getenv("GOOGle_API_KEY")
if not api_key:
    raise ValueError("Chưa tìm thấy GEMINI_API_KEY trong file .env!")

client = genai.Client(api_key=api_key)

print("Danh sách các model khả dụng cho API key của bạn:")
for m in client.models.list():
    # Lọc lấy các model hỗ trợ generateContent
    actions = getattr(m, "supported_actions", []) or getattr(m, "supported_generation_methods", [])
    if "generateContent" in actions:
        # Bỏ tiền tố 'models/' nếu có để lấy đúng tên truyền vào config
        model_name = m.name.replace("models/", "")
        print(f"- {model_name}")