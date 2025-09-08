from flask import Flask, request, send_file, jsonify, render_template
import os
import subprocess
import uuid
import json

app = Flask(__name__, static_folder='static', static_url_path='/static')

# Thư mục chứa audio
OUTPUT_DIR = "./static/audio/"
if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

# Đường dẫn file books.json (em đã có sẵn)
BOOKS_FILE = "./data/books.json"
if not os.path.exists("./data"):
    os.makedirs("./data")

# Load dữ liệu sách từ file JSON
with open(BOOKS_FILE, 'r', encoding='utf-8') as f:
    books = json.load(f)


def generate_audio(text):
    """Tạo file audio tiếng Việt từ text bằng Piper."""
    output_filename = f"{uuid.uuid4().hex}.wav"
    output_path = os.path.join(OUTPUT_DIR, output_filename)

    input_text_path = "temp_input.txt"
    with open(input_text_path, "w", encoding="utf-8") as f:
        f.write(text)

    # Model Piper tiếng Việt (ưu tiên file trong models/, fallback ckpt)
    model_path = "./models/vi_model.onnx"
    config_path = "./models/vi_model.onnx.json"
    if not os.path.exists(model_path):
        model_path = "./epoch_epoch4790.onnx"
        config_path = "./epoch_epoch4790.onnx.json"

    command = f'piper -m "{model_path}" -c "{config_path}" -i {input_text_path} -f "{output_path}"'
    print("RUNNING COMMAND:", command)

    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    print("STDOUT:", result.stdout)
    print("STDERR:", result.stderr)

    if result.returncode == 0:
        return output_filename
    else:
        raise Exception("Failed to generate audio")


@app.route('/', methods=['GET'])
def index():
    """Trang chủ: danh sách sách."""
    return render_template('index.html', books=books)


@app.route('/book/<int:book_id>', methods=['GET'])
def book_detail(book_id):
    """Hiển thị trang chi tiết sách."""
    book = next((b for b in books if b['id'] == book_id), None)
    if not book:
        return jsonify({'error': 'Sách không tồn tại'}), 404
    return render_template('book.html', book=book)


@app.route('/generate_audio/<int:book_id>/<int:page_idx>', methods=['GET'])
def generate_page_audio(book_id, page_idx):
    """Sinh audio cho một trang nếu chưa có."""
    try:
        book = next((b for b in books if b['id'] == book_id), None)
        if not book or page_idx >= len(book['pages']):
            return jsonify({'error': 'Sách hoặc trang không tồn tại'}), 404

        page = book['pages'][page_idx]
        if page['audio']:  # Nếu đã có audio rồi thì trả về luôn
            return jsonify({'audio_url': f"/static/audio/{page['audio']}"})

        text = page['text']
        audio_file = generate_audio(text)
        page['audio'] = audio_file

        # Cập nhật lại books.json
        with open(BOOKS_FILE, 'w', encoding='utf-8') as f:
            json.dump(books, f, indent=2, ensure_ascii=False)

        return jsonify({'audio_url': f"/static/audio/{audio_file}"})
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/download/<path:filename>')
def download_file(filename):
    """Tải file audio."""
    return send_file(os.path.join(OUTPUT_DIR, filename), as_attachment=True)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
