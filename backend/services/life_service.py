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

# =====================================
# SAVE DAY
# =====================================


def save_day_service(
    payload,
):

    conn = connect_db()

    try:

        cursor = conn.cursor()

        # =====================================
        # UPSERT DAY
        # =====================================

        cursor.execute(
            """
        INSERT INTO life_days(

            date,
            overall_progress

        )
        VALUES(
            ?, ?
        )

        ON CONFLICT(date)

        DO UPDATE SET

            overall_progress=
            excluded.overall_progress
        """,
            (
                payload.date,
                payload.overall_progress,
            ),
        )

        # =====================================
        # GET DAY ID
        # =====================================

        cursor.execute(
            """
        SELECT id
        FROM life_days
        WHERE date=?
        """,
            (payload.date,),
        )

        day_row = safe_fetchone(cursor)

        day_id = day_row["id"]

        # =====================================
        # DELETE OLD TASKS
        # =====================================

        cursor.execute(
            """
        DELETE FROM life_tasks
        WHERE day_id=?
        """,
            (day_id,),
        )

        # =====================================
        # INSERT TASKS
        # =====================================

        for task in payload.tasks:

            cursor.execute(
                """
            INSERT INTO life_tasks(

                day_id,
                task_name,
                progress,
                completed,
                start_time,
                end_time

            )
            VALUES(
                ?, ?, ?, ?, ?, ?
            )
            """,
                (
                    day_id,
                    task.task_name,
                    task.progress,
                    int(task.completed),
                    task.start_time,
                    task.end_time,
                ),
            )

            task_id = cursor.lastrowid

            # =====================================
            # TODAY TASKS
            # =====================================

            for todo in task.todayTasks:

                cursor.execute(
                    """
                INSERT INTO life_todos(

                    task_id,
                    text,
                    completed,
                    todo_type

                )
                VALUES(
                    ?, ?, ?, ?
                )
                """,
                    (
                        task_id,
                        todo.text,
                        int(todo.completed),
                        "today",
                    ),
                )

            # =====================================
            # PENDING TASKS
            # =====================================

            for pending in task.pendingTasks:

                cursor.execute(
                    """
                INSERT INTO life_todos(

                    task_id,
                    text,
                    completed,
                    todo_type

                )
                VALUES(
                    ?, ?, ?, ?
                )
                """,
                    (
                        task_id,
                        pending.text,
                        int(pending.completed),
                        "pending",
                    ),
                )

            # =====================================
            # DEVELOPMENTS
            # =====================================

            for dev in task.developments:

                cursor.execute(
                    """
                INSERT INTO life_todos(

                    task_id,
                    text,
                    completed,
                    todo_type

                )
                VALUES(
                    ?, ?, ?, ?
                )
                """,
                    (
                        task_id,
                        dev.text,
                        int(dev.completed),
                        "development",
                    ),
                )

        safe_commit(conn)

        print(f"""
✅ DAY SAVED

DATE:
{payload.date}
""")

        return {
            "status": "ok",
            "day_id": day_id,
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
# GET LIFE HISTORY
# =====================================


def get_life_history_service():

    conn = connect_db()

    try:

        cursor = conn.cursor()

        cursor.execute("""
        SELECT *
        FROM life_days
        ORDER BY date ASC
        """)

        days = safe_fetchall(cursor)

        # =====================================
        # LOAD TASKS
        # =====================================

        for day in days:

            cursor.execute(
                """
            SELECT *
            FROM life_tasks
            WHERE day_id=?
            """,
                (day["id"],),
            )

            tasks = safe_fetchall(cursor)

            # =====================================
            # LOAD TODOS
            # =====================================

            for task in tasks:

                cursor.execute(
                    """
                SELECT *
                FROM life_todos
                WHERE task_id=?
                """,
                    (task["id"],),
                )

                todos = safe_fetchall(cursor)

                task["todayTasks"] = [
                    todo for todo in todos if todo["todo_type"] == "today"
                ]

                task["pendingTasks"] = [
                    todo for todo in todos if todo["todo_type"] == "pending"
                ]

                task["developments"] = [
                    todo for todo in todos if todo["todo_type"] == "development"
                ]

            day["tasks"] = tasks

        return days

    finally:

        close_db(conn)


# =====================================
# GET DAY
# =====================================


def get_day_service(
    date,
):

    conn = connect_db()

    try:

        cursor = conn.cursor()

        cursor.execute(
            """
        SELECT *
        FROM life_days
        WHERE date=?
        """,
            (date,),
        )

        day = safe_fetchone(cursor)

        if not day:

            return None

        cursor.execute(
            """
        SELECT *
        FROM life_tasks
        WHERE day_id=?
        """,
            (day["id"],),
        )

        tasks = safe_fetchall(cursor)

        day["tasks"] = tasks

        return day

    finally:

        close_db(conn)


# =====================================
# AUTO RESCHEDULE
# =====================================


def auto_reschedule_service(
    day_id,
):

    return {
        "status": "ok",
        "message": "Auto reschedule hazır",
    }


# =====================================
# COPY DAY
# =====================================


def copy_day_service(
    payload,
):

    return {
        "status": "ok",
        "message": "Copy day hazır",
    }


# =====================================
# APPLY 21 DAY CYCLE
# =====================================


def apply_21_day_cycle_service():

    return {
        "status": "ok",
        "message": "21 day cycle hazır",
    }
