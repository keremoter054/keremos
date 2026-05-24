from fastapi import APIRouter
from fastapi import HTTPException

from services.note_service import (
    get_notes_service,
    generate_notes_service,
    delete_note_service,
    delete_video_notes_service,
    get_full_note_service,
)

router = APIRouter(
    prefix="/notes",
    tags=["Notes"],
)

# =====================================
# GENERATE NOTES
# =====================================


@router.post("/generate/{video_id}")
def generate_notes(
    video_id: int,
):

    try:

        result = generate_notes_service(video_id)

        return result

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e),
        )


# =====================================
# GET NOTES
# =====================================


@router.get("/{video_id}")
def get_notes(
    video_id: int,
):

    try:

        result = get_notes_service(video_id)

        return result

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e),
        )


# =====================================
# GET FULL NOTE
# =====================================


@router.get("/full/{video_id}")
def get_full_note(
    video_id: int,
):

    try:

        result = get_full_note_service(video_id)

        return result

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e),
        )


# =====================================
# DELETE NOTE
# =====================================


@router.delete("/{note_id}")
def delete_note(
    note_id: int,
):

    try:

        result = delete_note_service(note_id)

        return result

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e),
        )


# =====================================
# DELETE VIDEO NOTES
# =====================================


@router.delete("/video/{video_id}")
def delete_video_notes(
    video_id: int,
):

    try:

        result = delete_video_notes_service(video_id)

        return result

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e),
        )
