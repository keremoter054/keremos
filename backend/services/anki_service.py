import requests
import traceback

from config.settings import (
    ANKI_URL,
)

# =====================================
# ANKI REQUEST
# =====================================


def anki_request(
    action,
    params=None,
):

    try:

        payload = {
            "action": action,
            "version": 6,
            "params": params or {},
        }

        response = requests.post(
            ANKI_URL,
            json=payload,
            timeout=30,
        )

        data = response.json()

        return data

    except Exception as e:

        print(f"""
❌ ANKI REQUEST ERROR

ACTION:
{action}

ERROR:
{e}
""")

        traceback.print_exc()

        return {
            "result": None,
            "error": str(e),
        }


# =====================================
# CREATE DECK
# =====================================


def create_deck(
    deck_name,
):

    return anki_request(
        "createDeck",
        {
            "deck": deck_name,
        },
    )


# =====================================
# GET DECKS
# =====================================


def get_decks():

    return anki_request("deckNames")


# =====================================
# GET MODELS
# =====================================


def get_models():

    return anki_request("modelNames")


# =====================================
# ADD NOTE
# =====================================


def add_note(
    deck_name,
    front,
    back="",
    tags=None,
    model_name="Cloze",
):

    if tags is None:

        tags = []

    note = {
        "deckName": deck_name,
        "modelName": model_name,
        "fields": {
            "Text": front,
            "Back Extra": back,
        },
        "tags": tags,
        "options": {
            "allowDuplicate": False,
        },
    }

    return anki_request(
        "addNote",
        {
            "note": note,
        },
    )


# =====================================
# ADD BASIC NOTE
# =====================================


def add_basic_note(
    deck_name,
    front,
    back,
    tags=None,
):

    if tags is None:

        tags = []

    note = {
        "deckName": deck_name,
        "modelName": "Basic",
        "fields": {
            "Front": front,
            "Back": back,
        },
        "tags": tags,
    }

    return anki_request(
        "addNote",
        {
            "note": note,
        },
    )


# =====================================
# DELETE NOTES
# =====================================


def delete_notes(
    note_ids,
):

    return anki_request(
        "deleteNotes",
        {
            "notes": note_ids,
        },
    )


# =====================================
# FIND NOTES
# =====================================


def find_notes(
    query,
):

    return anki_request(
        "findNotes",
        {
            "query": query,
        },
    )


# =====================================
# UPDATE NOTE TAGS
# =====================================


def add_tags(
    note_ids,
    tags,
):

    return anki_request(
        "addTags",
        {
            "notes": note_ids,
            "tags": tags,
        },
    )


# =====================================
# TEST BASIC
# =====================================


def test_basic_note():

    result = add_basic_note(
        deck_name="KeremOS-Test",
        front="Test Front",
        back="Test Back",
    )

    return result


# =====================================
# TEST CLOZE
# =====================================


def test_cloze_note():

    result = add_note(
        deck_name="KeremOS-Test",
        front="Python {{c1:backend}} geliştirmede kullanılır.",
        back="Cloze test",
    )

    return result


# =====================================
# ANKI HEALTH CHECK
# =====================================


def anki_health_check():

    try:

        result = anki_request("version")

        return {
            "status": "ok",
            "anki_version": result.get("result"),
        }

    except Exception as e:

        return {
            "status": "error",
            "error": str(e),
        }
