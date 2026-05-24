import traceback

from database.connection import (
    connect_db,
    close_db,
)

from database.db_utils import (
    safe_fetchall,
    safe_fetchone,
    safe_commit,
)

from services.ai_service import (
    generate_flashcards_ai,
    similarity,
)

from services.anki_service import (
    create_deck,
    add_note,
)

# =====================================
# GENERATE FLASHCARDS
# =====================================


def generate_flashcards_service(
    video_id,
):

    conn = connect_db()

    try:

        cursor = conn.cursor()

        # =====================================
        # GET FULL NOTE
        # =====================================

        cursor.execute(
            """
        SELECT
            content
        FROM video_full_notes
        WHERE video_id=?
        """,
            (video_id,),
        )

        row = safe_fetchone(cursor)

        if not row:

            return {
                "status": "error",
                "error": "Video note bulunamadı",
            }

        note_content = row["content"]

        # =====================================
        # AI GENERATE
        # =====================================

        generated_cards = generate_flashcards_ai(note_content)

        inserted = 0

        skipped = 0

        # =====================================
        # INSERT FLASHCARDS
        # =====================================

        for card in generated_cards:

            # duplicate check
            cursor.execute(
                """
            SELECT
                content
            FROM flashcards
            WHERE video_id=?
            """,
                (video_id,),
            )

            existing_cards = safe_fetchall(cursor)

            duplicate = False

            for existing in existing_cards:

                sim = similarity(
                    existing["content"],
                    card,
                )

                if sim > 0.92:

                    duplicate = True
                    break

            if duplicate:

                skipped += 1
                continue

            cursor.execute(
                """
            INSERT INTO flashcards(

                video_id,
                content,
                status,
                review_count

            )
            VALUES(
                ?, ?, ?, ?
            )
            """,
                (
                    video_id,
                    card,
                    "pending",
                    0,
                ),
            )

            inserted += 1

        safe_commit(conn)

        print(f"""
✅ FLASHCARDS GENERATED

VIDEO:
{video_id}

INSERTED:
{inserted}

SKIPPED:
{skipped}
""")

        return {
            "status": "ok",
            "inserted": inserted,
            "skipped": skipped,
        }

    except Exception as e:

        traceback.print_exc()

        return {
            "status": "error",
            "error": str(e),
        }

    finally:

        close_db(conn)


# =====================================
# GET FLASHCARDS
# =====================================


def get_flashcards_service(
    video_id,
):

    conn = connect_db()

    try:

        cursor = conn.cursor()

        cursor.execute(
            """
        SELECT *
        FROM flashcards
        WHERE video_id=?
        ORDER BY id DESC
        """,
            (video_id,),
        )

        cards = safe_fetchall(cursor)

        return cards

    finally:

        close_db(conn)


# =====================================
# REVIEW FLASHCARD
# =====================================


def review_flashcard_service(
    payload,
):

    conn = connect_db()

    try:

        cursor = conn.cursor()

        cursor.execute(
            """
        UPDATE flashcards

        SET

            status=?,
            review_count=
                review_count + 1

        WHERE id=?
        """,
            (
                payload.status,
                payload.flashcard_id,
            ),
        )

        safe_commit(conn)

        return {"status": "ok"}

    finally:

        close_db(conn)


# =====================================
# SEND ALL FLASHCARDS
# =====================================


def send_all_flashcards_service(
    video_id,
):

    conn = connect_db()

    try:

        cursor = conn.cursor()

        # =====================================
        # VIDEO INFO
        # =====================================

        cursor.execute(
            """
        SELECT
            title
        FROM videos
        WHERE id=?
        """,
            (video_id,),
        )

        video = safe_fetchone(cursor)

        if not video:

            return {
                "status": "error",
                "error": "Video bulunamadı",
            }

        video_title = video["title"]

        # =====================================
        # PLAYLIST INFO
        # =====================================

        cursor.execute(
            """
        SELECT
            p.title as playlist_title

        FROM playlists p

        JOIN videos v
        ON p.id = v.playlist_id

        WHERE v.id=?
        """,
            (video_id,),
        )

        playlist = safe_fetchone(cursor)

        playlist_title = playlist["playlist_title"]

        # =====================================
        # BUILD DECK
        # =====================================

        deck_name = f"KeremOS::" f"{playlist_title}::" f"{video_title}"

        create_deck(deck_name)

        # =====================================
        # GET FLASHCARDS
        # =====================================

        cursor.execute(
            """
        SELECT *
        FROM flashcards
        WHERE video_id=?
        """,
            (video_id,),
        )

        cards = safe_fetchall(cursor)

        sent = 0

        failed = 0

        # =====================================
        # SEND TO ANKI
        # =====================================

        for card in cards:

            result = add_note(
                deck_name=deck_name,
                front=card["content"],
                tags=[
                    "KeremOS",
                    "AI",
                ],
            )

            if result.get("error"):

                failed += 1

            else:

                sent += 1

        print(f"""
✅ FLASHCARDS SENT

VIDEO:
{video_id}

SENT:
{sent}

FAILED:
{failed}
""")

        return {
            "status": "ok",
            "sent": sent,
            "failed": failed,
        }

    except Exception as e:

        traceback.print_exc()

        return {
            "status": "error",
            "error": str(e),
        }

    finally:

        close_db(conn)


# =====================================
# DELETE VIDEO FLASHCARDS
# =====================================


def delete_flashcards_by_video_service(
    video_id,
):

    conn = connect_db()

    try:

        cursor = conn.cursor()

        cursor.execute(
            """
        DELETE FROM flashcards
        WHERE video_id=?
        """,
            (video_id,),
        )

        deleted = cursor.rowcount

        safe_commit(conn)

        return {
            "status": "ok",
            "deleted": deleted,
        }

    finally:

        close_db(conn)


# =====================================
# DELETE ALL FLASHCARDS
# =====================================


def delete_all_flashcards_service():

    conn = connect_db()

    try:

        cursor = conn.cursor()

        cursor.execute("""
        DELETE FROM flashcards
        """)

        deleted = cursor.rowcount

        safe_commit(conn)

        return {
            "status": "ok",
            "deleted": deleted,
        }

    finally:

        close_db(conn)
