import traceback
from datetime import datetime, timedelta

from database.connection import (
    connect_db,
    close_db,
)

from database.db_utils import (
    safe_fetchall,
    safe_fetchone,
    safe_commit,
)

from services.youtube_service import (
    extract_playlist_id,
    get_playlist_metadata,
    get_playlist_videos,
    get_video_details,
    calculate_playlist_stats,
)

# =====================================
# HELPERS
# =====================================


def calculate_daily_target(
    total_minutes,
    target_days,
):

    if target_days <= 0:
        return 0

    return round(total_minutes / target_days)


def calculate_finish_date(
    target_days,
):

    if target_days <= 0:
        return None

    finish_date = datetime.now() + timedelta(days=target_days)

    return finish_date.strftime("%Y-%m-%d")


def calculate_playlist_progress(
    playlist,
):

    estimated = (
        playlist.get(
            "estimated_total_minutes",
            0,
        )
        or 0
    )

    completed = (
        playlist.get(
            "completed_minutes",
            0,
        )
        or 0
    )

    remaining = max(
        estimated - completed,
        0,
    )

    progress = 0

    if estimated > 0:

        progress = round(
            (completed / estimated) * 100,
            2,
        )

    return {
        "remaining_minutes": remaining,
        "progress": progress,
    }


# =====================================
# GET ALL PLAYLISTS
# =====================================


def get_all_playlists():

    conn = connect_db()

    try:

        cursor = conn.cursor()

        cursor.execute("""
        SELECT
            playlists.*,
            categories.name as category
        FROM playlists

        LEFT JOIN categories
        ON playlists.category_id = categories.id

        ORDER BY order_index ASC
        """)

        playlists = safe_fetchall(cursor)

        enriched = []

        for playlist in playlists:

            progress_data = calculate_playlist_progress(playlist)

            playlist["remaining_minutes"] = progress_data["remaining_minutes"]

            playlist["yuzde"] = progress_data["progress"]

            enriched.append(playlist)

        return enriched

    finally:

        close_db(conn)


# =====================================
# IMPORT PLAYLIST
# =====================================


