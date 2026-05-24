from fastapi import APIRouter
from fastapi import HTTPException

from services.video_service import (
    get_video_progress_service,
    get_video_result_service,
    get_video_transcript_service,
    start_video_analysis_service,
    get_video_status_summary_service,
)

# =====================================
# ROUTER
# =====================================

router = APIRouter(
    prefix="/video",
    tags=["Videos"],
)

# =====================================
# START VIDEO ANALYSIS
# =====================================


@router.post("/analyze/start")
def start_video_analysis(
    video_id: int,
):

    try:

        return start_video_analysis_service(video_id)

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e),
        )


# =====================================
# GET VIDEO PROGRESS
# =====================================


@router.get("/progress/{video_id}")
def get_video_progress(
    video_id: int,
):

    try:

        return get_video_progress_service(video_id)

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e),
        )


# =====================================
# GET VIDEO RESULT
# =====================================


@router.get("/result/{video_id}")
def get_video_result(
    video_id: int,
):

    try:

        return get_video_result_service(video_id)

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e),
        )


# =====================================
# GET VIDEO TRANSCRIPT
# =====================================


@router.get("/transcript/{video_id}")
def get_video_transcript(
    video_id: int,
):

    try:

        return get_video_transcript_service(video_id)

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e),
        )


# =====================================
# VIDEO STATUS SUMMARY
# =====================================


@router.get("/status/summary")
def get_video_status_summary():

    try:

        return get_video_status_summary_service()

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e),
        )


# =====================================
# HEALTH TEST
# =====================================


@router.get("/health")
def video_health():

    return {
        "status": "healthy",
        "service": "video_router",
    }
