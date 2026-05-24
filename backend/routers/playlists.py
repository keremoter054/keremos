from fastapi import APIRouter
from fastapi import HTTPException

from services.playlist_service import (
    get_all_playlists,
    import_playlist_service,
    reorder_playlists_service,
    get_playlist_videos_service,
    get_categories_service,
    get_category_playlists_service,
)

from schemas.playlist_schema import (
    PlaylistImportSchema,
    PlaylistReorderSchema,
)

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
