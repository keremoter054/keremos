from fastapi import APIRouter
from fastapi import HTTPException

from services.goal_service import (
    get_goals_service,
    create_goal_service,
    delete_goal_service,
    update_goal_service,
    predict_goal_service,
    add_goal_requirement_service,
    toggle_goal_requirement_service,
    delete_goal_requirement_service,
)

from schemas.goal_schema import (
    GoalCreateSchema,
    GoalUpdateSchema,
    GoalRequirementSchema,
)

router = APIRouter(
    prefix="/goals",
    tags=["Goals"],
)

# =====================================
# GET GOALS
# =====================================


@router.get("")
def get_goals():

    try:

        result = get_goals_service()

        return result

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e),
        )


# =====================================
# CREATE GOAL
# =====================================


@router.post("/create")
def create_goal(
    payload: GoalCreateSchema,
):

    try:

        result = create_goal_service(payload)

        return result

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e),
        )


# =====================================
# UPDATE GOAL
# =====================================


@router.put("/update/{goal_id}")
def update_goal(
    goal_id: int,
    payload: GoalUpdateSchema,
):

    try:

        result = update_goal_service(
            goal_id,
            payload,
        )

        return result

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e),
        )


# =====================================
# DELETE GOAL
# =====================================


@router.delete("/{goal_id}")
def delete_goal(
    goal_id: int,
):

    try:

        result = delete_goal_service(goal_id)

        return result

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e),
        )


# =====================================
# PREDICT GOAL
# =====================================


@router.get("/predict/{goal_id}")
def predict_goal(
    goal_id: int,
):

    try:

        result = predict_goal_service(goal_id)

        return result

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e),
        )


# =====================================
# ADD REQUIREMENT
# =====================================


@router.post("/requirements/add")
def add_requirement(
    payload: GoalRequirementSchema,
):

    try:

        result = add_goal_requirement_service(
            payload.goal_id,
            payload.text,
        )

        return result

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e),
        )


# =====================================
# TOGGLE REQUIREMENT
# =====================================


@router.put("/requirements/toggle/{todo_id}")
def toggle_requirement(
    todo_id: int,
):

    try:

        result = toggle_goal_requirement_service(todo_id)

        return result

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e),
        )


# =====================================
# DELETE REQUIREMENT
# =====================================


@router.delete("/requirements/{todo_id}")
def delete_requirement(
    todo_id: int,
):

    try:

        result = delete_goal_requirement_service(todo_id)

        return result

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e),
        )
