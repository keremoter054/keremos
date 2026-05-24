from fastapi import APIRouter
from fastapi import HTTPException

from services.worker_service import (
    get_worker_status_service,
    start_worker_service,
    stop_worker_service,
    restart_worker_service,
    get_queue_status_service,
    clear_queue_service,
)

router = APIRouter(
    prefix="/workers",
    tags=["Workers"],
)

# =====================================
# GET WORKER STATUS
# =====================================


@router.get("/status")
def get_worker_status():

    try:

        result = get_worker_status_service()

        return result

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e),
        )


# =====================================
# START WORKER
# =====================================


@router.post("/start")
def start_worker():

    try:

        result = start_worker_service()

        return result

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e),
        )


# =====================================
# STOP WORKER
# =====================================


@router.post("/stop")
def stop_worker():

    try:

        result = stop_worker_service()

        return result

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e),
        )


# =====================================
# RESTART WORKER
# =====================================


@router.post("/restart")
def restart_worker():

    try:

        result = restart_worker_service()

        return result

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e),
        )


# =====================================
# GET QUEUE STATUS
# =====================================


@router.get("/queue")
def get_queue_status():

    try:

        result = get_queue_status_service()

        return result

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e),
        )


# =====================================
# CLEAR QUEUE
# =====================================


@router.delete("/queue")
def clear_queue():

    try:

        result = clear_queue_service()

        return result

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e),
        )
