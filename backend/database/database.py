import sqlite3
import os
import threading
import time
import traceback
from datetime import datetime

# =====================================
# GLOBAL DEBUG
# =====================================

active_connections = 0
connection_lock = threading.Lock()

connection_registry = {}

# =====================================
# THREAD LOCAL
# =====================================

thread_local = threading.local()

# =====================================
# BASE PATH
# =====================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DB_FOLDER = os.path.join(
    BASE_DIR,
    "data",
)

DB_PATH = os.path.join(
    DB_FOLDER,
    "app.db",
)

BACKUP_FOLDER = os.path.join(
    BASE_DIR,
    "backups",
)

os.makedirs(DB_FOLDER, exist_ok=True)
os.makedirs(BACKUP_FOLDER, exist_ok=True)

# =====================================
# CONNECT DB
# =====================================


def connect_db():

    global active_connections

    # =====================================
    # THREAD LOCAL CONNECTION
    # =====================================

    if hasattr(thread_local, "conn"):

        try:

            thread_local.conn.execute("SELECT 1")

            return thread_local.conn

        except Exception:

            try:
                thread_local.conn.close()

            except Exception:
                pass

            del thread_local.conn

    # =====================================
    # NEW CONNECTION
    # =====================================

    conn = sqlite3.connect(
        DB_PATH,
        timeout=30,
        check_same_thread=False,
    )

    conn.row_factory = sqlite3.Row

    # =====================================
    # PRAGMA
    # =====================================

    conn.execute("PRAGMA synchronous=NORMAL;")
    conn.execute("PRAGMA foreign_keys=ON;")
    conn.execute("PRAGMA busy_timeout=30000;")

    # =====================================
    # THREAD SAVE
    # =====================================

    thread_local.conn = conn

    # =====================================
    # DEBUG
    # =====================================

    thread_id = threading.get_ident()

    connection_id = id(conn)

    with connection_lock:

        active_connections += 1

        connection_registry[connection_id] = {
            "thread_id": thread_id,
            "created_at": time.strftime("%Y-%m-%d %H:%M:%S"),
        }

    print(f"""
🔌 DB CONNECTED

THREAD:
{thread_id}

CONNECTION:
{connection_id}

ACTIVE:
{active_connections}
""")

    return conn


# =====================================
# SAFE CLOSE
# =====================================


def close_db(conn):

    global active_connections

    if not conn:
        return

    try:

        connection_id = id(conn)

        conn.close()

        print(f"""
🔒 DB CLOSED

CONNECTION:
{connection_id}
""")

    except Exception:

        traceback.print_exc()

    finally:

        with connection_lock:

            active_connections -= 1

            if active_connections < 0:
                active_connections = 0

            if connection_id in connection_registry:
                del connection_registry[connection_id]

        # thread local cleanup
        if hasattr(thread_local, "conn"):

            try:
                del thread_local.conn

            except Exception:
                pass


# =====================================
# CONNECTION DEBUG
# =====================================


def debug_connections():

    return {
        "active_connections": active_connections,
        "registry": connection_registry,
    }


# =====================================
# SAFE COLUMN ADD
# =====================================


def add_column_if_not_exists(
    cursor,
    table,
    column,
    col_type,
):

    # =====================================
    # TABLE EXIST CHECK
    # =====================================

    cursor.execute(
        """
        SELECT name
        FROM sqlite_master
        WHERE type='table'
        AND name=?
        """,
        (table,),
    )

    table_exists = cursor.fetchone()

    if not table_exists:

        print(f"""
⚠️ TABLE YOK

TABLE:
{table}
""")

        return

    # =====================================
    # COLUMN CHECK
    # =====================================

    cursor.execute(f"PRAGMA table_info({table})")

    columns = [row[1] for row in cursor.fetchall()]

    if column not in columns:

        try:

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

        except Exception as e:

            print(f"""
❌ COLUMN ADD ERROR

TABLE:
{table}

COLUMN:
{column}

ERROR:
{e}
""")


# =====================================
# INIT DB
# =====================================


