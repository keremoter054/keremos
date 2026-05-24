from pydantic import BaseModel
from typing import Optional


class VideoAnalyzeSchema(BaseModel):

    video_id: int


class VideoProgressSchema(BaseModel):

    video_id: int

    status: str

    current_index: int = 0

    total_chunks: int = 0

    progress_percent: float = 0


class VideoResultSchema(BaseModel):

    video_id: int

    summary: Optional[str] = None

    transcript: Optional[str] = None

    questions: Optional[str] = None

    status: str = "not_started"


class VideoTranscriptSchema(BaseModel):

    video_id: int

    transcript: str

    source: Optional[str] = None


class VideoCardSchema(BaseModel):

    id: int

    playlist_id: int

    youtube_video_id: str

    title: str

    duration_seconds: int = 0

    created_at: Optional[str] = None


class VideoAnalysisStatusSchema(BaseModel):

    video_id: int

    status: str

    current_index: int = 0

    total_chunks: int = 0


class WatchLogSchema(BaseModel):

    id: int

    youtube_video_id: str

    watched_seconds: int = 0

    watched_date: Optional[str] = None

    created_at: Optional[str] = None


class VideoStatsSchema(BaseModel):

    total_videos: int = 0

    analyzed_videos: int = 0

    completed_videos: int = 0

    total_hours: float = 0

    watched_hours: float = 0

    progress_percent: float = 0


class VideoResponseSchema(BaseModel):

    status: str = "ok"

    error: Optional[str] = None

    message: Optional[str] = None
