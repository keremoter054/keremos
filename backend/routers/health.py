from fastapi import APIRouter
from fastapi import HTTPException

from database.health import (
    db_health,
    optimize_db,
)

from database.backup import (
    backup_db,
    list_backups,
    delete_backup,
)

from database.connection import (
    debug_connections,
)

router = APIRouter(
    prefix="/health",
    tags=["Health"],
)

# =====================================
# DB HEALTH
# =====================================


@router.get("/db")
def get_db_health():

    try:

        result = db_health()

        return result

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e),
        )


# =====================================
# OPTIMIZE DB
# =====================================


@router.post("/optimize")
def optimize_database():

    try:

        result = optimize_db()

        return result

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e),
        )


# =====================================
# CREATE BACKUP
# =====================================


@router.post("/backup")
def create_backup():

    try:

        result = backup_db()

        return result

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e),
        )


# =====================================
# LIST BACKUPS
# =====================================


@router.get("/backups")
def get_backups():

    try:

        result = list_backups()

        return result

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e),
        )


# =====================================
# DELETE BACKUP
# =====================================


@router.delete("/backup/{filename}")
def remove_backup(
    filename: str,
):

    try:

        result = delete_backup(filename)

        return result

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e),
        )


# =====================================
# CONNECTION DEBUG
# =====================================


@router.get("/connections")
def get_connection_debug():

    try:

        result = debug_connections()

        return result

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e),
        )


# =====================================
# API HEALTH
# =====================================


@router.get("")
def health_check():

    return {
        "status": "ok",
        "message": "KeremOS API running",
    }
