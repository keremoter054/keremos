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

from services.youtube_service import (
    extract_playlist_id,
    get_playlist_metadata,
    get_playlist_videos,
    get_video_details,
    calculate_playlist_stats,
)

# =====================================
# GET ALL PLAYLISTS
# =====================================


def get_all_playlists():

    conn = connect_db()

    try:

        cursor = conn.cursor()

        cursor.execute("""
        SELECT
            *
        FROM playlists
        ORDER BY order_index ASC
        """)

        playlists = safe_fetchall(cursor)

        return playlists

    finally:

        close_db(conn)


# =====================================
# IMPORT PLAYLIST
# =====================================


def import_playlist_service(
    playlist_url,
    category_name,
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
        # PLAYLIST METADATA
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
        # UPSERT PLAYLIST
        # =====================================

        cursor.execute(
            """
        INSERT INTO playlists(

            youtube_playlist_id,
            title,
            category_id,
            order_index,
            channel_name,
            thumbnail_url,
            video_count

        )
        VALUES(
            ?, ?, ?, ?, ?, ?, ?
        )

        ON CONFLICT(
            youtube_playlist_id
        )

        DO UPDATE SET

            title=excluded.title,
            category_id=excluded.category_id,
            channel_name=excluded.channel_name,
            thumbnail_url=excluded.thumbnail_url,
            video_count=excluded.video_count
        """,
            (
                playlist_id,
                metadata["title"],
                category_id,
                next_order,
                metadata["channel_name"],
                metadata["thumbnail_url"],
                metadata["video_count"],
            ),
        )

        # =====================================
        # GET PLAYLIST DB ID
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
        # FETCH VIDEOS
        # =====================================

        raw_videos = get_playlist_videos(playlist_id)

        video_ids = [video["youtube_video_id"] for video in raw_videos]

        video_details = get_video_details(video_ids)

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

        # =====================================
        # STATS
        # =====================================

        stats = calculate_playlist_stats(video_details)

        print(f"""
✅ PLAYLIST IMPORTED

TITLE:
{metadata["title"]}

VIDEOS:
{inserted_count}
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
