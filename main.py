import json
import uuid
from datetime import datetime

def process_text(input_text):
    words = input_text.split()
    # Giả lập xử lý dữ liệu
    result = {
        "id": str(uuid.uuid4()),
        "original_text": input_text,
        "word_count": len(words),
        "uppercase_words": [w for w in words if w.isupper()],
        "processed_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "status": "success"
    }
    return result

if __name__ == "__main__":
    text_to_test = "Data Scientist học AI Engineer rất NHANH"
    output = process_text(text_to_test)
    
    # Xuất kết quả ra màn hình
    print(json.dumps(output, indent=4, ensure_ascii=False))