# =====================================
# KEREMOS TASK TIME ENGINE TEST
# =====================================

from datetime import datetime
from datetime import timedelta

# =====================================
# TASK MODEL
# =====================================

tasks = [
    {
        "id": 1,
        "text": "Backend Refactor",
        "completed": False,
        "dueDate": "2026-05-24",
        "dueTime": "14:00",
        "priority": "high",
        "order": 1,
    },
    {
        "id": 2,
        "text": "Timeline Engine",
        "completed": False,
        "dueDate": "2026-05-24",
        "dueTime": "16:00",
        "priority": "medium",
        "order": 2,
    },
    {
        "id": 3,
        "text": "AI Worker",
        "completed": True,
        "dueDate": "2026-05-24",
        "dueTime": "18:00",
        "priority": "high",
        "order": 3,
    },
]

# =====================================
# SIMULATED TIME
# =====================================

simulated_now = datetime.strptime("2026-05-24 17:30", "%Y-%m-%d %H:%M")

print("""
=====================================
SIMULATION START
=====================================
""")

print("Simulated Time:")
print(simulated_now)

# =====================================
# AUTO MOVE ENGINE
# =====================================

for task in tasks:

    # =====================================
    # TASK DATETIME
    # =====================================

    task_datetime = datetime.strptime(
        f"{task['dueDate']} {task['dueTime']}", "%Y-%m-%d %H:%M"
    )

    # =====================================
    # CHECK EXPIRED
    # =====================================

    if simulated_now > task_datetime and not task["completed"]:

        print(f"""
⚠️ TASK EXPIRED:

{task["text"]}
""")

        # =====================================
        # MOVE NEXT DAY
        # =====================================

        new_datetime = task_datetime + timedelta(days=1)

        task["dueDate"] = new_datetime.strftime("%Y-%m-%d")

        task["dueTime"] = new_datetime.strftime("%H:%M")

        print(f"""
✅ MOVED TO NEXT DAY

NEW DATE:
{task["dueDate"]}

NEW TIME:
{task["dueTime"]}
""")

# =====================================
# FINAL TASKS
# =====================================

print("""
=====================================
FINAL TASKS
=====================================
""")

for task in tasks:

    print(f"""
TASK:
{task["text"]}

DATE:
{task["dueDate"]}

TIME:
{task["dueTime"]}

COMPLETED:
{task["completed"]}

PRIORITY:
{task["priority"]}
""")
