from pydantic import BaseModel
from pydantic import Field
from typing import Optional


class PlaylistImportSchema(BaseModel):

    playlist_url: str = Field(
        ...,
        min_length=5,
    )

    category: str = Field(
        ...,
        min_length=1,
    )


class PlaylistReorderSchema(BaseModel):

    order: list[int]


class PlaylistResponseSchema(BaseModel):

    status: str = "ok"

    playlist_title: Optional[str] = None

    inserted_videos: int = 0

    error: Optional[str] = None


class PlaylistVideoSchema(BaseModel):

    id: int

    playlist_id: int

    youtube_video_id: str

    title: str

    duration_seconds: int = 0


class CategorySchema(BaseModel):

    id: int

    name: str


class PlaylistStatsSchema(BaseModel):

    total_videos: int = 0

    total_seconds: int = 0

    total_hours: float = 0


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
