from fastapi import FastAPI
import uuid
from datetime import datetime

# 1. Khởi tạo "Nhà hàng" AI
app = FastAPI()

@app.get("/")
def home():
    return {"message": "Chào mừng Data Scientist đến với AI API!"}

# 2. Tạo một Endpoint (Cổng) để xử lý văn bản
@app.get("/analyze")
def analyze(text: str):
    words = text.split()
    return {
        "id": str(uuid.uuid4()),
        "input_text": text,
        "word_count": len(words),
        "processed_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }