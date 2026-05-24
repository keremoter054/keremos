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
# GENERATE ANALYSIS
# =====================================


def generate_analysis(
    transcript,
):

    try:

        debug_print("ANALYSIS GENERATION START")

        # =====================================
        # LOAD PROMPT
        # =====================================

        system_prompt = load_prompt("analysis_prompt.txt")

        # =====================================
        # CHUNK TRANSCRIPT
        # =====================================

        chunks = smart_chunk(transcript)

        analyses = []

        # =====================================
        # PROCESS CHUNKS
        # =====================================

        for index, chunk in enumerate(chunks):

            print(f"""
🧠 ANALYSIS CHUNK

{index + 1}/{len(chunks)}
""")

            user_prompt = f"""
Deeply analyze this content:

{chunk}
"""

            response = ask_ai(
                system_prompt=system_prompt,
                user_prompt=user_prompt,
            )

            if response:

                analyses.append(response)

        # =====================================
        # MERGE ANALYSIS
        # =====================================

        final_analysis = merge_chunks(analyses)

        debug_print("ANALYSIS COMPLETE")

        return final_analysis

    except Exception as e:

        debug_error(
            "ANALYSIS GENERATOR ERROR",
            e,
        )

        traceback.print_exc()

        return ""


# =====================================
# GENERATE ANALYSIS JSON
# =====================================


def generate_analysis_json(
    transcript,
):

    analysis = generate_analysis(transcript)

    return {
        "status": "ok",
        "analysis": analysis,
    }


# =====================================
# ANALYSIS ANALYTICS
# =====================================


def analysis_analytics(
    analysis,
):

    words = len(analysis.split())

    characters = len(analysis)

    sections = analysis.count("#")

    recommendations = analysis.lower().count("recommend")

    return {
        "words": words,
        "characters": characters,
        "sections": sections,
        "recommendations": recommendations,
    }


# =====================================
# ANALYSIS EXISTS
# =====================================


def analysis_exists(
    analysis,
):

    if not analysis:

        return False

    cleaned = analysis.strip()

    if len(cleaned) < 100:

        return False

    return True


# =====================================
# CLEAN ANALYSIS
# =====================================


def clean_analysis(
    analysis,
):

    return analysis.strip()


# =====================================
# GENERATE ARCHITECTURE ANALYSIS
# =====================================


def generate_architecture_analysis(
    transcript,
):

    try:

        system_prompt = """
You are a senior software architect.

Analyze:
- architecture
- layers
- scalability
- dependencies
- workflows
- optimization opportunities
- bottlenecks
- engineering quality

Use markdown formatting.
"""

        user_prompt = f"""
Analyze this architecture:

{transcript}
"""

        response = ask_ai(
            system_prompt=system_prompt,
            user_prompt=user_prompt,
        )

        return response

    except Exception as e:

        debug_error(
            "ARCHITECTURE ANALYSIS ERROR",
            e,
        )

        return ""


# =====================================
# GENERATE LEARNING ANALYSIS
# =====================================


def generate_learning_analysis(
    transcript,
):

    try:

        system_prompt = """
You are a learning systems expert.

Analyze:
- learning structure
- concept hierarchy
- prerequisite knowledge
- educational flow
- memory optimization
- weak areas
- mastery opportunities
"""

        user_prompt = f"""
Analyze this learning content:

{transcript}
"""

        response = ask_ai(
            system_prompt=system_prompt,
            user_prompt=user_prompt,
        )

        return response

    except Exception as e:

        debug_error(
            "LEARNING ANALYSIS ERROR",
            e,
        )

        return ""


# =====================================
# GENERATE OPTIMIZATION REPORT
# =====================================


def generate_optimization_report(
    transcript,
):

    try:

        system_prompt = """
You are a performance optimization engineer.

Analyze:
- inefficiencies
- bottlenecks
- scalability risks
- automation opportunities
- optimization potential
- workflow improvements
"""

        user_prompt = f"""
Generate an optimization report:

{transcript}
"""

        response = ask_ai(
            system_prompt=system_prompt,
            user_prompt=user_prompt,
        )

        return response

    except Exception as e:

        debug_error(
            "OPTIMIZATION REPORT ERROR",
            e,
        )

        return ""
