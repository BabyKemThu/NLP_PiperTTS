# NLP PiperTTS – Mô hình Text-to-Speech (TTS) tiếng Việt

Repository này cung cấp phiên bản đầu tiên của mô hình **Tổng hợp giọng nói tiếng Việt (TTS)**, phát triển bằng framework Piper và kiến trúc **VITS**. Mô hình được huấn luyện trên dữ liệu âm thanh tiếng Việt chất lượng cao, tạo ra giọng nói tự nhiên và dễ hiểu từ văn bản. File `.onnx` đảm bảo khả năng tích hợp đa nền tảng.

## Nội dung của phiên bản này
- `epoch_epoch4790.onnx` – File mô hình ONNX đã huấn luyện (có trên GitHub Releases)
- `epoch_epoch4790.onnx.json` – Metadata của mô hình
- `README.md` – Phiên bản tiếng Anh

## Cấu trúc repo
- `main.py` – File chạy chính để thực hiện suy luận.
- `dacdiemamthanh.py` – Tiện ích phân tích đặc trưng âm thanh.
- `templates/` – Template giao diện web demo.
- `static/` – Chứa CSS, JS và file âm thanh sinh ra.
- `audio/` – Dữ liệu âm thanh đầu vào và đầu ra.
- `epoch_epoch4790.onnx.json` – Metadata mô tả mô hình đã huấn luyện.

## Mô hình đã huấn luyện
File `.onnx` quá lớn nên được đưa lên **GitHub Releases**.  
[Tải model tại đây](https://github.com/BabyKemThu/NLP_PiperTTS/releases)

## Hướng dẫn sử dụng
1. Clone repository:
   ```bash
   git clone https://github.com/BabyKemThu/NLP_PiperTTS.git
   cd NLP_PiperTTS
