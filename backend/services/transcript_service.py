import os
import traceback
import tempfile

import whisper
import yt_dlp

from youtube_transcript_api import (
    YouTubeTranscriptApi,
)

from youtube_transcript_api._errors import (
    TranscriptsDisabled,
    NoTranscriptFound,
)

from config.settings import (
    WHISPER_MODEL,
)

from utils.debug_utils import (
    debug_print,
    debug_error,
)

# =====================================
# GLOBAL MODEL
# =====================================

_whisper_model = None

# =====================================
# LOAD WHISPER MODEL
# =====================================


def get_whisper_model():

    global _whisper_model

    if _whisper_model is None:

        debug_print("LOADING WHISPER MODEL")

        _whisper_model = whisper.load_model(WHISPER_MODEL)

    return _whisper_model


# =====================================
# GET TRANSCRIPT
# =====================================


def get_transcript(
    youtube_video_id,
):

    # =====================================
    # TRY TRANSCRIPT API
    # =====================================

    transcript = get_youtube_transcript(youtube_video_id)

    if transcript:

        return transcript

    # =====================================
    # FALLBACK TO WHISPER
    # =====================================

    return get_whisper_transcript(youtube_video_id)


# =====================================
# YOUTUBE TRANSCRIPT API
# =====================================


def get_youtube_transcript(
    youtube_video_id,
):

    try:

        transcript = YouTubeTranscriptApi.get_transcript(
            youtube_video_id,
            languages=[
                "tr",
                "en",
            ],
        )

        text = "\n".join(item["text"] for item in transcript)

        debug_print("TRANSCRIPT API SUCCESS")

        return {
            "status": "ok",
            "source": "youtube_transcript_api",
            "text": text,
        }

    except TranscriptsDisabled:

        debug_error(
            "TRANSCRIPTS DISABLED",
            youtube_video_id,
        )

        return None

    except NoTranscriptFound:

        debug_error(
            "NO TRANSCRIPT FOUND",
            youtube_video_id,
        )

        return None

    except Exception as e:

        debug_error(
            "TRANSCRIPT API FAILED",
            e,
        )

        return None


# =====================================
# WHISPER FALLBACK
# =====================================


def get_whisper_transcript(
    youtube_video_id,
):

    try:

        with tempfile.TemporaryDirectory() as temp_dir:

            audio_path = os.path.join(
                temp_dir,
                "audio.%(ext)s",
            )

            # =====================================
            # DOWNLOAD AUDIO
            # =====================================

            url = "https://www.youtube.com/watch?v=" + youtube_video_id

            ydl_opts = {
                "format": "bestaudio/best",
                "outtmpl": audio_path,
                "quiet": True,
                "noplaylist": True,
            }

            with yt_dlp.YoutubeDL(ydl_opts) as ydl:

                ydl.download([url])

            debug_print("AUDIO DOWNLOADED")

            # =====================================
            # FIND AUDIO FILE
            # =====================================

            downloaded_file = None

            for file in os.listdir(temp_dir):

                if file.startswith("audio"):

                    downloaded_file = os.path.join(
                        temp_dir,
                        file,
                    )

                    break

            if not downloaded_file:

                raise Exception("Audio file not found")

            # =====================================
            # LOAD MODEL
            # =====================================

            model = get_whisper_model()

            # =====================================
            # TRANSCRIBE
            # =====================================

            result = model.transcribe(downloaded_file)

            text = result["text"]

            debug_print("WHISPER SUCCESS")

            return {
                "status": "ok",
                "source": "whisper",
                "text": text,
            }

    except Exception as e:

        debug_error(
            "WHISPER ERROR",
            e,
        )

        traceback.print_exc()

        return {
            "status": "error",
            "error": str(e),
        }


# =====================================
# TRANSCRIPT EXISTS
# =====================================


def transcript_exists(
    text,
):

    if not text:

        return False

    cleaned = text.strip()

    return len(cleaned) >= 30


# =====================================
# SMART CHUNK
# =====================================


def smart_chunk(
    text,
    max_chars=12000,
):

    chunks = []

    current = ""

    paragraphs = text.split("\n")

    for paragraph in paragraphs:

        if len(current) + len(paragraph) > max_chars:

            chunks.append(current.strip())

            current = ""

        current += paragraph + "\n"

    if current.strip():

        chunks.append(current.strip())

    return chunks


# =====================================
# MERGE CHUNKS
# =====================================


def merge_chunks(
    chunks,
):

    return "\n\n".join(chunks)


# =====================================
# TRANSCRIPT STATS
# =====================================


def transcript_stats(
    text,
):

    words = text.split()

    return {
        "characters": len(text),
        "words": len(words),
        "estimated_minutes": round(
            len(words) / 150,
            1,
        ),
    }
