import sqlite3
import time
import traceback

# =====================================
# SAFE EXECUTE
# =====================================


def safe_execute(
    cursor,
    query,
    params=None,
):

    try:

        if params is None:

            cursor.execute(query)

        else:

            cursor.execute(
                query,
                params,
            )

        return True

    except Exception as e:

        print(f"""
❌ SAFE EXECUTE ERROR

QUERY:
{query}

PARAMS:
{params}

ERROR:
{e}
""")

        traceback.print_exc()

        return False


# =====================================
# SAFE FETCHALL
# =====================================


def safe_fetchall(cursor):

    try:

        rows = cursor.fetchall()

        return [dict(row) for row in rows]

    except Exception as e:

        print(f"""
❌ FETCHALL ERROR

ERROR:
{e}
""")

        traceback.print_exc()

        return []


# =====================================
# SAFE FETCHONE
# =====================================


def safe_fetchone(cursor):

    try:

        row = cursor.fetchone()

        if row is None:

            return None

        return dict(row)

    except Exception as e:

        print(f"""
❌ FETCHONE ERROR

ERROR:
{e}
""")

        traceback.print_exc()

        return None


# =====================================
# SAFE COMMIT
# =====================================


def safe_commit(conn):

    try:

        conn.commit()

        return True

    except Exception as e:

        print(f"""
❌ COMMIT ERROR

ERROR:
{e}
""")

        traceback.print_exc()

        return False


# =====================================
# SAFE ROLLBACK
# =====================================


def safe_rollback(conn):

    try:

        conn.rollback()

        return True

    except Exception as e:

        print(f"""
❌ ROLLBACK ERROR

ERROR:
{e}
""")

        traceback.print_exc()

        return False


# =====================================
# RETRY QUERY
# =====================================


def retry_query(
    callback,
    retries=3,
    delay=1,
):

    last_error = None

    for attempt in range(retries):

        try:

            return callback()

        except sqlite3.OperationalError as e:

            last_error = e

            print(f"""
⚠️ RETRY QUERY

ATTEMPT:
{attempt + 1}

ERROR:
{e}
""")

            time.sleep(delay)

        except Exception as e:

            last_error = e

            traceback.print_exc()

            break

    print(f"""
❌ RETRY FAILED

ERROR:
{last_error}
""")

    return None


# =====================================
# ROW TO DICT
# =====================================


def row_to_dict(row):

    if row is None:

        return None

    return dict(row)


# =====================================
# ROWS TO LIST
# =====================================


def rows_to_list(rows):

    return [dict(row) for row in rows]


# =====================================
# CHECK TABLE EXISTS
# =====================================


def table_exists(
    cursor,
    table_name,
):

    cursor.execute(
        """
    SELECT name
    FROM sqlite_master
    WHERE type='table'
    AND name=?
    """,
        (table_name,),
    )

    return cursor.fetchone() is not None


# =====================================
# CHECK COLUMN EXISTS
# =====================================


def column_exists(
    cursor,
    table_name,
    column_name,
):

    cursor.execute(f"PRAGMA table_info({table_name})")

    columns = [row[1] for row in cursor.fetchall()]

    return column_name in columns
