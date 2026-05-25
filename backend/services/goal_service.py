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
# GET GOALS
# =====================================


def get_goals_service():

    conn = connect_db()

    try:

        cursor = conn.cursor()

        # =====================================
        # GET GOALS
        # =====================================

        cursor.execute("""
        SELECT *
        FROM goals
        WHERE deleted=0
        ORDER BY created_at DESC
        """)

        goals = safe_fetchall(cursor)

        # =====================================
        # GET REQUIREMENTS
        # =====================================

        for goal in goals:

            cursor.execute(
                """
            SELECT *
            FROM goal_todos
            WHERE goal_id=?
            AND deleted=0
            ORDER BY id DESC
            """,
                (goal["id"],),
            )

            requirements = safe_fetchall(cursor)

            goal["requirements"] = requirements

        return goals

    finally:

        close_db(conn)


# =====================================
# CREATE GOAL
# =====================================


def create_goal_service(
    payload,
):

    conn = connect_db()

    try:

        cursor = conn.cursor()

        # =====================================
        # REMAINING TIME
        # =====================================

        remaining_minutes = payload.estimated_minutes

        cursor.execute(
            """
        INSERT INTO goals(

            title,
            description,
            deadline_date,
            status,
            progress,

            estimated_minutes,
            actual_minutes,
            difference_minutes,
            remaining_minutes

        )
        VALUES(
            ?, ?, ?, ?, ?, ?, ?, ?, ?
        )
        """,
            (
                payload.title,
                payload.description,
                payload.deadline_date,
                "active",
                0,
                payload.estimated_minutes,
                0,
                0,
                remaining_minutes,
            ),
        )

        safe_commit(conn)

        return {
            "status": "ok",
            "goal_id": cursor.lastrowid,
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
# UPDATE GOAL
# =====================================


def update_goal_service(
    goal_id,
    payload,
):

    conn = connect_db()

    try:

        cursor = conn.cursor()

        # =====================================
        # REMAINING TIME
        # =====================================

        estimated_minutes = payload.estimated_minutes or 0

        actual_minutes = payload.actual_minutes or 0

        difference_minutes = payload.difference_minutes or 0

        remaining_minutes = estimated_minutes + difference_minutes - actual_minutes

        cursor.execute(
            """
        UPDATE goals

        SET

            title=?,
            description=?,
            deadline_date=?,
            status=?,
            progress=?,

            estimated_minutes=?,
            actual_minutes=?,
            difference_minutes=?,
            remaining_minutes=?

        WHERE id=?
        """,
            (
                payload.title,
                payload.description,
                payload.deadline_date,
                payload.status,
                payload.progress,
                estimated_minutes,
                actual_minutes,
                difference_minutes,
                remaining_minutes,
                goal_id,
            ),
        )

        safe_commit(conn)

        return {"status": "ok"}

    finally:

        close_db(conn)


# =====================================
# DELETE GOAL
# =====================================


def delete_goal_service(
    goal_id,
):

    conn = connect_db()

    try:

        cursor = conn.cursor()

        cursor.execute(
            """
        UPDATE goals
        SET deleted=1
        WHERE id=?
        """,
            (goal_id,),
        )

        safe_commit(conn)

        return {"status": "ok"}

    finally:

        close_db(conn)


# =====================================
# PREDICT GOAL
# =====================================


def predict_goal_service(
    goal_id,
):

    conn = connect_db()

    try:

        cursor = conn.cursor()

        cursor.execute(
            """
        SELECT *
        FROM goal_todos
        WHERE goal_id=?
        AND deleted=0
        """,
            (goal_id,),
        )

        requirements = safe_fetchall(cursor)

        total = len(requirements)

        completed = len([r for r in requirements if r["completed"]])

        remaining = total - completed

        if total == 0:

            progress = 0

        else:

            progress = round(
                (completed / total) * 100,
                1,
            )

        estimated_days = remaining * 2

        return {
            "status": "ok",
            "total_requirements": total,
            "completed_requirements": completed,
            "remaining_requirements": remaining,
            "progress": progress,
            "estimated_days": estimated_days,
        }

    finally:

        close_db(conn)


# =====================================
# ADD REQUIREMENT
# =====================================


def add_goal_requirement_service(
    goal_id,
    text,
):

    conn = connect_db()

    try:

        cursor = conn.cursor()

        cursor.execute(
            """
        INSERT INTO goal_todos(

            goal_id,
            text,
            completed

        )
        VALUES(
            ?, ?, ?
        )
        """,
            (
                goal_id,
                text,
                0,
            ),
        )

        safe_commit(conn)

        return {
            "status": "ok",
            "todo_id": cursor.lastrowid,
        }

    finally:

        close_db(conn)


# =====================================
# TOGGLE REQUIREMENT
# =====================================


def toggle_goal_requirement_service(
    todo_id,
):

    conn = connect_db()

    try:

        cursor = conn.cursor()

        # =====================================
        # GET CURRENT
        # =====================================

        cursor.execute(
            """
        SELECT completed
        FROM goal_todos
        WHERE id=?
        """,
            (todo_id,),
        )

        row = safe_fetchone(cursor)

        if not row:

            return {
                "status": "error",
                "error": "Todo bulunamadı",
            }

        new_value = 0 if row["completed"] else 1

        # =====================================
        # UPDATE
        # =====================================

        cursor.execute(
            """
        UPDATE goal_todos
        SET completed=?
        WHERE id=?
        """,
            (
                new_value,
                todo_id,
            ),
        )

        safe_commit(conn)

        return {
            "status": "ok",
            "completed": bool(new_value),
        }

    finally:

        close_db(conn)


# =====================================
# DELETE REQUIREMENT
# =====================================


def delete_goal_requirement_service(
    todo_id,
):

    conn = connect_db()

    try:

        cursor = conn.cursor()

        cursor.execute(
            """
        UPDATE goal_todos
        SET deleted=1
        WHERE id=?
        """,
            (todo_id,),
        )

        safe_commit(conn)

        return {"status": "ok"}

    finally:

        close_db(conn)
