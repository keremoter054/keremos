from pydantic import BaseModel
from pydantic import Field

from typing import Optional

# =====================================
# FLASHCARD MODEL
# =====================================


class FlashcardModel(BaseModel):

    id: int

    video_id: int

    content: str

    tags: str = "[]"

    source_note_id: Optional[int] = None

    status: str = "pending"

    review_count: int = 0

    created_at: Optional[str] = None

    class Config:

        from_attributes = True


# =====================================
# FLASHCARD REVIEW MODEL
# =====================================


class FlashcardReviewModel(BaseModel):

    flashcard_id: int

    status: str = Field(
        ...,
        pattern="^(pending|accepted|rejected)$",
    )


# =====================================
# FLASHCARD GENERATE MODEL
# =====================================


class FlashcardGenerateModel(BaseModel):

    video_id: int


# =====================================
# FLASHCARD RESPONSE MODEL
# =====================================


class FlashcardResponseModel(BaseModel):

    status: str = "ok"

    inserted: int = 0

    skipped: int = 0

    error: Optional[str] = None


# =====================================
# FLASHCARD SEND MODEL
# =====================================


class FlashcardSendModel(BaseModel):

    sent: int = 0

    failed: int = 0


# =====================================
# FLASHCARD DELETE MODEL
# =====================================


class FlashcardDeleteModel(BaseModel):

    deleted: int = 0


# =====================================
# FLASHCARD STATS MODEL
# =====================================


class FlashcardStatsModel(BaseModel):

    total_flashcards: int = 0

    accepted_flashcards: int = 0

    rejected_flashcards: int = 0

    pending_flashcards: int = 0

    total_reviews: int = 0


# =====================================
# FLASHCARD FILTER MODEL
# =====================================


class FlashcardFilterModel(BaseModel):

    status: Optional[str] = None

    video_id: Optional[int] = None

    tag: Optional[str] = None


# =====================================
# ANKI DECK MODEL
# =====================================


class AnkiDeckModel(BaseModel):

    deck_name: str

    card_count: int = 0


# =====================================
# ANKI SEND RESPONSE
# =====================================


class AnkiSendResponseModel(BaseModel):

    status: str = "ok"

    deck_name: Optional[str] = None

    sent: int = 0

    failed: int = 0

    error: Optional[str] = None


# =====================================
# FLASHCARD ANALYTICS MODEL
# =====================================


class FlashcardAnalyticsModel(BaseModel):

    average_reviews: float = 0

    mastery_percent: float = 0

    total_cards: int = 0

    completed_cards: int = 0
