import yt_dlp
import whisper
import os
import torch

# 🔥 DEVICE
device = "cuda" if torch.cuda.is_available() else "cpu"
print("🚀 Device:", device)

# 🔥 MODEL (SADECE 1 KERE YÜKLENİR)
print("🧠 Model yükleniyor...")
model = whisper.load_model("small").to(device)


def download_audio(video_id):
    url = f"https://www.youtube.com/watch?v={video_id}"

    ydl_opts = {
        "format": "bestaudio/best",
        "outtmpl": f"{video_id}.%(ext)s",
        "quiet": False,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    for f in os.listdir():
        if f.startswith(video_id):
            return f


def transcribe(audio_file):
    print("🧠 Transcribe başlıyor...")

    result = model.transcribe(
        audio_file,
        fp16=(device == "cuda"),  # 🔥 GPU hızlandırma
        verbose=True,
    )

    return result["text"]


if __name__ == "__main__":
    video_id = "CEr_UiR4Gvk"

    print("🎧 Ses indiriliyor...")
    audio = download_audio(video_id)

    print("📂 Ses dosyası:", audio)

    text = transcribe(audio)

    print("\n--- TRANSCRIPT ---\n")
    print(text[:1000])
