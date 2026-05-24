from pydantic import BaseModel

from typing import Optional


class DashboardAnalyticsSchema(BaseModel):

    total_goals: int = 0

    total_playlists: int = 0

    total_videos: int = 0

    total_flashcards: int = 0

    total_notes: int = 0

    analyzed_videos: int = 0

    total_hours: float = 0


class ProductivityAnalyticsSchema(BaseModel):

    average_progress: float = 0

    tracked_days: int = 0

    completed_tasks: int = 0

    pending_tasks: int = 0

    estimated_completion_days: float = 0


class VideoAnalyticsSchema(BaseModel):

    total_videos: int = 0

    analyzed_videos: int = 0

    completed_videos: int = 0

    total_hours: float = 0

    watched_hours: float = 0

    progress_percent: float = 0


class GoalAnalyticsSchema(BaseModel):

    goal_id: int

    title: str

    progress: float = 0

    total_requirements: int = 0

    completed_requirements: int = 0

    remaining_requirements: int = 0


class GlobalProgressSchema(BaseModel):

    global_progress: float = 0

    civilization_progress: float = 0

    learning_progress: float = 0

    productivity_progress: float = 0


class CompletionPredictionSchema(BaseModel):

    progress: float = 0

    remaining_tasks: int = 0

    estimated_days: float = 0

    estimated_finish_date: Optional[str] = None


class HeatmapDaySchema(BaseModel):

    date: str

    value: float = 0

    completed: bool = False


class WeeklyStatsSchema(BaseModel):

    week: str

    completed_tasks: int = 0

    progress: float = 0

    hours_worked: float = 0


class MonthlyStatsSchema(BaseModel):

    month: str

    completed_tasks: int = 0

    progress: float = 0

    total_hours: float = 0


class AnalyticsResponseSchema(BaseModel):

    status: str = "ok"

    dashboard: Optional[DashboardAnalyticsSchema] = None

    productivity: Optional[ProductivityAnalyticsSchema] = None

    video: Optional[VideoAnalyticsSchema] = None

    global_progress: Optional[GlobalProgressSchema] = None

    prediction: Optional[CompletionPredictionSchema] = None


class StreakSchema(BaseModel):

    current_streak: int = 0

    best_streak: int = 0

    total_active_days: int = 0


class PerformanceSchema(BaseModel):

    efficiency_score: float = 0

    consistency_score: float = 0

    learning_score: float = 0

    execution_score: float = 0
