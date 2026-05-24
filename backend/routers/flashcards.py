from fastapi import APIRouter
from fastapi import HTTPException

from services.flashcard_service import (
    generate_flashcards_service,
    get_flashcards_service,
    review_flashcard_service,
    send_all_flashcards_service,
    delete_flashcards_by_video_service,
    delete_all_flashcards_service,
)

from schemas.flashcard_schema import (
    FlashcardReviewSchema,
)

router = APIRouter(
    prefix="/flashcards",
    tags=["Flashcards"],
)

# =====================================
# GENERATE FLASHCARDS
# =====================================


@router.post("/generate/{video_id}")
def generate_flashcards(
    video_id: int,
):

    try:

        result = generate_flashcards_service(video_id)

        return result

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e),
        )


# =====================================
# GET FLASHCARDS
# =====================================


@router.get("/{video_id}")
def get_flashcards(
    video_id: int,
):

    try:

        result = get_flashcards_service(video_id)

        return result

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e),
        )


# =====================================
# REVIEW FLASHCARD
# =====================================


@router.post("/review")
def review_flashcard(
    payload: FlashcardReviewSchema,
):

    try:

        result = review_flashcard_service(payload)

        return result

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e),
        )


# =====================================
# SEND ALL TO ANKI
# =====================================


@router.post("/send-all/{video_id}")
def send_all_flashcards(
    video_id: int,
):

    try:

        result = send_all_flashcards_service(video_id)

        return result

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e),
        )


# =====================================
# DELETE VIDEO FLASHCARDS
# =====================================


@router.delete("/video/{video_id}")
def delete_flashcards_by_video(
    video_id: int,
):

    try:

        result = delete_flashcards_by_video_service(video_id)

        return result

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e),
        )


# =====================================
# DELETE ALL FLASHCARDS
# =====================================


@router.delete("/all")
def delete_all_flashcards():

    try:

        result = delete_all_flashcards_service()

        return result

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e),
        )
