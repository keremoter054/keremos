from fastapi import APIRouter
from fastapi import HTTPException

from services.shift_service import (
    get_shift_plan_service,
    get_today_shift_service,
    create_shift_service,
    update_shift_service,
    delete_shift_service,
    generate_shift_cycle_service,
)

from schemas.shift_schema import (
    ShiftCreateSchema,
    ShiftUpdateSchema,
)

router = APIRouter(
    prefix="/shifts",
    tags=["Shifts"],
)

# =====================================
# GET SHIFT PLAN
# =====================================


@router.get("")
def get_shift_plan():

    try:

        result = get_shift_plan_service()

        return result

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e),
        )


# =====================================
# GET TODAY SHIFT
# =====================================


@router.get("/today")
def get_today_shift():

    try:

        result = get_today_shift_service()

        return result

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e),
        )


# =====================================
# CREATE SHIFT
# =====================================


@router.post("/create")
def create_shift(
    payload: ShiftCreateSchema,
):

    try:

        result = create_shift_service(payload)

        return result

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e),
        )


# =====================================
# UPDATE SHIFT
# =====================================


@router.put("/update/{shift_id}")
def update_shift(
    shift_id: int,
    payload: ShiftUpdateSchema,
):

    try:

        result = update_shift_service(
            shift_id,
            payload,
        )

        return result

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e),
        )


# =====================================
# DELETE SHIFT
# =====================================


@router.delete("/{shift_id}")
def delete_shift(
    shift_id: int,
):

    try:

        result = delete_shift_service(shift_id)

        return result

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e),
        )


# =====================================
# GENERATE SHIFT CYCLE
# =====================================


@router.post("/generate-cycle")
def generate_shift_cycle():

    try:

        result = generate_shift_cycle_service()

        return result

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e),
        )
