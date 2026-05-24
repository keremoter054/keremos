# =====================================
# KEREMOS LIVE TASK ENGINE
# =====================================

from datetime import datetime
from datetime import timedelta
import time

# =====================================
# DEBUG MODE
# =====================================

DEBUG_MODE = True

DEBUG_TIME = "2026-05-24 15:30"

# =====================================
# TASKS
# =====================================

tasks = [
    {
        "id": 1,
        "text": "Backend Refactor",
        "startTime": "14:00",
        "duration": 60,
        "completed": False,
        "priority": "high",
    },
    {
        "id": 2,
        "text": "AI Worker",
        "startTime": "15:00",
        "duration": 90,
        "completed": False,
        "priority": "medium",
    },
    {
        "id": 3,
        "text": "Timeline Engine",
        "startTime": "17:00",
        "duration": 120,
        "completed": False,
        "priority": "high",
    },
]

# =====================================
# GET CURRENT TIME
# =====================================


def get_current_time():

    if DEBUG_MODE:

        return datetime.strptime(DEBUG_TIME, "%Y-%m-%d %H:%M")

    return datetime.now()


# =====================================
# TASK STATUS
# =====================================


def calculate_task_status(task):

    now = get_current_time()

    # =====================================
    # TASK START
    # =====================================

    task_start = datetime.strptime(f"2026-05-24 {task['startTime']}", "%Y-%m-%d %H:%M")

    # =====================================
    # TASK END
    # =====================================

    task_end = task_start + timedelta(minutes=task["duration"])

    # =====================================
    # COMPLETED
    # =====================================

    if task["completed"]:

        return {
            "status": "COMPLETED",
            "late_minutes": 0,
        }

    # =====================================
    # WAITING
    # =====================================

    if now < task_start:

        return {
            "status": "WAITING",
            "late_minutes": 0,
        }

    # =====================================
    # ACTIVE
    # =====================================

    if now >= task_start and now <= task_end:

        return {
            "status": "ACTIVE",
            "late_minutes": 0,
        }

    # =====================================
    # LATE
    # =====================================

    late_minutes = int((now - task_end).total_seconds() / 60)

    return {
        "status": "LATE",
        "late_minutes": late_minutes,
    }


# =====================================
# AUTO SHIFT ENGINE
# =====================================


def auto_shift_tasks():

    print("""
=====================================
AUTO SHIFT ENGINE
=====================================
""")

    for task in tasks:

        result = calculate_task_status(task)

        # =====================================
        # LATE TASK
        # =====================================

        if result["status"] == "LATE" and not task["completed"]:

            print(f"""
⚠️ TASK LATE

TASK:
{task["text"]}

LATE:
{result["late_minutes"]} minutes
""")

            # =====================================
            # MOVE NEXT DAY
            # =====================================

            current_start = datetime.strptime(
                f"2026-05-24 {task['startTime']}", "%Y-%m-%d %H:%M"
            )

            new_start = current_start + timedelta(days=1)

            task["startTime"] = new_start.strftime("%H:%M")

            print(f"""
✅ TASK MOVED

NEW TIME:
{task["startTime"]}
""")


# =====================================
# RENDER TASKS
# =====================================


def render_tasks():

    now = get_current_time()

    print("""
=====================================
KEREMOS LIVE TASK ENGINE
=====================================
""")

    print(f"""
CURRENT TIME:
{now}
""")

    for task in tasks:

        result = calculate_task_status(task)

        # =====================================
        # ICON
        # =====================================

        icon = "⚪"

        if result["status"] == "ACTIVE":

            icon = "🟢"

        elif result["status"] == "LATE":

            icon = "🔴"

        elif result["status"] == "COMPLETED":

            icon = "✅"

        elif result["status"] == "WAITING":

            icon = "🟡"

        print(f"""
{icon} TASK:
{task["text"]}

START:
{task["startTime"]}

DURATION:
{task["duration"]} min

PRIORITY:
{task["priority"]}

STATUS:
{result["status"]}

LATE:
{result["late_minutes"]} min
""")


# =====================================
# MAIN LOOP
# =====================================

while True:

    render_tasks()

    auto_shift_tasks()

    print("""
=====================================
REFRESHING IN 5 SECONDS
=====================================
""")

    time.sleep(5)
