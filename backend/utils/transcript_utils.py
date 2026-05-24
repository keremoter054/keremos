import re

# =====================================
# CLEAN TRANSCRIPT
# =====================================


def clean_transcript(
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
    # REMOVE DOUBLE NEWLINES
    # =====================================

    text = re.sub(
        r"\n+",
        "\n",
        text,
    )

    return text.strip()


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


# =====================================
# SMART CHUNK
# =====================================


def smart_chunk(
    text,
    max_chars=12000,
):

    chunks = []

    current = ""

    paragraphs = text.split("\n")

    for paragraph in paragraphs:

        if len(current) + len(paragraph) > max_chars:

            chunks.append(current.strip())

            current = ""

        current += paragraph + "\n"

    if current.strip():

        chunks.append(current.strip())

    return chunks


# =====================================
# WORD COUNT
# =====================================


def transcript_word_count(
    text,
):

    return len(text.split())


# =====================================
# CHARACTER COUNT
# =====================================


def transcript_character_count(
    text,
):

    return len(text)


# =====================================
# ESTIMATED MINUTES
# =====================================


def estimated_minutes(
    text,
):

    words = transcript_word_count(text)

    return round(
        words / 150,
        1,
    )


# =====================================
# TRANSCRIPT STATS
# =====================================


def transcript_stats(
    text,
):

    return {
        "characters": transcript_character_count(text),
        "words": transcript_word_count(text),
        "estimated_minutes": estimated_minutes(text),
    }


# =====================================
# MERGE CHUNKS
# =====================================


def merge_chunks(
    chunks,
):

    return "\n\n".join(chunks)


# =====================================
# SPLIT SENTENCES
# =====================================


def split_sentences(
    text,
):

    sentences = re.split(
        r"(?<=[.!?]) +",
        text,
    )

    return [s.strip() for s in sentences if s.strip()]


# =====================================
# REMOVE EMPTY LINES
# =====================================


def remove_empty_lines(
    text,
):

    lines = text.splitlines()

    cleaned = [line.strip() for line in lines if line.strip()]

    return "\n".join(cleaned)


# =====================================
# NORMALIZE TRANSCRIPT
# =====================================


def normalize_transcript(
    text,
):

    text = clean_transcript(text)

    text = remove_empty_lines(text)

    return text
