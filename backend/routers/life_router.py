from fastapi import APIRouter
from backend.database.database import connect_db

router = APIRouter(prefix="/life", tags=["Life System"])


@router.post("/locked-block")
def create_locked_block(data: dict):

    title = data.get("title")
    start_time = data.get("start_time")
    end_time = data.get("end_time")
    repeat_type = data.get("repeat_type", "daily")

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute(
        """
    INSERT INTO locked_blocks (
        title,
        start_time,
        end_time,
        repeat_type
    )
    VALUES (?, ?, ?, ?)
    """,
        (title, start_time, end_time, repeat_type),
    )

    conn.commit()
    conn.close()

    return {"status": "ok"}


@router.get("/locked-blocks")
def get_locked_blocks():

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT *
    FROM locked_blocks
    ORDER BY start_time ASC
    """)

    rows = cursor.fetchall()

    conn.close()

    return [dict(r) for r in rows]


@router.post("/shift")
def create_shift(data: dict):

    date = data.get("date")
    shift_type = data.get("shift_type")

    work_start = data.get("work_start")
    work_end = data.get("work_end")

    sleep_start = data.get("sleep_start")
    sleep_end = data.get("sleep_end")

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute(
        """
    INSERT INTO shifts (
        date,
        shift_type,
        work_start,
        work_end,
        sleep_start,
        sleep_end
    )
    VALUES (?, ?, ?, ?, ?, ?)
    """,
        (date, shift_type, work_start, work_end, sleep_start, sleep_end),
    )

    conn.commit()
    conn.close()

    return {"status": "ok"}


@router.get("/shifts")
def get_shifts():

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT *
    FROM shifts
    ORDER BY date ASC
    """)

    rows = cursor.fetchall()

    conn.close()

    return [dict(r) for r in rows]


@router.post("/daily-task")
def create_daily_task(data: dict):

    date = data.get("date")

    start_time = data.get("start_time")
    end_time = data.get("end_time")

    title = data.get("title")

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute(
        """
    INSERT INTO daily_tasks (
        date,
        start_time,
        end_time,
        title
    )
    VALUES (?, ?, ?, ?)
    """,
        (date, start_time, end_time, title),
    )

    conn.commit()
    conn.close()

    return {"status": "ok"}


@router.get("/daily-tasks")
def get_daily_tasks():

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT *
    FROM daily_tasks
    ORDER BY start_time ASC
    """)

    rows = cursor.fetchall()

    conn.close()

    return [dict(r) for r in rows]


@router.post("/daily-task/{task_id}/toggle")
def toggle_task(task_id: int):

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute(
        """
    SELECT completed
    FROM daily_tasks
    WHERE id=?
    """,
        (task_id,),
    )

    row = cursor.fetchone()

    if not row:
        return {"error": "task not found"}

    new_value = 0 if row["completed"] == 1 else 1

    cursor.execute(
        """
    UPDATE daily_tasks
    SET completed=?
    WHERE id=?
    """,
        (new_value, task_id),
    )

    conn.commit()
    conn.close()

    return {"status": "ok", "completed": new_value}
