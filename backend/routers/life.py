from fastapi import APIRouter
from fastapi import HTTPException

from services.life_service import (
    save_day_service,
    get_life_history_service,
    get_day_service,
    auto_reschedule_service,
    copy_day_service,
    apply_21_day_cycle_service,
)

from schemas.life_schema import (
    SaveDaySchema,
    CopyDaySchema,
)

router = APIRouter(
    prefix="/life",
    tags=["Life"],
)

# =====================================
# SAVE DAY
# =====================================


@router.post("/save-day")
def save_day(
    payload: SaveDaySchema,
):

    try:

        result = save_day_service(payload)

        return result

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e),
        )


# =====================================
# GET HISTORY
# =====================================


@router.get("/history")
def get_history():

    try:

        result = get_life_history_service()

        return result

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e),
        )


# =====================================
# GET DAY
# =====================================


@router.get("/day/{date}")
def get_day(
    date: str,
):

    try:

        result = get_day_service(date)

        return result

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e),
        )


# =====================================
# AUTO RESCHEDULE
# =====================================


@router.post("/auto-reschedule/{day_id}")
def auto_reschedule(
    day_id: int,
):

    try:

        result = auto_reschedule_service(day_id)

        return result

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e),
        )


# =====================================
# COPY DAY
# =====================================


@router.post("/copy-day")
def copy_day(
    payload: CopyDaySchema,
):

    try:

        result = copy_day_service(payload)

        return result

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e),
        )


# =====================================
# APPLY 21 DAY CYCLE
# =====================================


@router.post("/apply-21-cycle")
def apply_21_day_cycle():

    try:

        result = apply_21_day_cycle_service()

        return result

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e),
        )
