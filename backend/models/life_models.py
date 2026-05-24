from pydantic import BaseModel
from pydantic import Field

from typing import Optional

# =====================================
# LIFE DAY MODEL
# =====================================


class LifeDayModel(BaseModel):

    id: int

    date: str

    overall_progress: float = 0

    created_at: Optional[str] = None

    class Config:

        from_attributes = True


# =====================================
# LIFE TASK MODEL
# =====================================


class LifeTaskModel(BaseModel):

    id: int

    day_id: int

    task_name: str

    progress: float = 0

    completed: bool = False

    start_time: Optional[str] = None

    end_time: Optional[str] = None

    created_at: Optional[str] = None

    class Config:

        from_attributes = True


# =====================================
# LIFE TODO MODEL
# =====================================


class LifeTodoModel(BaseModel):

    id: Optional[int] = None

    task_id: Optional[int] = None

    text: str

    completed: bool = False

    todo_type: Optional[str] = None

    created_at: Optional[str] = None

    class Config:

        from_attributes = True


# =====================================
# SAVE TASK MODEL
# =====================================


class SaveTaskModel(BaseModel):

    task_name: str = Field(
        ...,
        min_length=1,
    )

    progress: float = 0

    completed: bool = False

    start_time: Optional[str] = None

    end_time: Optional[str] = None

    pendingTasks: list[LifeTodoModel] = []

    todayTasks: list[LifeTodoModel] = []

    developments: list[LifeTodoModel] = []


# =====================================
# SAVE DAY MODEL
# =====================================


class SaveDayModel(BaseModel):

    date: str

    overall_progress: float = 0

    tasks: list[SaveTaskModel] = []


# =====================================
# COPY DAY MODEL
# =====================================


class CopyDayModel(BaseModel):

    source_date: str

    target_dates: list[str]


# =====================================
# LIFE HISTORY MODEL
# =====================================


class LifeHistoryModel(BaseModel):

    days: list[LifeDayModel] = []


# =====================================
# AUTO RESCHEDULE MODEL
# =====================================


class AutoRescheduleModel(BaseModel):

    moved_tasks: int = 0

    source_day: Optional[str] = None

    target_day: Optional[str] = None


# =====================================
# PRODUCTIVITY MODEL
# =====================================


class ProductivityModel(BaseModel):

    average_progress: float = 0

    tracked_days: int = 0

    total_completed_tasks: int = 0

    total_pending_tasks: int = 0


# =====================================
# SHIFT BLOCK MODEL
# =====================================


class ShiftBlockModel(BaseModel):

    shift_type: str

    work_start: str

    work_end: str

    sleep_start: Optional[str] = None

    sleep_end: Optional[str] = None


# =====================================
# TIMELINE BLOCK MODEL
# =====================================


class TimelineBlockModel(BaseModel):

    start_time: str

    end_time: str

    title: str

    completed: bool = False

    color: Optional[str] = None