def init_db():

    conn = connect_db()

    cursor = conn.cursor()

    try:

        print("""
🚀 INIT DB START
""")

        # =====================================
        # WAL MODE
        # =====================================

        cursor.execute("PRAGMA journal_mode=WAL;")

        # =====================================
        # PLAYLISTS
        # =====================================

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS playlists (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            youtube_playlist_id TEXT UNIQUE,
            title TEXT,
            category_id INTEGER,
            order_index INTEGER DEFAULT 0,
            channel_name TEXT,
            thumbnail_url TEXT,
            video_count INTEGER DEFAULT 0
        )
        """)

        # =====================================
        # GOALS
        # =====================================

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS goals (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            description TEXT DEFAULT '',
            status TEXT DEFAULT 'active',
            progress REAL DEFAULT 0,
            deadline_date TEXT,
            deleted INTEGER DEFAULT 0,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP
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
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP,
            FOREIGN KEY(goal_id)
            REFERENCES goals(id)
        )
        """)

        # =====================================
        # ROADMAPS
        # =====================================

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS roadmaps (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            goal_id INTEGER,
            title TEXT,
            completed INTEGER DEFAULT 0,
            deleted INTEGER DEFAULT 0,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP,
            FOREIGN KEY(goal_id)
            REFERENCES goals(id)
        )
        """)

        # =====================================
        # MILESTONES
        # =====================================

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS milestones (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            goal_id INTEGER,
            title TEXT,
            completed INTEGER DEFAULT 0,
            deleted INTEGER DEFAULT 0,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP,
            FOREIGN KEY(goal_id)
            REFERENCES goals(id)
        )
        """)

        # =====================================
        # GOAL STATS
        # =====================================

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS goal_stats (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            goal_id INTEGER,
            value REAL DEFAULT 0,
            note TEXT,
            deleted INTEGER DEFAULT 0,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP,
            FOREIGN KEY(goal_id)
            REFERENCES goals(id)
        )
        """)

        # =====================================
        # SAFE MIGRATIONS
        # =====================================

        add_column_if_not_exists(
            cursor,
            "playlists",
            "goal_id",
            "INTEGER",
        )

        # =====================================
        # INDEXES
        # =====================================

        cursor.execute("""
        CREATE INDEX IF NOT EXISTS idx_goals_status
        ON goals(status)
        """)

        cursor.execute("""
        CREATE INDEX IF NOT EXISTS idx_goals_deleted
        ON goals(deleted)
        """)

        cursor.execute("""
        CREATE INDEX IF NOT EXISTS idx_goal_todos_goal
        ON goal_todos(goal_id)
        """)

        cursor.execute("""
        CREATE INDEX IF NOT EXISTS idx_goal_todos_completed
        ON goal_todos(completed)
        """)

        cursor.execute("""
        CREATE INDEX IF NOT EXISTS idx_goal_stats_goal
        ON goal_stats(goal_id)
        """)

        # =====================================
        # TRIGGERS
        # =====================================

        cursor.execute("""
        CREATE TRIGGER IF NOT EXISTS trg_goals_updated_at
        AFTER UPDATE ON goals
        FOR EACH ROW
        WHEN NEW.updated_at IS OLD.updated_at
        BEGIN
            UPDATE goals
            SET updated_at = CURRENT_TIMESTAMP
            WHERE id = NEW.id;
        END;
        """)

        cursor.execute("""
        CREATE TRIGGER IF NOT EXISTS trg_goal_todos_updated_at
        AFTER UPDATE ON goal_todos
        FOR EACH ROW
        WHEN NEW.updated_at IS OLD.updated_at
        BEGIN
            UPDATE goal_todos
            SET updated_at = CURRENT_TIMESTAMP
            WHERE id = NEW.id;
        END;
        """)

        conn.commit()

        print("""
✅ INIT DB SUCCESS
""")

    except Exception as e:

        conn.rollback()

        print(f"""
❌ INIT DB ERROR

ERROR:
{e}
""")

        traceback.print_exc()

    finally:

        close_db(conn)


# =====================================
# OPTIMIZE DB
# =====================================


def optimize_db():

    conn = connect_db()

    try:

        conn.execute("PRAGMA wal_checkpoint(TRUNCATE)")

        conn.execute("VACUUM")

        conn.execute("PRAGMA optimize")

        conn.commit()

        print("""
✅ DB OPTIMIZED
""")

    finally:

        close_db(conn)


# =====================================
# DB HEALTH CHECK
# =====================================


def db_health():

    conn = connect_db()

    try:

        cursor = conn.cursor()

        cursor.execute("PRAGMA integrity_check")

        integrity_result = cursor.fetchone()[0]

        cursor.execute("PRAGMA journal_mode")

        journal_mode = cursor.fetchone()[0]

        return {
            "integrity": integrity_result,
            "journal_mode": journal_mode,
            "active_connections": active_connections,
        }

    finally:

        close_db(conn)


# =====================================
# SQLITE SAFE BACKUP
# =====================================


def backup_db():

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    backup_path = os.path.join(
        BACKUP_FOLDER,
        f"app_backup_{timestamp}.db",
    )

    source_conn = connect_db()

    backup_conn = None

    try:

        backup_conn = sqlite3.connect(backup_path)

        source_conn.backup(backup_conn)

        backup_conn.close()

        print(f"""
✅ SQLITE BACKUP SUCCESS

PATH:
{backup_path}
""")

        return backup_path

    except Exception:

        traceback.print_exc()

        return None

    finally:

        if backup_conn:

            try:
                backup_conn.close()

            except Exception:
                pass

        close_db(source_conn)
