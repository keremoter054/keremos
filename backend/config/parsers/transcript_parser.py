import re

from utils.debug_utils import (
    debug_error,
)

from utils.transcript_utils import (
    clean_transcript,
    remove_empty_lines,
)

# =====================================
# PARSE TRANSCRIPT
# =====================================


def parse_transcript(
    text,
):

    try:

        if not text:

            return ""

        # =====================================
        # CLEAN
        # =====================================

        parsed = clean_transcript(text)

        parsed = remove_empty_lines(parsed)

        return parsed

    except Exception as e:

        debug_error(
            "TRANSCRIPT PARSER ERROR",
            e,
        )

        return ""


# =====================================
# REMOVE TIMESTAMPS
# =====================================


def remove_timestamps(
    text,
):

    if not text:

        return ""

    # =====================================
    # 00:00 FORMAT
    # =====================================

    text = re.sub(
        r"\b\d{1,2}:\d{2}\b",
        "",
        text,
    )

    # =====================================
    # 00:00:00 FORMAT
    # =====================================

    text = re.sub(
        r"\b\d{1,2}:\d{2}:\d{2}\b",
        "",
        text,
    )

    return text.strip()


# =====================================
# REMOVE SPEAKER LABELS
# =====================================


def remove_speaker_labels(
    text,
):

    if not text:

        return ""

    # =====================================
    # EXAMPLES:
    # SPEAKER:
    # JOHN:
    # AI:
    # =====================================

    cleaned = re.sub(
        r"^[A-Z\s]{2,20}:\s*",
        "",
        text,
        flags=re.MULTILINE,
    )

    return cleaned.strip()


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

        if not normalized:

            continue

        if normalized in seen:

            continue

        seen.add(normalized)

        cleaned.append(line.strip())

    return "\n".join(cleaned)


# =====================================
# NORMALIZE TRANSCRIPT
# =====================================


def normalize_transcript(
    text,
):

    if not text:

        return ""

    normalized = parse_transcript(text)

    normalized = remove_timestamps(normalized)

    normalized = remove_speaker_labels(normalized)

    normalized = remove_duplicate_lines(normalized)

    return normalized.strip()


# =====================================
# SPLIT PARAGRAPHS
# =====================================


def split_paragraphs(
    text,
):

    if not text:

        return []

    paragraphs = [p.strip() for p in text.split("\n") if p.strip()]

    return paragraphs


# =====================================
# EXTRACT QUESTIONS
# =====================================


def extract_questions(
    text,
):

    if not text:

        return []

    sentences = re.split(
        r"(?<=[.!?])\s+",
        text,
    )

    questions = [sentence.strip() for sentence in sentences if "?" in sentence]

    return questions


# =====================================
# TRANSCRIPT LANGUAGE DETECT
# =====================================


def detect_transcript_language(
    text,
):

    if not text:

        return "unknown"

    turkish_chars = [
        "ç",
        "ğ",
        "ı",
        "ö",
        "ş",
        "ü",
    ]

    lowered = text.lower()

    for char in turkish_chars:

        if char in lowered:

            return "tr"

    return "en"


# =====================================
# TRANSCRIPT PARSER STATS
# =====================================


def transcript_parser_stats(
    text,
):

    paragraphs = split_paragraphs(text)

    questions = extract_questions(text)

    return {
        "paragraphs": len(paragraphs),
        "questions": len(questions),
        "language": detect_transcript_language(text),
    }


# =====================================
# TRANSCRIPT EXISTS
# =====================================


def transcript_exists(
    text,
):

    if not text:

        return False

    cleaned = text.strip()

    if len(cleaned) < 30:

        return False

    return True
