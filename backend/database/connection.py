import sqlite3
import threading
import traceback
import time
import os

from config.settings import (
    DB_PATH,
    DB_TIMEOUT,
)

# =====================================
# GLOBAL STATE
# =====================================

active_connections = 0

connection_lock = threading.Lock()

connection_registry = {}

thread_local = threading.local()

# =====================================
# INITIALIZE DATABASE
# =====================================


def initialize_database():

    os.makedirs(
        os.path.dirname(DB_PATH),
        exist_ok=True,
    )

    conn = connect_db()

    try:

        conn.execute("SELECT 1")

        print(f"""
✅ DATABASE INITIALIZED

PATH:
{DB_PATH}
""")

    finally:

        close_db(conn)


# =====================================
# CONNECT DB
# =====================================


def connect_db():

    global active_connections

    thread_id = threading.get_ident()

    # =====================================
    # THREAD LOCAL
    # =====================================

    existing_conn = getattr(
        thread_local,
        "connection",
        None,
    )

    if existing_conn:

        try:

            existing_conn.execute("SELECT 1")

            return existing_conn

        except Exception:

            try:

                existing_conn.close()

            except Exception:
                pass

    # =====================================
    # CREATE CONNECTION
    # =====================================

    conn = sqlite3.connect(
        DB_PATH,
        timeout=DB_TIMEOUT,
        check_same_thread=False,
    )

    # =====================================
    # SQLITE SETTINGS
    # =====================================

    conn.execute("PRAGMA journal_mode=WAL;")

    conn.execute("PRAGMA synchronous=NORMAL;")

    conn.execute("PRAGMA foreign_keys=ON;")

    conn.execute("PRAGMA busy_timeout=30000;")

    conn.row_factory = sqlite3.Row

    # =====================================
    # SAVE LOCAL
    # =====================================

    thread_local.connection = conn

    # =====================================
    # DEBUG
    # =====================================

    with connection_lock:

        active_connections += 1

        connection_registry[thread_id] = {
            "created_at": time.time(),
        }

    return conn


# =====================================
# CLOSE DB
# =====================================


def close_db(
    conn=None,
):

    global active_connections

    thread_id = threading.get_ident()

    try:

        local_conn = conn or getattr(
            thread_local,
            "connection",
            None,
        )

        if local_conn:

            try:

                local_conn.close()

            except Exception:

                traceback.print_exc()

        thread_local.connection = None

    except Exception:

        traceback.print_exc()

    finally:

        with connection_lock:

            active_connections -= 1

            if active_connections < 0:

                active_connections = 0

            if thread_id in connection_registry:

                del connection_registry[thread_id]


# =====================================
# COMMIT
# =====================================


def commit_db(
    conn,
):

    try:

        conn.commit()

    except Exception:

        traceback.print_exc()

        conn.rollback()

        raise


# =====================================
# ROLLBACK
# =====================================


def rollback_db(
    conn,
):

    try:

        conn.rollback()

    except Exception:

        traceback.print_exc()


# =====================================
# DATABASE HEALTH
# =====================================


def database_health():

    try:

        conn = connect_db()

        conn.execute("SELECT 1")

        close_db(conn)

        return {
            "status": "healthy",
            "database": DB_PATH,
        }

    except Exception as e:

        return {
            "status": "error",
            "error": str(e),
        }


# =====================================
# DEBUG CONNECTIONS
# =====================================


def debug_connections():

    return {
        "active_connections": active_connections,
        "threads": list(connection_registry.keys()),
        "registry": connection_registry,
    }