def import_playlist_service(
    playlist_url,
    category_name,
    goal,
):

    conn = connect_db()

    try:

        cursor = conn.cursor()

        # =====================================
        # PLAYLIST ID
        # =====================================

        playlist_id = extract_playlist_id(playlist_url)

        if not playlist_id:

            return {
                "status": "error",
                "error": "Playlist ID bulunamadı",
            }

        # =====================================
        # CATEGORY
        # =====================================

        cursor.execute(
            """
            INSERT OR IGNORE INTO categories(
                name
            )
            VALUES(?)
            """,
            (category_name,),
        )

        cursor.execute(
            """
            SELECT id
            FROM categories
            WHERE name=?
            """,
            (category_name,),
        )

        category = safe_fetchone(cursor)

        category_id = category["id"]

        # =====================================
        # METADATA
        # =====================================

        metadata = get_playlist_metadata(playlist_id)

        if not metadata:

            return {
                "status": "error",
                "error": "Playlist metadata alınamadı",
            }

        # =====================================
        # ORDER INDEX
        # =====================================

        cursor.execute("""
        SELECT COALESCE(
            MAX(order_index),
            0
        ) + 1 as next_order
        FROM playlists
        """)

        next_order = cursor.fetchone()[0]

        # =====================================
        # FETCH VIDEOS
        # =====================================

        raw_videos = get_playlist_videos(playlist_id)

        print(f"""
RAW VIDEOS:
{len(raw_videos)}
""")

        video_ids = [video["youtube_video_id"] for video in raw_videos]

        video_details = get_video_details(video_ids)

        print(f"""
VIDEO DETAILS:
{len(video_details)}
""")

        stats = calculate_playlist_stats(video_details)

        estimated_minutes = stats["total_seconds"] // 60

        # =====================================
        # UPSERT PLAYLIST
        # =====================================

        cursor.execute(
            """
            INSERT INTO playlists(

                youtube_playlist_id,
                title,
                category_id,
                goal,
                order_index,
                channel_name,
                thumbnail_url,
                video_count,
                estimated_total_minutes,
                remaining_minutes

            )
            VALUES(
                ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
            )

            ON CONFLICT(
                youtube_playlist_id
            )

            DO UPDATE SET

                title=excluded.title,
                category_id=excluded.category_id,
                goal=excluded.goal,
                channel_name=excluded.channel_name,
                thumbnail_url=excluded.thumbnail_url,
                video_count=excluded.video_count,
                estimated_total_minutes=excluded.estimated_total_minutes
            """,
            (
                playlist_id,
                metadata["title"],
                category_id,
                goal,
                next_order,
                metadata["channel_name"],
                metadata["thumbnail_url"],
                metadata["video_count"],
                estimated_minutes,
                estimated_minutes,
            ),
        )

        # =====================================
        # GET PLAYLIST ID
        # =====================================

        cursor.execute(
            """
            SELECT id
            FROM playlists
            WHERE youtube_playlist_id=?
            """,
            (playlist_id,),
        )

        playlist_row = safe_fetchone(cursor)

        db_playlist_id = playlist_row["id"]

        # =====================================
        # INSERT VIDEOS
        # =====================================

        inserted_count = 0

        for video in video_details:

            cursor.execute(
                """
                INSERT OR IGNORE INTO videos(

                    playlist_id,
                    youtube_video_id,
                    title,
                    duration_seconds

                )
                VALUES(
                    ?, ?, ?, ?
                )
                """,
                (
                    db_playlist_id,
                    video["youtube_video_id"],
                    video["title"],
                    video["duration_seconds"],
                ),
            )

            if cursor.rowcount > 0:

                inserted_count += 1

        safe_commit(conn)

        print(f"""

✅ PLAYLIST IMPORTED

TITLE:
{metadata["title"]}

CATEGORY:
{category_name}

GOAL:
{goal}

VIDEOS:
{inserted_count}

TOTAL MINUTES:
{estimated_minutes}

""")

        return {
            "status": "ok",
            "playlist_title": metadata["title"],
            "inserted_videos": inserted_count,
            "stats": stats,
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
# UPDATE PLAYLIST TARGET
# =====================================


def update_playlist_target_service(
    playlist_id,
    target_days,
    priority_level=1,
):

    conn = connect_db()

    try:

        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT *
            FROM playlists
            WHERE id=?
            """,
            (playlist_id,),
        )

        playlist = safe_fetchone(cursor)

        if not playlist:

            return {
                "status": "error",
                "error": "Playlist bulunamadı",
            }

        estimated_minutes = playlist["estimated_total_minutes"] or 0

        daily_target = calculate_daily_target(
            estimated_minutes,
            target_days,
        )

        finish_date = calculate_finish_date(target_days)

        cursor.execute(
            """
            UPDATE playlists
            SET
                target_days=?,
                daily_target_minutes=?,
                target_finish_date=?,
                priority_level=?
            WHERE id=?
            """,
            (
                target_days,
                daily_target,
                finish_date,
                priority_level,
                playlist_id,
            ),
        )

        safe_commit(conn)

        return {
            "status": "ok",
            "daily_target_minutes": daily_target,
            "target_finish_date": finish_date,
        }

    finally:

        close_db(conn)


# =====================================
# UPDATE PLAYLIST PROGRESS
# =====================================


def update_playlist_progress_service(
    playlist_id,
    watched_minutes,
):

    conn = connect_db()

    try:

        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT *
            FROM playlists
            WHERE id=?
            """,
            (playlist_id,),
        )

        playlist = safe_fetchone(cursor)

        if not playlist:

            return {
                "status": "error",
                "error": "Playlist bulunamadı",
            }

        completed = playlist["completed_minutes"] or 0

        estimated = playlist["estimated_total_minutes"] or 0

        new_completed = completed + watched_minutes

        remaining = max(
            estimated - new_completed,
            0,
        )

        is_delayed = 0

        daily_target = playlist["daily_target_minutes"] or 0

        if daily_target > 0 and watched_minutes < daily_target:

            is_delayed = 1

        cursor.execute(
            """
            UPDATE playlists
            SET
                completed_minutes=?,
                remaining_minutes=?,
                is_delayed=?,
                last_study_date=?
            WHERE id=?
            """,
            (
                new_completed,
                remaining,
                is_delayed,
                datetime.now().strftime("%Y-%m-%d"),
                playlist_id,
            ),
        )

        safe_commit(conn)

        return {
            "status": "ok",
            "completed_minutes": new_completed,
            "remaining_minutes": remaining,
            "is_delayed": is_delayed,
        }

    finally:

        close_db(conn)


# =====================================
# REORDER PLAYLISTS
# =====================================


def reorder_playlists_service(
    order,
):

    conn = connect_db()

    try:

        cursor = conn.cursor()

        for index, playlist_id in enumerate(order):

            cursor.execute(
                """
                UPDATE playlists
                SET order_index=?
                WHERE id=?
                """,
                (
                    index + 1,
                    playlist_id,
                ),
            )

        safe_commit(conn)

        return {"status": "ok"}

    finally:

        close_db(conn)


# =====================================
# GET PLAYLIST VIDEOS
# =====================================


def get_playlist_videos_service(
    playlist_id,
):

    conn = connect_db()

    try:

        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT
                *
            FROM videos
            WHERE playlist_id=?
            ORDER BY id ASC
            """,
            (playlist_id,),
        )

        videos = safe_fetchall(cursor)

        return videos

    finally:

        close_db(conn)


# =====================================
# GET CATEGORIES
# =====================================


def get_categories_service():

    conn = connect_db()

    try:

        cursor = conn.cursor()

        cursor.execute("""
        SELECT *
        FROM categories
        ORDER BY name ASC
        """)

        categories = safe_fetchall(cursor)

        return categories

    finally:

        close_db(conn)


# =====================================
# GET CATEGORY PLAYLISTS
# =====================================


def get_category_playlists_service(
    category_id,
):

    conn = connect_db()

    try:

        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT *
            FROM playlists
            WHERE category_id=?
            ORDER BY order_index ASC
            """,
            (category_id,),
        )

        playlists = safe_fetchall(cursor)

        return playlists

    finally:

        close_db(conn)
