import re

from utils.debug_utils import (
    debug_error,
)

# =====================================
# PARSE NOTES
# =====================================


def parse_notes(
    text,
):

    try:

        if not text:

            return ""

        parsed = clean_notes(text)

        parsed = normalize_notes(parsed)

        return parsed

    except Exception as e:

        debug_error(
            "NOTE PARSER ERROR",
            e,
        )

        return ""


# =====================================
# CLEAN NOTES
# =====================================


def clean_notes(
    text,
):

    if not text:

        return ""

    # =====================================
    # REMOVE EXTRA SPACES
    # =====================================

    text = re.sub(
        r"\s+",
        " ",
        text,
    )

    # =====================================
    # FIX NEWLINES
    # =====================================

    text = re.sub(
        r"\n{3,}",
        "\n\n",
        text,
    )

    return text.strip()


# =====================================
# NORMALIZE NOTES
# =====================================


def normalize_notes(
    text,
):

    if not text:

        return ""

    lines = text.splitlines()

    normalized = []

    for line in lines:

        cleaned = line.strip()

        if not cleaned:

            normalized.append("")

            continue

        normalized.append(cleaned)

    return "\n".join(normalized)


# =====================================
# EXTRACT HEADINGS
# =====================================


def extract_headings(
    text,
):

    if not text:

        return []

    headings = []

    lines = text.splitlines()

    for line in lines:

        cleaned = line.strip()

        if cleaned.startswith("#"):

            headings.append(cleaned)

    return headings


# =====================================
# EXTRACT CODE BLOCKS
# =====================================


def extract_code_blocks(
    text,
):

    if not text:

        return []

    pattern = r"```(.*?)```"

    blocks = re.findall(
        pattern,
        text,
        flags=re.DOTALL,
    )

    return blocks


# =====================================
# REMOVE DUPLICATE LINES
# =====================================


def remove_duplicate_lines(
    text,
):

    if not text:

        return ""

    lines = text.splitlines()

    seen = set()

    cleaned = []

    for line in lines:

        normalized = line.strip().lower()

        if normalized in seen:

            continue

        seen.add(normalized)

        cleaned.append(line)

    return "\n".join(cleaned)


# =====================================
# NOTES WORD COUNT
# =====================================


def notes_word_count(
    text,
):

    return len(text.split())


# =====================================
# NOTES CHARACTER COUNT
# =====================================


def notes_character_count(
    text,
):

    return len(text)


# =====================================
# NOTES STATS
# =====================================


def notes_stats(
    text,
):

    headings = extract_headings(text)

    code_blocks = extract_code_blocks(text)

    return {
        "words": notes_word_count(text),
        "characters": notes_character_count(text),
        "headings": len(headings),
        "code_blocks": len(code_blocks),
    }


# =====================================
# NOTES EXISTS
# =====================================


def notes_exists(
    text,
):

    if not text:

        return False

    cleaned = text.strip()

    if len(cleaned) < 30:

        return False

    return True


# =====================================
# SPLIT NOTES SECTIONS
# =====================================


def split_note_sections(
    text,
):

    if not text:

        return []

    sections = re.split(
        r"(?=# )",
        text,
    )

    return [section.strip() for section in sections if section.strip()]


# =====================================
# EXTRACT BULLETS
# =====================================


def extract_bullets(
    text,
):

    if not text:

        return []

    bullets = []

    lines = text.splitlines()

    for line in lines:

        cleaned = line.strip()

        if cleaned.startswith("- ") or cleaned.startswith("* "):

            bullets.append(cleaned)

    return bullets
