from pydantic import BaseModel
from pydantic import Field

from typing import Optional

# =====================================
# IMPORT
# =====================================


class PlaylistImportSchema(BaseModel):

    playlist_url: str = Field(
        ...,
        min_length=5,
    )

    category: str = Field(
        ...,
        min_length=1,
    )

    goal: str = Field(
        ...,
        min_length=1,
    )


# =====================================
# REORDER
# =====================================


class PlaylistReorderSchema(BaseModel):

    order: list[int]


# =====================================
# TARGET SYSTEM
# =====================================


class PlaylistTargetSchema(BaseModel):

    playlist_id: int

    target_days: int

    priority_level: int = 1


# =====================================
# PROGRESS SYSTEM
# =====================================


class PlaylistProgressSchema(BaseModel):

    playlist_id: int

    watched_minutes: int


# =====================================
# RESPONSE
# =====================================


class PlaylistResponseSchema(BaseModel):

    status: str = "ok"

    playlist_title: Optional[str] = None

    inserted_videos: int = 0

    error: Optional[str] = None


# =====================================
# VIDEO
# =====================================


class PlaylistVideoSchema(BaseModel):

    id: int

    playlist_id: int

    youtube_video_id: str

    title: str

    duration_seconds: int = 0


# =====================================
# CATEGORY
# =====================================


class CategorySchema(BaseModel):

    id: int

    name: str


# =====================================
# PLAYLIST STATS
# =====================================


class PlaylistStatsSchema(BaseModel):

    total_videos: int = 0

    total_seconds: int = 0

    total_hours: float = 0


# =====================================
# PLAYLIST CARD
# =====================================


class PlaylistCardSchema(BaseModel):

    id: int

    title: str

    thumbnail_url: Optional[str] = None

    channel_name: Optional[str] = None

    video_count: int = 0

    toplam_saat: float = 0

    izlenen_saat: float = 0

    yuzde: float = 0

    kalan_gun: Optional[int] = None

    bitis_tarihi: Optional[str] = None

    category: Optional[str] = None

    goal: Optional[str] = None

    # =====================================
    # TIME ENGINE
    # =====================================

    target_days: int = 0

    daily_target_minutes: int = 0

    estimated_total_minutes: int = 0

    completed_minutes: int = 0

    remaining_minutes: int = 0

    priority_level: int = 1

    speed_required: float = 0

    speed_current: float = 0

    is_delayed: bool = False

    status: str = "active"

    target_finish_date: Optional[str] = None

    last_study_date: Optional[str] = None


# =====================================
# LEARNING ENGINE STATS
# =====================================


class LearningStatsSchema(BaseModel):

    status: str = "ok"

    total_minutes: int = 0

    completed_minutes: int = 0

    remaining_minutes: int = 0

    progress: float = 0

    playlist_count: int = 0

    delayed_count: int = 0
