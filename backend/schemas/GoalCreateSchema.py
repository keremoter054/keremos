from typing import Optional

from pydantic import BaseModel

# =====================================
# GOAL CREATE SCHEMA
# =====================================


class GoalCreateSchema(BaseModel):

    title: str

    description: str = ""

    estimated_minutes: int = 0

    deadline_date: Optional[str] = None


# =====================================
# GOAL UPDATE SCHEMA
# =====================================


class GoalUpdateSchema(BaseModel):

    title: Optional[str] = None

    description: Optional[str] = None

    status: Optional[str] = None

    progress: Optional[float] = None

    estimated_minutes: Optional[int] = None

    actual_minutes: Optional[int] = None

    difference_minutes: Optional[int] = None

    remaining_minutes: Optional[int] = None

    deadline_date: Optional[str] = None
