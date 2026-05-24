from pydantic import BaseModel
from pydantic import Field

from typing import Optional

# =====================================
# VIDEO MODEL
# =====================================


class VideoModel(BaseModel):

    id: int

    playlist_id: int

    youtube_video_id: str

    title: str

    duration_seconds: int = 0

    created_at: Optional[str] = None

    class Config:

        from_attributes = True


# =====================================
# VIDEO PROGRESS MODEL
# =====================================


class VideoProgressModel(BaseModel):

    video_id: int

    daily_limit: int = 2

    correct_streak: int = 0

    wrong_streak: int = 0

    mastery_score: float = 0

    is_completed: int = 0

    class Config:

        from_attributes = True


# =====================================
# VIDEO ANALYSIS MODEL
# =====================================


class VideoAnalysisModel(BaseModel):

    id: int

    video_id: int

    summary: Optional[str] = None

    transcript: Optional[str] = None

    questions: Optional[str] = None

    status: str = "not_started"

    current_index: int = 0

    total_chunks: int = 0

    class Config:

        from_attributes = True


# =====================================
# VIDEO TRANSCRIPT MODEL
# =====================================


class VideoTranscriptModel(BaseModel):

    video_id: int

    transcript: str

    source: Optional[str] = None


# =====================================
# VIDEO ANALYZE REQUEST
# =====================================


class VideoAnalyzeRequestModel(BaseModel):

    video_id: int


# =====================================
# VIDEO ANALYZE RESPONSE
# =====================================


class VideoAnalyzeResponseModel(BaseModel):

    status: str

    video_id: int

    message: Optional[str] = None

    error: Optional[str] = None


# =====================================
# VIDEO STATUS MODEL
# =====================================


class VideoStatusModel(BaseModel):

    video_id: int

    status: str

    current_index: int = 0

    total_chunks: int = 0

    progress_percent: float = 0


# =====================================
# VIDEO SUMMARY MODEL
# =====================================


class VideoSummaryModel(BaseModel):

    video_id: int

    summary: Optional[str] = None

    transcript: Optional[str] = None


# =====================================
# WATCH LOG MODEL
# =====================================


class WatchLogModel(BaseModel):

    id: int

    youtube_video_id: str

    watched_seconds: int = 0

    watched_date: Optional[str] = None

    created_at: Optional[str] = None

    class Config:

        from_attributes = True


# =====================================
# VIDEO STATS MODEL
# =====================================


class VideoStatsModel(BaseModel):

    total_videos: int = 0

    analyzed_videos: int = 0

    completed_videos: int = 0

    total_hours: float = 0

    watched_hours: float = 0

    progress_percent: float = 0
