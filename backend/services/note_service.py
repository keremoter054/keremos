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
    generate_notes_ai,
    generate_summary_ai,
)

# =====================================
# GENERATE NOTES
# =====================================


def generate_notes_service(
    video_id,
):

    conn = connect_db()

    try:

        cursor = conn.cursor()

        # =====================================
        # GET TRANSCRIPT
        # =====================================

        cursor.execute(
            """
        SELECT
            transcript
        FROM video_analysis
        WHERE video_id=?
        """,
            (video_id,),
        )

        row = safe_fetchone(cursor)

        if not row:

            return {
                "status": "error",
                "error": "Transcript bulunamadı",
            }

        transcript = row["transcript"]

        # =====================================
        # AI GENERATE NOTES
        # =====================================

        notes = generate_notes_ai(transcript)

        summary = generate_summary_ai(transcript)

        # =====================================
        # SAVE FULL NOTE
        # =====================================

        cursor.execute(
            """
        INSERT INTO video_full_notes(

            video_id,
            content

        )
        VALUES(
            ?, ?
        )

        ON CONFLICT(video_id)

        DO UPDATE SET

            content=
            excluded.content
        """,
            (
                video_id,
                notes,
            ),
        )

        # =====================================
        # SAVE SUMMARY NOTE
        # =====================================

        cursor.execute(
            """
        INSERT INTO notes(

            video_id,
            question,
            answer,
            status

        )
        VALUES(
            ?, ?, ?, ?
        )
        """,
            (
                video_id,
                "AI Summary",
                summary,
                "generated",
            ),
        )

        safe_commit(conn)

        print(f"""
✅ NOTES GENERATED

VIDEO:
{video_id}
""")

        return {
            "status": "ok",
            "summary": summary,
            "notes": notes,
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
# GET NOTES
# =====================================


def get_notes_service(
    video_id,
):

    conn = connect_db()

    try:

        cursor = conn.cursor()

        cursor.execute(
            """
        SELECT *
        FROM notes
        WHERE video_id=?
        ORDER BY id DESC
        """,
            (video_id,),
        )

        notes = safe_fetchall(cursor)

        return notes

    finally:

        close_db(conn)


# =====================================
# GET FULL NOTE
# =====================================


def get_full_note_service(
    video_id,
):

    conn = connect_db()

    try:

        cursor = conn.cursor()

        cursor.execute(
            """
        SELECT *
        FROM video_full_notes
        WHERE video_id=?
        """,
            (video_id,),
        )

        note = safe_fetchone(cursor)

        return note

    finally:

        close_db(conn)


# =====================================
# DELETE NOTE
# =====================================


def delete_note_service(
    note_id,
):

    conn = connect_db()

    try:

        cursor = conn.cursor()

        cursor.execute(
            """
        DELETE FROM notes
        WHERE id=?
        """,
            (note_id,),
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
# DELETE VIDEO NOTES
# =====================================


def delete_video_notes_service(
    video_id,
):

    conn = connect_db()

    try:

        cursor = conn.cursor()

        # =====================================
        # DELETE NOTES
        # =====================================

        cursor.execute(
            """
        DELETE FROM notes
        WHERE video_id=?
        """,
            (video_id,),
        )

        deleted_notes = cursor.rowcount

        # =====================================
        # DELETE FULL NOTES
        # =====================================

        cursor.execute(
            """
        DELETE FROM video_full_notes
        WHERE video_id=?
        """,
            (video_id,),
        )

        deleted_full_notes = cursor.rowcount

        safe_commit(conn)

        return {
            "status": "ok",
            "deleted_notes": deleted_notes,
            "deleted_full_notes": deleted_full_notes,
        }

    finally:

        close_db(conn)
