### **File 2: README_VN.md (Vietnamese translation, synchronized)**
```markdown
# NLP PiperTTS – Mô hình Text-to-Speech (TTS) tiếng Việt

Repository này cung cấp phiên bản đầu tiên của mô hình **Tổng hợp giọng nói tiếng Việt (TTS)**, được phát triển bởi tác giả sử dụng framework **Piper** với kiến trúc **VITS (Variational Inference Text-to-Speech)**. Mô hình được huấn luyện trên dữ liệu âm thanh tiếng Việt chất lượng cao để tạo ra giọng nói tự nhiên, dễ hiểu từ văn bản. File ONNX đảm bảo khả năng tương thích đa nền tảng và dễ dàng tích hợp vào các ứng dụng khác nhau.

## Nội dung của phiên bản này
- `epoch_epoch4790.onnx` – File mô hình ONNX đã huấn luyện (có trên GitHub Releases)
- `epoch_epoch4790.onnx.json` – Metadata của mô hình
- `README.md` – Phiên bản tiếng Anh của README này

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

## Hướng dẫn sử dụng
1. Clone repository:
   ```bash
   git clone https://github.com/BabyKemThu/NLP_PiperTTS.git
   cd NLP_PiperTTS
