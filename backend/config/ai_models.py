# =====================================
# OPENAI MODELS
# =====================================

OPENAI_MODELS = {
    "fast": "gpt-4o-mini",
    "smart": "gpt-4.1",
    "reasoning": "o4-mini",
    "vision": "gpt-4o",
    "embedding": "text-embedding-3-small",
}

# =====================================
# WHISPER MODELS
# =====================================

WHISPER_MODELS = {
    "tiny": "tiny",
    "base": "base",
    "small": "small",
    "medium": "medium",
    "large": "large",
}

# =====================================
# DEFAULT AI MODELS
# =====================================

DEFAULT_CHAT_MODEL = OPENAI_MODELS["fast"]

DEFAULT_REASONING_MODEL = OPENAI_MODELS["reasoning"]

DEFAULT_VISION_MODEL = OPENAI_MODELS["vision"]

DEFAULT_EMBEDDING_MODEL = OPENAI_MODELS["embedding"]

DEFAULT_WHISPER_MODEL = WHISPER_MODELS["small"]

# =====================================
# TOKEN LIMITS
# =====================================

MODEL_TOKEN_LIMITS = {
    "gpt-4o-mini": 128000,
    "gpt-4.1": 128000,
    "o4-mini": 200000,
    "gpt-4o": 128000,
}

# =====================================
# TEMPERATURES
# =====================================

AI_TEMPERATURES = {
    "stable": 0.2,
    "balanced": 0.5,
    "creative": 0.9,
}

# =====================================
# AI TASK ROUTING
# =====================================

AI_TASK_MODELS = {
    "flashcards": OPENAI_MODELS["fast"],
    "notes": OPENAI_MODELS["smart"],
    "analysis": OPENAI_MODELS["reasoning"],
    "vision": OPENAI_MODELS["vision"],
    "summary": OPENAI_MODELS["fast"],
    "prediction": OPENAI_MODELS["reasoning"],
}

# =====================================
# AI SYSTEM PROMPTS
# =====================================

FLASHCARD_SYSTEM_PROMPT = """
Sen profesyonel bir eğitim AI sistemisin.

Kaliteli Anki cloze kartları üret.
"""

NOTES_SYSTEM_PROMPT = """
Sen profesyonel ders notu oluşturan
bir AI sistemisin.
"""

SUMMARY_SYSTEM_PROMPT = """
Transcriptleri düzenli şekilde
özetleyen bir AI sistemisin.
"""

# =====================================
# AI RETRY SETTINGS
# =====================================

AI_MAX_RETRIES = 3

AI_RETRY_DELAY = 2

# =====================================
# TRANSCRIPT SETTINGS
# =====================================

TRANSCRIPT_LANGUAGES = [
    "tr",
    "en",
]

# =====================================
# CHUNK SETTINGS
# =====================================

MAX_CHUNK_SIZE = 12000

MIN_CHUNK_SIZE = 4000

# =====================================
# FLASHCARD SETTINGS
# =====================================

MAX_FLASHCARDS_PER_REQUEST = 30

MIN_FLASHCARD_LENGTH = 20

MAX_FLASHCARD_LENGTH = 300
