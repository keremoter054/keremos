import json
import time
import traceback

from openai import OpenAI

from config.settings import (
    OPENAI_API_KEY,
)

from config.ai_models import (
    DEFAULT_CHAT_MODEL,
    DEFAULT_REASONING_MODEL,
    AI_MAX_RETRIES,
    AI_RETRY_DELAY,
    AI_TEMPERATURES,
    FLASHCARD_SYSTEM_PROMPT,
    NOTES_SYSTEM_PROMPT,
    SUMMARY_SYSTEM_PROMPT,
)

# =====================================
# OPENAI CLIENT
# =====================================

client = OpenAI(api_key=OPENAI_API_KEY)

# =====================================
# ASK AI
# =====================================


def ask_ai(
    prompt,
    system_prompt="",
    model=DEFAULT_CHAT_MODEL,
    temperature=None,
):

    if temperature is None:

        temperature = AI_TEMPERATURES["balanced"]

    response = client.chat.completions.create(
        model=model,
        temperature=temperature,
        messages=[
            {
                "role": "system",
                "content": system_prompt,
            },
            {
                "role": "user",
                "content": prompt,
            },
        ],
    )

    return response.choices[0].message.content


# =====================================
# ASK AI SAFE
# =====================================


def ask_ai_safe(
    prompt,
    system_prompt="",
    model=DEFAULT_CHAT_MODEL,
    temperature=None,
):

    last_error = None

    for attempt in range(AI_MAX_RETRIES):

        try:

            result = ask_ai(
                prompt=prompt,
                system_prompt=system_prompt,
                model=model,
                temperature=temperature,
            )

            return result

        except Exception as e:

            last_error = e

            print(f"""
❌ AI ERROR

ATTEMPT:
{attempt + 1}

ERROR:
{e}
""")

            traceback.print_exc()

            time.sleep(AI_RETRY_DELAY)

    return f"""
AI ERROR:
{last_error}
"""


# =====================================
# GENERATE FLASHCARDS
# =====================================


def generate_flashcards_ai(
    text,
):

    prompt = f"""
Aşağıdaki metinden kaliteli
Anki cloze flashcardları üret.

Kurallar:

- Sadece cloze formatı kullan
- Her satır tek kart olsun
- Gereksiz kart üretme
- Önemli bilgileri seç

METİN:

{text}
"""

    result = ask_ai_safe(
        prompt=prompt,
        system_prompt=FLASHCARD_SYSTEM_PROMPT,
        temperature=AI_TEMPERATURES["stable"],
    )

    cards = []

    for line in result.split("\n"):

        cleaned = line.strip()

        if "{{c1:" in cleaned:

            cards.append(cleaned)

    return cards


# =====================================
# GENERATE SUMMARY
# =====================================


def generate_summary_ai(
    text,
):

    prompt = f"""
Aşağıdaki transcripti düzenli
şekilde özetle.

Başlıklar kullan.
Önemli noktaları çıkar.

TRANSCRIPT:

{text}
"""

    result = ask_ai_safe(
        prompt=prompt,
        system_prompt=SUMMARY_SYSTEM_PROMPT,
        temperature=AI_TEMPERATURES["balanced"],
    )

    return result


# =====================================
# GENERATE NOTES
# =====================================


def generate_notes_ai(
    text,
):

    prompt = f"""
Aşağıdaki transcripti profesyonel
ders notuna dönüştür.

Kurallar:

- Başlık kullan
- Açıklama yap
- Gerekirse örnek ver
- Düzenli markdown kullan

TRANSCRIPT:

{text}
"""

    result = ask_ai_safe(
        prompt=prompt,
        system_prompt=NOTES_SYSTEM_PROMPT,
        temperature=AI_TEMPERATURES["balanced"],
    )

    return result


# =====================================
# FIX CLOZE
# =====================================


def fix_cloze(
    text,
):

    if "{{c1:" in text:

        return text

    return "{{c1:" + text + "}}"


# =====================================
# SIMILARITY
# =====================================


def similarity(
    text1,
    text2,
):

    text1 = text1.lower().strip()

    text2 = text2.lower().strip()

    if text1 == text2:

        return 1.0

    words1 = set(text1.split())

    words2 = set(text2.split())

    intersection = words1.intersection(words2)

    union = words1.union(words2)

    if not union:

        return 0

    return len(intersection) / len(union)


# =====================================
# PARSE JSON SAFE
# =====================================


def parse_json_safe(
    text,
):

    try:

        return json.loads(text)

    except Exception:

        traceback.print_exc()

        return None


# =====================================
# AI HEALTH CHECK
# =====================================


def ai_health_check():

    try:

        result = ask_ai_safe(
            prompt="Hello",
            system_prompt="You are alive.",
        )

        return {
            "status": "ok",
            "response": result,
        }

    except Exception as e:

        return {
            "status": "error",
            "error": str(e),
        }
