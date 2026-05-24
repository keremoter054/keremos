import os
from dotenv import load_dotenv

# =====================================
# LOAD ENV
# =====================================

load_dotenv()

# =====================================
# BASE PATHS
# =====================================

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATA_DIR = os.path.join(BASE_DIR, "data")

BACKUP_DIR = os.path.join(BASE_DIR, "backups")

TEMP_DIR = os.path.join(BASE_DIR, "temp")

LOG_DIR = os.path.join(BASE_DIR, "logs")

# =====================================
# CREATE DIRS
# =====================================

os.makedirs(DATA_DIR, exist_ok=True)
os.makedirs(BACKUP_DIR, exist_ok=True)
os.makedirs(TEMP_DIR, exist_ok=True)
os.makedirs(LOG_DIR, exist_ok=True)

# =====================================
# DATABASE
# =====================================

DB_PATH = os.path.join(DATA_DIR, "app.db")

DB_TIMEOUT = 30

# =====================================
# AI SETTINGS
# =====================================

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

AI_MODEL = "gpt-4o-mini"

# =====================================
# YOUTUBE
# =====================================

YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")

# =====================================
# ANKI
# =====================================

ANKI_URL = "http://127.0.0.1:8765"

# =====================================
# DEBUG
# =====================================

DEBUG_MODE = True

# =====================================
# WORKERS
# =====================================

WORKER_COUNT = 1

QUEUE_TIMEOUT = 5

# =====================================
# WHISPER
# =====================================

WHISPER_MODEL = "small"

# =====================================
# DEVICE
# =====================================

try:

    import torch

    DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

except Exception:

    DEVICE = "cpu"

# =====================================
# APP
# =====================================

APP_NAME = "KeremOS"

APP_VERSION = "1.0.0"
