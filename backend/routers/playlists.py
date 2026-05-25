from fastapi import APIRouter
from fastapi import HTTPException

from services.playlist_service import (
    get_all_playlists,
    import_playlist_service,
    reorder_playlists_service,
    get_playlist_videos_service,
    get_categories_service,
    get_category_playlists_service,
    update_playlist_target_service,
    update_playlist_progress_service,
)

from schemas.playlist_schema import (
    PlaylistImportSchema,
    PlaylistReorderSchema,
)

from pydantic import BaseModel

# =====================================
# EXTRA SCHEMAS
# =====================================


class PlaylistTargetSchema(BaseModel):

    playlist_id: int

    target_days: int

    priority_level: int = 1


class PlaylistProgressSchema(BaseModel):

    playlist_id: int

    watched_minutes: int


router = APIRouter(
    prefix="/playlists",
    tags=["Playlists"],
)

# =====================================
# GET ALL PLAYLISTS
# =====================================


@router.get("")
def get_playlists():

    try:

        data = get_all_playlists()

        return data

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e),
        )


# =====================================
# IMPORT PLAYLIST
# =====================================


@router.post("/import")
def import_playlist(
    payload: PlaylistImportSchema,
):

    try:

        result = import_playlist_service(
            payload.playlist_url,
            payload.category,
            payload.goal,
        )

        return result

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e),
        )


# =====================================
# REORDER PLAYLISTS
# =====================================


@router.post("/reorder")
def reorder_playlists(
    payload: PlaylistReorderSchema,
):

    try:

        result = reorder_playlists_service(payload.order)

        return result

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e),
        )


# =====================================
# UPDATE PLAYLIST TARGET
# =====================================


@router.post("/target")
def update_playlist_target(
    payload: PlaylistTargetSchema,
):

    try:

        result = update_playlist_target_service(
            payload.playlist_id,
            payload.target_days,
            payload.priority_level,
        )

        return result

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e),
        )


# =====================================
# UPDATE PLAYLIST PROGRESS
# =====================================


@router.post("/progress")
def update_playlist_progress(
    payload: PlaylistProgressSchema,
):

    try:

        result = update_playlist_progress_service(
            payload.playlist_id,
            payload.watched_minutes,
        )

        return result

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e),
        )


# =====================================
# GET PLAYLIST VIDEOS
# =====================================


@router.get("/{playlist_id}/videos")
def get_playlist_videos(
    playlist_id: int,
):

    try:

        videos = get_playlist_videos_service(playlist_id)

        return videos

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e),
        )


# =====================================
# GET CATEGORIES
# =====================================


@router.get("/categories/all")
def get_categories():

    try:

        data = get_categories_service()

        return data

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e),
        )


# =====================================
# GET CATEGORY PLAYLISTS
# =====================================


@router.get("/category/{category_id}")
def get_category_playlists(
    category_id: int,
):

    try:

        data = get_category_playlists_service(category_id)

        return data

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e),
        )


# =====================================
# LEARNING ENGINE STATS
# =====================================


@router.get("/learning/stats")
def get_learning_stats():

    try:

        playlists = get_all_playlists()

        total_minutes = sum(
            (
                playlist.get(
                    "estimated_total_minutes",
                    0,
                )
                or 0
            )
            for playlist in playlists
        )

        completed_minutes = sum(
            (
                playlist.get(
                    "completed_minutes",
                    0,
                )
                or 0
            )
            for playlist in playlists
        )

        remaining_minutes = sum(
            (
                playlist.get(
                    "remaining_minutes",
                    0,
                )
                or 0
            )
            for playlist in playlists
        )

        delayed_count = len([p for p in playlists if p.get("is_delayed")])

        progress = 0

        if total_minutes > 0:

            progress = round(
                (completed_minutes / total_minutes) * 100,
                2,
            )

        return {
            "status": "ok",
            "total_minutes": total_minutes,
            "completed_minutes": completed_minutes,
            "remaining_minutes": remaining_minutes,
            "progress": progress,
            "playlist_count": len(playlists),
            "delayed_count": delayed_count,
        }

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e),
        )
