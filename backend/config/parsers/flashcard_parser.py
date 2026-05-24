import re

from utils.debug_utils import (
    debug_error,
)

# =====================================
# PARSE FLASHCARDS
# =====================================


def parse_flashcards(
    text,
):

    try:

        flashcards = []

        seen = set()

        lines = text.splitlines()

        for line in lines:

            cleaned = clean_flashcard(line)

            if not cleaned:

                continue

            # =====================================
            # VALIDATION
            # =====================================

            if not is_valid_flashcard(cleaned):

                continue

            # =====================================
            # DUPLICATE CHECK
            # =====================================

            normalized = normalize_flashcard(cleaned)

            if normalized in seen:

                continue

            seen.add(normalized)

            flashcards.append(cleaned)

        return flashcards

    except Exception as e:

        debug_error(
            "FLASHCARD PARSER ERROR",
            e,
        )

        return []


# =====================================
# CLEAN FLASHCARD
# =====================================


def clean_flashcard(
    text,
):

    if not text:

        return ""

    cleaned = text.strip()

    # =====================================
    # REMOVE BULLETS
    # =====================================

    cleaned = re.sub(
        r"^[-*•]\s*",
        "",
        cleaned,
    )

    # =====================================
    # REMOVE NUMBERING
    # =====================================

    cleaned = re.sub(
        r"^\d+\.\s*",
        "",
        cleaned,
    )

    return cleaned.strip()


# =====================================
# VALID FLASHCARD
# =====================================


def is_valid_flashcard(
    text,
):

    if not text:

        return False

    # =====================================
    # MIN LENGTH
    # =====================================

    if len(text) < 10:

        return False

    # =====================================
    # CLOZE CHECK
    # =====================================

    if "{{c1:" not in text:

        return False

    # =====================================
    # VALID CLOZE FORMAT
    # =====================================

    pattern = r"\{\{c1:(.*?)\}\}"

    match = re.search(
        pattern,
        text,
    )

    if not match:

        return False

    cloze_content = match.group(1)

    if len(cloze_content.strip()) < 1:

        return False

    return True


# =====================================
# NORMALIZE FLASHCARD
# =====================================


def normalize_flashcard(
    text,
):

    normalized = text.lower().strip()

    normalized = re.sub(
        r"\s+",
        " ",
        normalized,
    )

    return normalized


# =====================================
# EXTRACT CLOZE
# =====================================


def extract_cloze(
    flashcard,
):

    pattern = r"\{\{c1:(.*?)\}\}"

    match = re.search(
        pattern,
        flashcard,
    )

    if not match:

        return None

    return match.group(1)


# =====================================
# EXTRACT CONTEXT
# =====================================


def extract_context(
    flashcard,
):

    pattern = r"\{\{c1:(.*?)\}\}"

    context = re.sub(
        pattern,
        "_____",
        flashcard,
    )

    return context


# =====================================
# COUNT CLOZES
# =====================================


def count_clozes(
    flashcard,
):

    matches = re.findall(
        r"\{\{c\d+:(.*?)\}\}",
        flashcard,
    )

    return len(matches)


# =====================================
# FILTER DUPLICATES
# =====================================


def filter_duplicates(
    flashcards,
):

    unique = []

    seen = set()

    for card in flashcards:

        normalized = normalize_flashcard(card)

        if normalized in seen:

            continue

        seen.add(normalized)

        unique.append(card)

    return unique


# =====================================
# FLASHCARD STATS
# =====================================


def flashcard_stats(
    flashcards,
):

    total = len(flashcards)

    average_length = 0

    if total > 0:

        average_length = round(
            sum(len(card) for card in flashcards) / total,
            1,
        )

    return {
        "total": total,
        "average_length": average_length,
    }


# =====================================
# PARSE FLASHCARDS JSON
# =====================================


def parse_flashcards_json(
    text,
):

    cards = parse_flashcards(text)

    return {
        "status": "ok",
        "total": len(cards),
        "flashcards": cards,
    }
