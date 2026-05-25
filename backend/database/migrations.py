from database.connection import (
    connect_db,
    close_db,
)

# =====================================
# SAFE COLUMN ADD
# =====================================


def add_column_if_not_exists(
    cursor,
    table,
    column,
    col_type,
):

    cursor.execute(f"PRAGMA table_info({table})")

    columns = [row[1] for row in cursor.fetchall()]

    if column not in columns:

        cursor.execute(f"""
            ALTER TABLE {table}
            ADD COLUMN {column} {col_type}
            """)

        print(f"""
✅ COLUMN ADDED

TABLE:
{table}

COLUMN:
{column}
""")


# =====================================
# RUN MIGRATIONS
# =====================================


def run_migrations():

    conn = connect_db()

    cursor = conn.cursor()

    # =====================================
    # CATEGORIES
    # =====================================

    cursor.execute("""

    CREATE TABLE IF NOT EXISTS categories (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        name TEXT UNIQUE
    )

    """)

    # =====================================
    # PLAYLISTS
    # =====================================

    cursor.execute("""

    CREATE TABLE IF NOT EXISTS playlists (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        youtube_playlist_id TEXT UNIQUE,

        title TEXT,

        category_id INTEGER,

        channel_name TEXT,

        thumbnail_url TEXT,

        video_count INTEGER DEFAULT 0,

        order_index INTEGER DEFAULT 0,

        goal_id INTEGER,


        target_days INTEGER DEFAULT 0,

        daily_target_minutes INTEGER DEFAULT 0,

        estimated_total_minutes INTEGER DEFAULT 0,

        completed_minutes INTEGER DEFAULT 0,

        remaining_minutes INTEGER DEFAULT 0,

        priority_level INTEGER DEFAULT 1,

        speed_required REAL DEFAULT 0,

        speed_current REAL DEFAULT 0,

        is_delayed INTEGER DEFAULT 0,

        status TEXT DEFAULT 'active',

        target_finish_date TEXT,

        last_study_date TEXT,

        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )

    """)

    # =====================================
    # SAFE PLAYLIST MIGRATIONS
    # =====================================

    add_column_if_not_exists(
        cursor,
        "playlists",
        "goal_id",
        "INTEGER",
    )

    add_column_if_not_exists(
        cursor,
        "playlists",
        "target_days",
        "INTEGER DEFAULT 0",
    )

    add_column_if_not_exists(
        cursor,
        "playlists",
        "daily_target_minutes",
        "INTEGER DEFAULT 0",
    )

    add_column_if_not_exists(
        cursor,
        "playlists",
        "estimated_total_minutes",
        "INTEGER DEFAULT 0",
    )

    add_column_if_not_exists(
        cursor,
        "playlists",
        "completed_minutes",
        "INTEGER DEFAULT 0",
    )

    add_column_if_not_exists(
        cursor,
        "playlists",
        "remaining_minutes",
        "INTEGER DEFAULT 0",
    )

    add_column_if_not_exists(
        cursor,
        "playlists",
        "priority_level",
        "INTEGER DEFAULT 1",
    )

    add_column_if_not_exists(
        cursor,
        "playlists",
        "speed_required",
        "REAL DEFAULT 0",
    )

    add_column_if_not_exists(
        cursor,
        "playlists",
        "speed_current",
        "REAL DEFAULT 0",
    )

    add_column_if_not_exists(
        cursor,
        "playlists",
        "is_delayed",
        "INTEGER DEFAULT 0",
    )

    add_column_if_not_exists(
        cursor,
        "playlists",
        "status",
        "TEXT DEFAULT 'active'",
    )

    add_column_if_not_exists(
        cursor,
        "playlists",
        "target_finish_date",
        "TEXT",
    )

    add_column_if_not_exists(
        cursor,
        "playlists",
        "last_study_date",
        "TEXT",
    )

    # =====================================
    # VIDEOS
    # =====================================

    cursor.execute("""

    CREATE TABLE IF NOT EXISTS videos (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        playlist_id INTEGER,

        youtube_video_id TEXT,

        title TEXT,

        duration_seconds INTEGER DEFAULT 0,

        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )

    """)

    # =====================================
    # FLASHCARDS
    # =====================================

    cursor.execute("""

    CREATE TABLE IF NOT EXISTS flashcards (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        video_id INTEGER,

        content TEXT,

        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )

    """)

    # =====================================
    # NOTES
    # =====================================

    cursor.execute("""

    CREATE TABLE IF NOT EXISTS notes (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        video_id INTEGER,

        content TEXT,

        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )

    """)

    # =====================================
    # VIDEO ANALYSIS
    # =====================================

    cursor.execute("""

    CREATE TABLE IF NOT EXISTS video_analysis (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        video_id INTEGER UNIQUE,

        summary TEXT,

        notes TEXT,

        analysis TEXT,

        status TEXT DEFAULT 'pending',

        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )

    """)

    # =====================================
    # GOALS
    # =====================================

    cursor.execute("""

    CREATE TABLE IF NOT EXISTS goals (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        title TEXT,

        description TEXT,

        deadline_date TEXT,

        status TEXT DEFAULT 'active',

        progress REAL DEFAULT 0,

        estimated_minutes INTEGER DEFAULT 0,

        actual_minutes INTEGER DEFAULT 0,

        difference_minutes INTEGER DEFAULT 0,

        remaining_minutes INTEGER DEFAULT 0,

        deleted INTEGER DEFAULT 0,

        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )

    """)

    # =====================================
    # GOAL TODOS
    # =====================================

    cursor.execute("""

    CREATE TABLE IF NOT EXISTS goal_todos (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        goal_id INTEGER,

        text TEXT,

        completed INTEGER DEFAULT 0,

        deleted INTEGER DEFAULT 0,

        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )

    """)

    # =====================================
    # INDEXES
    # =====================================

    cursor.execute("""
    CREATE INDEX IF NOT EXISTS idx_playlists_order
    ON playlists(order_index)
    """)

    cursor.execute("""
    CREATE INDEX IF NOT EXISTS idx_playlists_status
    ON playlists(status)
    """)

    cursor.execute("""
    CREATE INDEX IF NOT EXISTS idx_videos_playlist
    ON videos(playlist_id)
    """)

    # =====================================
    # COMMIT
    # =====================================

    conn.commit()

    close_db(conn)

    print("""

✅ MIGRATIONS COMPLETE

🚀 LEARNING ENGINE READY

""")
