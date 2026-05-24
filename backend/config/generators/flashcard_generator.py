import json
import traceback

from services.ai_service import (
    ask_ai,
)

from prompts.prompt_loader import (
    load_prompt,
)

from utils.debug_utils import (
    debug_print,
    debug_error,
)

# =====================================
# GENERATE FLASHCARDS
# =====================================


def generate_flashcards(
    transcript,
):

    try:

        # =====================================
        # LOAD PROMPT
        # =====================================

        system_prompt = load_prompt("flashcard_prompt.txt")

        # =====================================
        # USER PROMPT
        # =====================================

        user_prompt = f"""
Generate cloze flashcards
from this content:

{transcript}
"""

        debug_print("FLASHCARD GENERATION START")

        # =====================================
        # AI REQUEST
        # =====================================

        response = ask_ai(
            system_prompt=system_prompt,
            user_prompt=user_prompt,
        )

        if not response:

            return []

        # =====================================
        # PARSE RESPONSE
        # =====================================

        flashcards = parse_flashcards(response)

        debug_print(
            "FLASHCARDS GENERATED",
            len(flashcards),
        )

        return flashcards

    except Exception as e:

        debug_error(
            "FLASHCARD GENERATOR ERROR",
            e,
        )

        traceback.print_exc()

        return []


# =====================================
# PARSE FLASHCARDS
# =====================================


def parse_flashcards(
    text,
):

    flashcards = []

    lines = text.splitlines()

    seen = set()

    for line in lines:

        cleaned = line.strip()

        if not cleaned:

            continue

        # =====================================
        # DUPLICATE CHECK
        # =====================================

        if cleaned in seen:

            continue

        # =====================================
        # CLOZE CHECK
        # =====================================

        if "{{c1:" not in cleaned:

            continue

        seen.add(cleaned)

        flashcards.append(cleaned)

    return flashcards


# =====================================
# GENERATE FLASHCARDS JSON
# =====================================


def generate_flashcards_json(
    transcript,
):

    cards = generate_flashcards(transcript)

    return {
        "status": "ok",
        "total": len(cards),
        "flashcards": cards,
    }


# =====================================
# FLASHCARD ANALYTICS
# =====================================


def flashcard_analytics(
    flashcards,
):

    total = len(flashcards)

    cloze_count = sum(1 for card in flashcards if "{{c1:" in card)

    average_length = 0

    if total > 0:

        average_length = round(
            sum(len(card) for card in flashcards) / total,
            1,
        )

    return {
        "total": total,
        "cloze_cards": cloze_count,
        "average_length": average_length,
    }


# =====================================
# EXPORT FLASHCARDS TXT
# =====================================


def export_flashcards_txt(
    flashcards,
):

    return "\n".join(flashcards)


# =====================================
# EXPORT FLASHCARDS JSON
# =====================================


def export_flashcards_json(
    flashcards,
):

    return json.dumps(
        flashcards,
        ensure_ascii=False,
        indent=4,
    )


# =====================================
# FILTER VALID FLASHCARDS
# =====================================


def filter_valid_flashcards(
    flashcards,
):

    valid = []

    for card in flashcards:

        if not isinstance(
            card,
            str,
        ):

            continue

        if "{{c1:" not in card:

            continue

        if len(card.strip()) < 10:

            continue

        valid.append(card.strip())

    return valid
