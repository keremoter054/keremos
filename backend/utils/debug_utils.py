import json
import traceback
from datetime import datetime

# =====================================
# DEBUG PRINT
# =====================================


def debug_print(
    title,
    data=None,
):

    print("\n" + "=" * 50)

    print(f"🔥 DEBUG: {title}")

    print("=" * 50)

    if data is not None:

        print(data)

    print("=" * 50 + "\n")


# =====================================
# JSON DEBUG
# =====================================


def debug_json(
    title,
    data,
):

    print("\n" + "=" * 50)

    print(f"🧠 JSON DEBUG: {title}")

    print("=" * 50)

    try:

        print(
            json.dumps(
                data,
                indent=4,
                ensure_ascii=False,
            )
        )

    except Exception:

        print(data)

    print("=" * 50 + "\n")


# =====================================
# ERROR DEBUG
# =====================================


def debug_error(
    title,
    error,
):

    print("\n" + "=" * 50)

    print(f"❌ ERROR: {title}")

    print("=" * 50)

    print(error)

    traceback.print_exc()

    print("=" * 50 + "\n")


# =====================================
# TIME DEBUG
# =====================================


def debug_time(
    title,
):

    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    print(f"""
⏰ {title}

TIME:
{now}
""")


# =====================================
# FUNCTION START
# =====================================


def debug_function_start(
    function_name,
):

    print(f"""
🚀 FUNCTION START

FUNCTION:
{function_name}
""")


# =====================================
# FUNCTION END
# =====================================


def debug_function_end(
    function_name,
):

    print(f"""
✅ FUNCTION END

FUNCTION:
{function_name}
""")


# =====================================
# DEBUG SEPARATOR
# =====================================


def debug_separator():

    print("\n" + "-" * 60 + "\n")


# =====================================
# DEBUG SUCCESS
# =====================================


def debug_success(
    message,
):

    print(f"""
✅ SUCCESS

{message}
""")


# =====================================
# DEBUG WARNING
# =====================================


def debug_warning(
    message,
):

    print(f"""
⚠️ WARNING

{message}
""")


# =====================================
# DEBUG INFO
# =====================================


def debug_info(
    message,
):

    print(f"""
ℹ️ INFO

{message}
""")


# =====================================
# DEBUG LIST
# =====================================


def debug_list(
    title,
    items,
):

    print(f"""
📋 {title}
""")

    for index, item in enumerate(
        items,
        start=1,
    ):

        print(f"{index}. {item}")


# =====================================
# DEBUG DICT
# =====================================


def debug_dict(
    title,
    data,
):

    print(f"""
🧩 {title}
""")

    for key, value in data.items():

        print(f"{key}: {value}")


# =====================================
# PERFORMANCE TIMER
# =====================================


def performance_timer():

    return datetime.now()


# =====================================
# PERFORMANCE RESULT
# =====================================


def performance_result(
    start_time,
    label="Operation",
):

    end_time = datetime.now()

    delta = end_time - start_time

    print(f"""
⚡ PERFORMANCE

LABEL:
{label}

DURATION:
{delta.total_seconds()}s
""")
