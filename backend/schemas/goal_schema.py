from pydantic import BaseModel
from pydantic import Field

from typing import Optional


class GoalCreateSchema(BaseModel):

    title: str = Field(
        ...,
        min_length=1,
        max_length=255,
    )

    description: str = ""

    deadline_date: Optional[str] = None


class GoalUpdateSchema(BaseModel):

    title: str

    description: str = ""

    status: str = "active"

    progress: float = 0

    deadline_date: Optional[str] = None


class GoalRequirementSchema(BaseModel):

    goal_id: int

    text: str = Field(
        ...,
        min_length=1,
    )


class GoalSchema(BaseModel):

    id: int

    title: str

    description: str = ""

    status: str = "active"

    progress: float = 0

    deadline_date: Optional[str] = None

    updated_at: Optional[str] = None

    created_at: Optional[str] = None

    deleted: int = 0


class GoalTodoSchema(BaseModel):

    id: int

    goal_id: int

    text: str

    completed: int = 0

    updated_at: Optional[str] = None

    created_at: Optional[str] = None

    deleted: int = 0


class GoalPredictionSchema(BaseModel):

    total_requirements: int = 0

    completed_requirements: int = 0

    remaining_requirements: int = 0

    progress: float = 0

    estimated_days: int = 0


class GoalResponseSchema(BaseModel):

    status: str = "ok"

    goal_id: Optional[int] = None

    error: Optional[str] = None


class GoalAnalyticsSchema(BaseModel):

    goal_id: int

    title: str

    progress: float = 0

    total_requirements: int = 0

    completed_requirements: int = 0
