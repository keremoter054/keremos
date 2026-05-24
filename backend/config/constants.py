# =====================================
# APP
# =====================================

APP_NAME = "KeremOS"

APP_VERSION = "1.0.0"

APP_DESCRIPTION = "Civilization Operating System"

# =====================================
# MONTHS
# =====================================

MONTHS_TR = [
    "Ocak",
    "Şubat",
    "Mart",
    "Nisan",
    "Mayıs",
    "Haziran",
    "Temmuz",
    "Ağustos",
    "Eylül",
    "Ekim",
    "Kasım",
    "Aralık",
]

# =====================================
# VIDEO STATUS
# =====================================

VIDEO_STATUS_NOT_STARTED = "not_started"

VIDEO_STATUS_PROCESSING = "processing"

VIDEO_STATUS_DONE = "done"

VIDEO_STATUS_FAILED = "failed"

VIDEO_STATUS_QUEUED = "queued"

# =====================================
# GOAL STATUS
# =====================================

GOAL_STATUS_ACTIVE = "active"

GOAL_STATUS_COMPLETED = "completed"

GOAL_STATUS_ARCHIVED = "archived"

# =====================================
# CHECKLIST TYPES
# =====================================

CHECKLIST_PENDING = "pending"

CHECKLIST_TODAY = "today"

CHECKLIST_DEVELOPMENT = "development"

# =====================================
# DEFAULTS
# =====================================

DEFAULT_DAILY_STUDY_HOURS = 6

DEFAULT_TOTAL_DAYS = 365

DEFAULT_QUEUE_WORKERS = 1

# =====================================
# LIMITS
# =====================================

MAX_FLASHCARDS_PER_VIDEO = 30

MAX_VIDEO_TITLE_LENGTH = 80

MAX_GOAL_TITLE_LENGTH = 255

# =====================================
# FILES
# =====================================

TEMP_AUDIO_EXTENSION = ".webm"

# =====================================
# COLORS
# =====================================

SUCCESS_COLOR = "#22c55e"

ERROR_COLOR = "#ef4444"

WARNING_COLOR = "#facc15"

INFO_COLOR = "#00d4ff"

BACKGROUND_COLOR = "#0f0f0f"

CARD_COLOR = "#181818"

# =====================================
# LOG PREFIXES
# =====================================

LOG_SUCCESS = "✅"

LOG_ERROR = "❌"

LOG_WARNING = "⚠️"

LOG_INFO = "📘"

LOG_WORKER = "🧠"

LOG_QUEUE = "📥"

# =====================================
# REGEX
# =====================================

CLOZE_PATTERN = r"\{\{c1:(.*?)\}\}"

BROKEN_CLOZE_PATTERN = r"(?<!\{)\{c1:(.*?)\}(?!\})"

# =====================================
# API
# =====================================

OPENAI_BASE_URL = "https://api.openai.com/v1/chat/completions"

YOUTUBE_BASE_URL = "https://www.googleapis.com/youtube/v3"

# =====================================
# TIMEOUTS
# =====================================

OPENAI_TIMEOUT = 30

REQUEST_TIMEOUT = 30

SAVE_DEBOUNCE_MS = 1000
