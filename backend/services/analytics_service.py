from database.connection import (
    connect_db,
    close_db,
)

from database.db_utils import (
    safe_fetchall,
    safe_fetchone,
)

# =====================================
# DASHBOARD ANALYTICS
# =====================================


def get_dashboard_analytics_service():

    conn = connect_db()

    try:

        cursor = conn.cursor()

        # =====================================
        # TOTAL GOALS
        # =====================================

        cursor.execute("""
        SELECT COUNT(*) as total
        FROM goals
        WHERE deleted=0
        """)

        total_goals = cursor.fetchone()["total"]

        # =====================================
        # TOTAL PLAYLISTS
        # =====================================

        cursor.execute("""
        SELECT COUNT(*) as total
        FROM playlists
        """)

        total_playlists = cursor.fetchone()["total"]

        # =====================================
        # TOTAL VIDEOS
        # =====================================

        cursor.execute("""
        SELECT COUNT(*) as total
        FROM videos
        """)

        total_videos = cursor.fetchone()["total"]

        # =====================================
        # TOTAL FLASHCARDS
        # =====================================

        cursor.execute("""
        SELECT COUNT(*) as total
        FROM flashcards
        """)

        total_flashcards = cursor.fetchone()["total"]

        return {
            "status": "ok",
            "total_goals": total_goals,
            "total_playlists": total_playlists,
            "total_videos": total_videos,
            "total_flashcards": total_flashcards,
        }

    finally:

        close_db(conn)


# =====================================
# GOAL ANALYTICS
# =====================================


def get_goal_analytics_service():

    conn = connect_db()

    try:

        cursor = conn.cursor()

        cursor.execute("""
        SELECT *
        FROM goals
        WHERE deleted=0
        """)

        goals = safe_fetchall(cursor)

        analytics = []

        for goal in goals:

            cursor.execute(
                """
            SELECT *
            FROM goal_todos
            WHERE goal_id=?
            AND deleted=0
            """,
                (goal["id"],),
            )

            requirements = safe_fetchall(cursor)

            total = len(requirements)

            completed = len([r for r in requirements if r["completed"]])

            progress = (
                0
                if total == 0
                else round(
                    (completed / total) * 100,
                    1,
                )
            )

            analytics.append(
                {
                    "goal_id": goal["id"],
                    "title": goal["title"],
                    "progress": progress,
                    "total_requirements": total,
                    "completed_requirements": completed,
                }
            )

        return analytics

    finally:

        close_db(conn)


# =====================================
# VIDEO ANALYTICS
# =====================================


def get_video_analytics_service():

    conn = connect_db()

    try:

        cursor = conn.cursor()

        cursor.execute("""
        SELECT
            COUNT(*) as total_videos,

            COALESCE(
                SUM(duration_seconds),
                0
            ) as total_seconds

        FROM videos
        """)

        row = safe_fetchone(cursor)

        total_hours = round(
            (row["total_seconds"] / 3600),
            2,
        )

        # =====================================
        # ANALYZED VIDEOS
        # =====================================

        cursor.execute("""
        SELECT COUNT(*) as analyzed
        FROM video_analysis
        WHERE status='done'
        """)

        analyzed = cursor.fetchone()["analyzed"]

        return {
            "total_videos": row["total_videos"],
            "total_hours": total_hours,
            "analyzed_videos": analyzed,
        }

    finally:

        close_db(conn)


# =====================================
# PRODUCTIVITY ANALYTICS
# =====================================


def get_productivity_analytics_service():

    conn = connect_db()

    try:

        cursor = conn.cursor()

        # =====================================
        # LIFE DAYS
        # =====================================

        cursor.execute("""
        SELECT *
        FROM life_days
        ORDER BY date ASC
        """)

        days = safe_fetchall(cursor)

        if not days:

            return {
                "status": "ok",
                "average_progress": 0,
                "tracked_days": 0,
            }

        total_progress = sum(day["overall_progress"] for day in days)

        average_progress = round(
            (total_progress / len(days)),
            1,
        )

        return {
            "status": "ok",
            "average_progress": average_progress,
            "tracked_days": len(days),
        }

    finally:

        close_db(conn)


# =====================================
# COMPLETION PREDICTION
# =====================================


def get_completion_prediction_service():

    conn = connect_db()

    try:

        cursor = conn.cursor()

        # =====================================
        # TOTAL TASKS
        # =====================================

        cursor.execute("""
        SELECT COUNT(*) as total
        FROM life_tasks
        """)

        total_tasks = cursor.fetchone()["total"]

        # =====================================
        # COMPLETED TASKS
        # =====================================

        cursor.execute("""
        SELECT COUNT(*) as completed
        FROM life_tasks
        WHERE completed=1
        """)

        completed_tasks = cursor.fetchone()["completed"]

        if total_tasks == 0:

            progress = 0

        else:

            progress = round(
                (completed_tasks / total_tasks) * 100,
                1,
            )

        remaining = total_tasks - completed_tasks

        estimated_days = remaining * 1.5

        return {
            "status": "ok",
            "progress": progress,
            "remaining_tasks": remaining,
            "estimated_days": estimated_days,
        }

    finally:

        close_db(conn)


# =====================================
# GLOBAL PROGRESS
# =====================================


def get_global_progress_service():

    conn = connect_db()

    try:

        cursor = conn.cursor()

        # =====================================
        # GOAL PROGRESS
        # =====================================

        cursor.execute("""
        SELECT progress
        FROM goals
        WHERE deleted=0
        """)

        goals = safe_fetchall(cursor)

        if not goals:

            return {
                "status": "ok",
                "global_progress": 0,
            }

        average_progress = round(
            sum(goal["progress"] for goal in goals) / len(goals),
            1,
        )

        return {
            "status": "ok",
            "global_progress": average_progress,
        }

    finally:

        close_db(conn)
