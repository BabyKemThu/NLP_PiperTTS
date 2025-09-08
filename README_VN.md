# NLP PiperTTS

Đây là dự án Text-to-Speech (TTS) tiếng Việt sử dụng kiến trúc **VITS** và framework **Piper TTS**.

## Cấu trúc repo
- `main.py` : file chạy chính.
- `dacdiemamthanh.py` : kiểm tra đặc trưng âm thanh.
- `templates/` : giao diện web demo.
- `static/` : chứa css, js và audio sinh ra.
- `audio/` : dữ liệu âm thanh đầu vào/ra.
- `epoch_epoch4790.onnx.json` : metadata của mô hình.

## Mô hình đã huấn luyện
File `.onnx` quá lớn nên được đưa lên **GitHub Releases**:  
👉 [Tải model tại đây](https://github.com/BabyKemThu/NLP_PiperTTS/releases)

## 🚀 Cách chạy demo
1. Clone repo:
   ```bash
   git clone https://github.com/BabyKemThu/NLP_PiperTTS.git
   cd NLP_PiperTTS
