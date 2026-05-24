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
# GENERATE NOTES
# =====================================


def generate_notes(
    transcript,
):

    try:

        debug_print("NOTES GENERATION START")

        # =====================================
        # LOAD PROMPT
        # =====================================

        system_prompt = load_prompt("notes_prompt.txt")

        # =====================================
        # CHUNK TRANSCRIPT
        # =====================================

        chunks = smart_chunk(transcript)

        generated_notes = []

        # =====================================
        # PROCESS CHUNKS
        # =====================================

        for index, chunk in enumerate(chunks):

            print(f"""
🧠 NOTES CHUNK

{index + 1}/{len(chunks)}
""")

            user_prompt = f"""
Generate professional educational notes
from this content:

{chunk}
"""

            response = ask_ai(
                system_prompt=system_prompt,
                user_prompt=user_prompt,
            )

            if response:

                generated_notes.append(response)

        # =====================================
        # MERGE NOTES
        # =====================================

        final_notes = merge_chunks(generated_notes)

        debug_print("NOTES COMPLETE")

        return final_notes

    except Exception as e:

        debug_error(
            "NOTES GENERATOR ERROR",
            e,
        )

        traceback.print_exc()

        return ""


# =====================================
# GENERATE NOTES JSON
# =====================================


def generate_notes_json(
    transcript,
):

    notes = generate_notes(transcript)

    return {
        "status": "ok",
        "notes": notes,
    }


# =====================================
# NOTES ANALYTICS
# =====================================


def notes_analytics(
    notes,
):

    words = len(notes.split())

    characters = len(notes)

    sections = notes.count("#")

    code_blocks = notes.count("```")

    return {
        "words": words,
        "characters": characters,
        "sections": sections,
        "code_blocks": code_blocks,
    }


# =====================================
# NOTES EXISTS
# =====================================


def notes_exists(
    notes,
):

    if not notes:

        return False

    cleaned = notes.strip()

    if len(cleaned) < 50:

        return False

    return True


# =====================================
# CLEAN NOTES
# =====================================


def clean_notes(
    notes,
):

    return notes.strip()


# =====================================
# GENERATE QUICK NOTES
# =====================================


def generate_quick_notes(
    transcript,
):

    try:

        system_prompt = """
You are a concise educational note AI.

Generate short learning notes.

Focus on:
- concepts
- architecture
- workflows
- important ideas
"""

        user_prompt = f"""
Generate concise notes:

{transcript}
"""

        response = ask_ai(
            system_prompt=system_prompt,
            user_prompt=user_prompt,
        )

        return response

    except Exception as e:

        debug_error(
            "QUICK NOTES ERROR",
            e,
        )

        return ""


# =====================================
# GENERATE STUDY GUIDE
# =====================================


def generate_study_guide(
    transcript,
):

    try:

        system_prompt = """
You are a professional study guide AI.

Create:
- key concepts
- important terms
- architecture
- workflows
- learning roadmap
- practical understanding
"""

        user_prompt = f"""
Create a study guide:

{transcript}
"""

        response = ask_ai(
            system_prompt=system_prompt,
            user_prompt=user_prompt,
        )

        return response

    except Exception as e:

        debug_error(
            "STUDY GUIDE ERROR",
            e,
        )

        return ""
