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

from utils.transcript_utils import (
    smart_chunk,
    merge_chunks,
)

# =====================================
# GENERATE SUMMARY
# =====================================


def generate_summary(
    transcript,
):

    try:

        debug_print("SUMMARY GENERATION START")

        # =====================================
        # LOAD PROMPT
        # =====================================

        system_prompt = load_prompt("summary_prompt.txt")

        # =====================================
        # CHUNK TRANSCRIPT
        # =====================================

        chunks = smart_chunk(transcript)

        summaries = []

        # =====================================
        # PROCESS CHUNKS
        # =====================================

        for index, chunk in enumerate(chunks):

            print(f"""
🧠 SUMMARY CHUNK

{index + 1}/{len(chunks)}
""")

            user_prompt = f"""
Create a structured learning summary
from this content:

{chunk}
"""

            response = ask_ai(
                system_prompt=system_prompt,
                user_prompt=user_prompt,
            )

            if response:

                summaries.append(response)

        # =====================================
        # MERGE
        # =====================================

        final_summary = merge_chunks(summaries)

        debug_print("SUMMARY COMPLETE")

        return final_summary

    except Exception as e:

        debug_error(
            "SUMMARY GENERATOR ERROR",
            e,
        )

        traceback.print_exc()

        return ""


# =====================================
# GENERATE SUMMARY JSON
# =====================================


def generate_summary_json(
    transcript,
):

    summary = generate_summary(transcript)

    return {
        "status": "ok",
        "summary": summary,
    }


# =====================================
# SUMMARY ANALYTICS
# =====================================


def summary_analytics(
    summary,
):

    words = len(summary.split())

    characters = len(summary)

    sections = summary.count("#")

    return {
        "words": words,
        "characters": characters,
        "sections": sections,
    }


# =====================================
# SUMMARY EXISTS
# =====================================


def summary_exists(
    summary,
):

    if not summary:

        return False

    cleaned = summary.strip()

    if len(cleaned) < 50:

        return False

    return True


# =====================================
# CLEAN SUMMARY
# =====================================


def clean_summary(
    summary,
):

    return summary.strip()


# =====================================
# GENERATE SHORT SUMMARY
# =====================================


def generate_short_summary(
    transcript,
):

    try:

        system_prompt = """
You are a concise summarization AI.

Create a short educational summary.

Maximum 10 bullet points.
"""

        user_prompt = f"""
Summarize this content:

{transcript}
"""

        response = ask_ai(
            system_prompt=system_prompt,
            user_prompt=user_prompt,
        )

        return response

    except Exception as e:

        debug_error(
            "SHORT SUMMARY ERROR",
            e,
        )

        return ""


# =====================================
# GENERATE KEY POINTS
# =====================================


def generate_key_points(
    transcript,
):

    try:

        system_prompt = """
Extract the most important learning points.

Return concise bullet points only.
"""

        user_prompt = f"""
Extract key points:

{transcript}
"""

        response = ask_ai(
            system_prompt=system_prompt,
            user_prompt=user_prompt,
        )

        if not response:

            return []

        return [line.strip() for line in response.splitlines() if line.strip()]

    except Exception as e:

        debug_error(
            "KEY POINT ERROR",
            e,
        )

        return []
