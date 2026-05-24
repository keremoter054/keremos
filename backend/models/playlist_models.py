from pydantic import BaseModel
from pydantic import Field

from typing import Optional

# =====================================
# PLAYLIST MODEL
# =====================================


class PlaylistModel(BaseModel):

    id: int

    youtube_playlist_id: str

    title: str

    category_id: Optional[int] = None

    order_index: int = 0

    channel_name: Optional[str] = None

    thumbnail_url: Optional[str] = None

    video_count: int = 0

    toplam_saat: float = 0

    izlenen_saat: float = 0

    yuzde: float = 0

    kalan_gun: Optional[int] = None

    bitis_tarihi: Optional[str] = None

    # =====================================
    # ORM MODE
    # =====================================

    class Config:

        from_attributes = True


# =====================================
# PLAYLIST IMPORT MODEL
# =====================================


class PlaylistImportModel(BaseModel):

    playlist_url: str = Field(
        ...,
        min_length=5,
    )

    category: str = Field(
        ...,
        min_length=1,
    )


# =====================================
# PLAYLIST REORDER MODEL
# =====================================


class PlaylistReorderModel(BaseModel):

    order: list[int]


# =====================================
# CATEGORY MODEL
# =====================================


class CategoryModel(BaseModel):

    id: int

    name: str

    class Config:

        from_attributes = True


# =====================================
# PLAYLIST STATS MODEL
# =====================================


class PlaylistStatsModel(BaseModel):

    total_videos: int = 0

    total_seconds: int = 0

    total_hours: float = 0


# =====================================
# PLAYLIST RESPONSE MODEL
# =====================================


class PlaylistResponseModel(BaseModel):

    status: str = "ok"

    playlists: list[PlaylistModel] = []


# =====================================
# PLAYLIST IMPORT RESPONSE
# =====================================


class PlaylistImportResponseModel(BaseModel):

    status: str

    playlist_title: Optional[str]

    inserted_videos: int = 0

    stats: Optional[PlaylistStatsModel] = None

    error: Optional[str] = None
