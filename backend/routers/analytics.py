from fastapi import APIRouter
from fastapi import HTTPException

from services.analytics_service import (
    get_dashboard_analytics_service,
    get_goal_analytics_service,
    get_video_analytics_service,
    get_productivity_analytics_service,
    get_completion_prediction_service,
    get_global_progress_service,
)

router = APIRouter(
    prefix="/analytics",
    tags=["Analytics"],
)

# =====================================
# DASHBOARD ANALYTICS
# =====================================


@router.get("/dashboard")
def get_dashboard_analytics():

    try:

        result = get_dashboard_analytics_service()

        return result

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e),
        )


# =====================================
# GOAL ANALYTICS
# =====================================


@router.get("/goals")
def get_goal_analytics():

    try:

        result = get_goal_analytics_service()

        return result

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e),
        )


# =====================================
# VIDEO ANALYTICS
# =====================================


@router.get("/videos")
def get_video_analytics():

    try:

        result = get_video_analytics_service()

        return result

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e),
        )


# =====================================
# PRODUCTIVITY ANALYTICS
# =====================================


@router.get("/productivity")
def get_productivity_analytics():

    try:

        result = get_productivity_analytics_service()

        return result

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e),
        )


# =====================================
# COMPLETION PREDICTION
# =====================================


@router.get("/prediction")
def get_completion_prediction():

    try:

        result = get_completion_prediction_service()

        return result

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e),
        )


# =====================================
# GLOBAL PROGRESS
# =====================================


@router.get("/global-progress")
def get_global_progress():

    try:

        result = get_global_progress_service()

        return result

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e),
        )
