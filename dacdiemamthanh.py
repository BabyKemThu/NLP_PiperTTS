import os
import wave
import contextlib

def inspect_audio(file_path):
    try:
        with contextlib.closing(wave.open(file_path, 'rb')) as wf:
            n_channels = wf.getnchannels()
            sample_width = wf.getsampwidth()
            framerate = wf.getframerate()
            n_frames = wf.getnframes()
            duration = n_frames / float(framerate)

        file_size = os.path.getsize(file_path)

        print(f"📁 File: {file_path}")
        print(f"🎧 Channels: {n_channels}")
        print(f"🎶 Sample rate: {framerate} Hz")
        print(f"🔢 Bit depth: {sample_width * 8}-bit")
        print(f"⏱️ Duration: {duration:.2f} sec")
        print(f"📦 File size: {file_size / 1024:.2f} KB")
        print("-" * 40)

    except wave.Error:
        print(f"⚠️ Không thể mở file WAV: {file_path}")
    except Exception as e:
        print(f"❌ Lỗi: {e}")

# Ví dụ sử dụng
inspect_audio("dataset_vi/wavs/00000.wav")
