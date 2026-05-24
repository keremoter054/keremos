from pydantic import BaseModel
from typing import Optional


class DashboardAnalyticsModel(BaseModel):
    total_goals: int = 0
    total_playlists: int = 0
    total_videos: int = 0
    total_flashcards: int = 0
    total_notes: int = 0
    analyzed_videos: int = 0
    total_hours: float = 0


class ProductivityAnalyticsModel(BaseModel):
    average_progress: float = 0
    tracked_days: int = 0
    completed_tasks: int = 0
    pending_tasks: int = 0
    estimated_completion_days: float = 0


class VideoAnalyticsModel(BaseModel):
    total_videos: int = 0
    analyzed_videos: int = 0
    completed_videos: int = 0
    total_hours: float = 0
    watched_hours: float = 0
    progress_percent: float = 0


class GoalAnalyticsModel(BaseModel):
    goal_id: int
    title: str
    progress: float = 0
    total_requirements: int = 0
    completed_requirements: int = 0
    remaining_requirements: int = 0


class GlobalProgressModel(BaseModel):
    global_progress: float = 0
    civilization_progress: float = 0
    learning_progress: float = 0
    productivity_progress: float = 0


class CompletionPredictionModel(BaseModel):
    progress: float = 0
    remaining_tasks: int = 0
    estimated_days: float = 0
    estimated_finish_date: Optional[str] = None


class HeatmapDayModel(BaseModel):
    date: str
    value: float = 0
    completed: bool = False


class WeeklyStatsModel(BaseModel):
    week: str
    completed_tasks: int = 0
    progress: float = 0
    hours_worked: float = 0


class MonthlyStatsModel(BaseModel):
    month: str
    completed_tasks: int = 0
    progress: float = 0
    total_hours: float = 0


class AnalyticsResponseModel(BaseModel):
    status: str = "ok"
    dashboard: Optional[DashboardAnalyticsModel] = None
    productivity: Optional[ProductivityAnalyticsModel] = None
    video: Optional[VideoAnalyticsModel] = None
    global_progress: Optional[GlobalProgressModel] = None
    prediction: Optional[CompletionPredictionModel] = None


class StreakModel(BaseModel):
    current_streak: int = 0
    best_streak: int = 0
    total_active_days: int = 0


class PerformanceModel(BaseModel):
    efficiency_score: float = 0
    consistency_score: float = 0
    learning_score: float = 0
    execution_score: float = 0
