from pydantic import BaseModel
from pydantic import Field

from typing import Optional

# =====================================
# GOAL MODEL
# =====================================


class GoalModel(BaseModel):

    id: int

    title: str

    description: str = ""

    status: str = "active"

    progress: float = 0

    deadline_date: Optional[str] = None

    updated_at: Optional[str] = None

    created_at: Optional[str] = None

    deleted: int = 0

    class Config:

        from_attributes = True


# =====================================
# GOAL TODO MODEL
# =====================================


class GoalTodoModel(BaseModel):

    id: int

    goal_id: int

    text: str

    completed: int = 0

    updated_at: Optional[str] = None

    created_at: Optional[str] = None

    deleted: int = 0

    class Config:

        from_attributes = True


# =====================================
# ROADMAP MODEL
# =====================================


class RoadmapModel(BaseModel):

    id: int

    goal_id: int

    title: str

    completed: int = 0

    updated_at: Optional[str] = None

    created_at: Optional[str] = None

    deleted: int = 0

    class Config:

        from_attributes = True


# =====================================
# MILESTONE MODEL
# =====================================


class MilestoneModel(BaseModel):

    id: int

    goal_id: int

    title: str

    completed: int = 0

    updated_at: Optional[str] = None

    created_at: Optional[str] = None

    deleted: int = 0

    class Config:

        from_attributes = True


# =====================================
# GOAL STAT MODEL
# =====================================


class GoalStatModel(BaseModel):

    id: int

    goal_id: int

    value: float = 0

    note: str = ""

    updated_at: Optional[str] = None

    created_at: Optional[str] = None

    deleted: int = 0

    class Config:

        from_attributes = True


# =====================================
# CREATE GOAL MODEL
# =====================================


class CreateGoalModel(BaseModel):

    title: str = Field(
        ...,
        min_length=1,
        max_length=255,
    )

    description: str = ""

    deadline_date: Optional[str] = None


# =====================================
# UPDATE GOAL MODEL
# =====================================


class UpdateGoalModel(BaseModel):

    title: str

    description: str = ""

    status: str = "active"

    progress: float = 0

    deadline_date: Optional[str] = None


# =====================================
# GOAL REQUIREMENT MODEL
# =====================================


class GoalRequirementModel(BaseModel):

    goal_id: int

    text: str = Field(
        ...,
        min_length=1,
    )


# =====================================
# GOAL PREDICTION MODEL
# =====================================


class GoalPredictionModel(BaseModel):

    total_requirements: int = 0

    completed_requirements: int = 0

    remaining_requirements: int = 0

    progress: float = 0

    estimated_days: int = 0


# =====================================
# GOAL RESPONSE MODEL
# =====================================


class GoalResponseModel(BaseModel):

    status: str = "ok"

    goal_id: Optional[int] = None

    error: Optional[str] = None


# =====================================
# GOAL ANALYTICS MODEL
# =====================================


class GoalAnalyticsModel(BaseModel):

    goal_id: int

    title: str

    progress: float = 0

    total_requirements: int = 0

    completed_requirements: int = 0
