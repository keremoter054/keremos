from pydantic import BaseModel
from pydantic import Field

from typing import Optional


class LifeTodoSchema(BaseModel):

    id: Optional[int] = None

    task_id: Optional[int] = None

    text: str

    completed: bool = False

    todo_type: Optional[str] = None

    created_at: Optional[str] = None


class LifeTaskSchema(BaseModel):

    id: Optional[int] = None

    day_id: Optional[int] = None

    task_name: str = Field(
        ...,
        min_length=1,
    )

    progress: float = 0

    completed: bool = False

    start_time: Optional[str] = None

    end_time: Optional[str] = None

    pendingTasks: list[LifeTodoSchema] = []

    todayTasks: list[LifeTodoSchema] = []

    developments: list[LifeTodoSchema] = []


class SaveDaySchema(BaseModel):

    date: str

    overall_progress: float = 0

    tasks: list[LifeTaskSchema] = []


class CopyDaySchema(BaseModel):

    source_date: str

    target_dates: list[str]


class LifeDaySchema(BaseModel):

    id: int

    date: str

    overall_progress: float = 0

    created_at: Optional[str] = None


class LifeHistorySchema(BaseModel):

    days: list[LifeDaySchema] = []


class AutoRescheduleSchema(BaseModel):

    moved_tasks: int = 0

    source_day: Optional[str] = None

    target_day: Optional[str] = None


class ProductivitySchema(BaseModel):

    average_progress: float = 0

    tracked_days: int = 0

    total_completed_tasks: int = 0

    total_pending_tasks: int = 0


class ShiftBlockSchema(BaseModel):

    shift_type: str

    work_start: str

    work_end: str

    sleep_start: Optional[str] = None

    sleep_end: Optional[str] = None


class TimelineBlockSchema(BaseModel):

    start_time: str

    end_time: str

    title: str

    completed: bool = False

    color: Optional[str] = None


class LifeResponseSchema(BaseModel):

    status: str = "ok"

    day_id: Optional[int] = None

    error: Optional[str] = None

    message: Optional[str] = None
