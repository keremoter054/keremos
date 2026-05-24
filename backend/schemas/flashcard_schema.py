from pydantic import BaseModel
from pydantic import Field

from typing import Optional


class FlashcardSchema(BaseModel):

    id: int

    video_id: int

    content: str

    tags: str = "[]"

    source_note_id: Optional[int] = None

    status: str = "pending"

    review_count: int = 0

    created_at: Optional[str] = None


class FlashcardReviewSchema(BaseModel):

    flashcard_id: int

    status: str = Field(
        ...,
        pattern="^(pending|accepted|rejected)$",
    )


class FlashcardGenerateSchema(BaseModel):

    video_id: int


class FlashcardResponseSchema(BaseModel):

    status: str = "ok"

    inserted: int = 0

    skipped: int = 0

    error: Optional[str] = None


class FlashcardSendSchema(BaseModel):

    sent: int = 0

    failed: int = 0


class FlashcardDeleteSchema(BaseModel):

    deleted: int = 0


class FlashcardStatsSchema(BaseModel):

    total_flashcards: int = 0

    accepted_flashcards: int = 0

    rejected_flashcards: int = 0

    pending_flashcards: int = 0

    total_reviews: int = 0


class FlashcardFilterSchema(BaseModel):

    status: Optional[str] = None

    video_id: Optional[int] = None

    tag: Optional[str] = None


class AnkiDeckSchema(BaseModel):

    deck_name: str

    card_count: int = 0


class AnkiSendResponseSchema(BaseModel):

    status: str = "ok"

    deck_name: Optional[str] = None

    sent: int = 0

    failed: int = 0

    error: Optional[str] = None


class FlashcardAnalyticsSchema(BaseModel):

    average_reviews: float = 0

    mastery_percent: float = 0

    total_cards: int = 0

    completed_cards: int = 0
