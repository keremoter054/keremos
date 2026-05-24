from pydantic import BaseModel

# =====================================
# SHIFT CREATE
# =====================================


class ShiftCreateSchema(BaseModel):

    date: str

    shift_type: str

    work_start: str

    work_end: str


# =====================================
# SHIFT UPDATE
# =====================================


class ShiftUpdateSchema(BaseModel):

    shift_type: str


# =====================================
# SHIFT RESPONSE
# =====================================


class ShiftResponseSchema(BaseModel):

    id: int

    date: str

    shift_type: str
