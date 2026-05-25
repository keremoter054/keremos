from database.connection import (
    connect_db,
    close_db,
)

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

        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )

    """)

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
    # COMMIT
    # =====================================

    conn.commit()

    close_db(conn)

    print("""
✅ MIGRATIONS COMPLETE
""")
