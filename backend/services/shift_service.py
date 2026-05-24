from datetime import datetime
from datetime import timedelta

from database.connection import (
    connect_db,
    close_db,
)

from database.db_utils import (
    safe_fetchall,
    safe_fetchone,
    safe_commit,
)

# =====================================
# GET SHIFT PLAN
# =====================================


def get_shift_plan_service():

    conn = connect_db()

    try:

        cursor = conn.cursor()

        cursor.execute("""
        SELECT *
        FROM shifts
        ORDER BY shift_date ASC
        """)

        shifts = safe_fetchall(cursor)

        return shifts

    finally:

        close_db(conn)


# =====================================
# GET TODAY SHIFT
# =====================================


def get_today_shift_service():

    conn = connect_db()

    try:

        cursor = conn.cursor()

        today = datetime.now().strftime("%Y-%m-%d")

        cursor.execute(
            """
        SELECT *
        FROM shifts
        WHERE shift_date=?
        """,
            (today,),
        )

        shift = safe_fetchone(cursor)

        return shift

    finally:

        close_db(conn)


# =====================================
# CREATE SHIFT
# =====================================


def create_shift_service(
    payload,
):

    conn = connect_db()

    try:

        cursor = conn.cursor()

        cursor.execute(
            """
        INSERT INTO shifts(

            shift_date,
            shift_type,
            work_start,
            work_end,
            note

        )
        VALUES(
            ?, ?, ?, ?, ?
        )
        """,
            (
                payload.shift_date,
                payload.shift_type,
                payload.work_start,
                payload.work_end,
                payload.note,
            ),
        )

        safe_commit(conn)

        return {
            "status": "ok",
            "shift_id": cursor.lastrowid,
        }

    finally:

        close_db(conn)


# =====================================
# UPDATE SHIFT
# =====================================


def update_shift_service(
    shift_id,
    payload,
):

    conn = connect_db()

    try:

        cursor = conn.cursor()

        cursor.execute(
            """
        UPDATE shifts

        SET

            shift_date=?,
            shift_type=?,
            work_start=?,
            work_end=?,
            note=?

        WHERE id=?
        """,
            (
                payload.shift_date,
                payload.shift_type,
                payload.work_start,
                payload.work_end,
                payload.note,
                shift_id,
            ),
        )

        safe_commit(conn)

        return {"status": "ok"}

    finally:

        close_db(conn)


# =====================================
# DELETE SHIFT
# =====================================


def delete_shift_service(
    shift_id,
):

    conn = connect_db()

    try:

        cursor = conn.cursor()

        cursor.execute(
            """
        DELETE FROM shifts
        WHERE id=?
        """,
            (shift_id,),
        )

        safe_commit(conn)

        return {"status": "ok"}

    finally:

        close_db(conn)


# =====================================
# GENERATE SHIFT CYCLE
# =====================================


def generate_shift_cycle_service():

    conn = connect_db()

    try:

        cursor = conn.cursor()

        # =====================================
        # CLEAR OLD SHIFTS
        # =====================================

        cursor.execute("""
        DELETE FROM shifts
        """)

        # =====================================
        # SHIFT ROTATION
        # =====================================

        rotation = [
            {
                "type": "Sabah",
                "start": "08:00",
                "end": "16:00",
            },
            {
                "type": "Akşam",
                "start": "16:00",
                "end": "00:00",
            },
            {
                "type": "Gece",
                "start": "00:00",
                "end": "08:00",
            },
        ]

        start_date = datetime.now()

        total_days = 180

        rotation_index = 0

        # =====================================
        # GENERATE
        # =====================================

        for i in range(total_days):

            current_date = start_date + timedelta(days=i)

            shift = rotation[rotation_index]

            cursor.execute(
                """
            INSERT INTO shifts(

                shift_date,
                shift_type,
                work_start,
                work_end,
                note

            )
            VALUES(
                ?, ?, ?, ?, ?
            )
            """,
                (
                    current_date.strftime("%Y-%m-%d"),
                    shift["type"],
                    shift["start"],
                    shift["end"],
                    "",
                ),
            )

            # =====================================
            # CHANGE EVERY 7 DAYS
            # =====================================

            if (i + 1) % 7 == 0:

                rotation_index += 1

                if rotation_index >= len(rotation):

                    rotation_index = 0

        safe_commit(conn)

        return {
            "status": "ok",
            "generated_days": total_days,
        }

    finally:

        close_db(conn)
