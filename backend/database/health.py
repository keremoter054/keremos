from database.connection import (
    connect_db,
    close_db,
    active_connections,
)

# =====================================
# DB HEALTH
# =====================================


def db_health():

    conn = connect_db()

    try:

        cursor = conn.cursor()

        # =====================================
        # INTEGRITY CHECK
        # =====================================

        cursor.execute("PRAGMA integrity_check")

        integrity_result = cursor.fetchone()[0]

        # =====================================
        # WAL CHECKPOINT INFO
        # =====================================

        cursor.execute("PRAGMA wal_checkpoint(PASSIVE)")

        wal_result = cursor.fetchall()

        # =====================================
        # PAGE COUNT
        # =====================================

        cursor.execute("PRAGMA page_count")

        page_count = cursor.fetchone()[0]

        # =====================================
        # PAGE SIZE
        # =====================================

        cursor.execute("PRAGMA page_size")

        page_size = cursor.fetchone()[0]

        # =====================================
        # DB SIZE
        # =====================================

        db_size_mb = round(
            (page_count * page_size) / 1024 / 1024,
            2,
        )

        return {
            "status": "ok",
            "integrity": integrity_result,
            "wal": wal_result,
            "active_connections": active_connections,
            "page_count": page_count,
            "page_size": page_size,
            "db_size_mb": db_size_mb,
        }

    finally:

        close_db(conn)


# =====================================
# OPTIMIZE DB
# =====================================


def optimize_db():

    conn = connect_db()

    try:

        # =====================================
        # WAL CHECKPOINT
        # =====================================

        conn.execute("PRAGMA wal_checkpoint(TRUNCATE)")

        # =====================================
        # VACUUM
        # =====================================

        conn.execute("VACUUM")

        # =====================================
        # SQLITE OPTIMIZE
        # =====================================

        conn.execute("PRAGMA optimize")

        conn.commit()

        print("""
✅ DB OPTIMIZED
""")

        return {"status": "ok"}

    finally:

        close_db(conn)
