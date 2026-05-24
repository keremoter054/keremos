import copy

# =====================================
# DEEP CLONE
# =====================================


def deep_clone(data):

    return copy.deepcopy(data)


# =====================================
# CLONE TASK
# =====================================


def clone_task(task):

    return {
        "task_name": task.get(
            "task_name",
            "",
        ),
        "progress": task.get(
            "progress",
            0,
        ),
        "completed": task.get(
            "completed",
            False,
        ),
        "start_time": task.get("start_time"),
        "end_time": task.get("end_time"),
        "pendingTasks": deep_clone(
            task.get(
                "pendingTasks",
                [],
            )
        ),
        "todayTasks": deep_clone(
            task.get(
                "todayTasks",
                [],
            )
        ),
        "developments": deep_clone(
            task.get(
                "developments",
                [],
            )
        ),
    }


# =====================================
# CLONE DAY
# =====================================


def clone_day(day):

    return {
        "date": day.get("date"),
        "overall_progress": day.get(
            "overall_progress",
            0,
        ),
        "tasks": [
            clone_task(task)
            for task in day.get(
                "tasks",
                [],
            )
        ],
    }


# =====================================
# COPY TASKS TO NEW DAY
# =====================================


def copy_tasks_to_day(
    source_day,
    target_date,
):

    cloned = clone_day(source_day)

    cloned["date"] = target_date

    return cloned


# =====================================
# RESET TASK COMPLETION
# =====================================


def reset_task_completion(
    task,
):

    task["completed"] = False

    task["progress"] = 0

    # =====================================
    # RESET TODOS
    # =====================================

    for key in [
        "pendingTasks",
        "todayTasks",
        "developments",
    ]:

        todos = task.get(
            key,
            [],
        )

        for todo in todos:

            todo["completed"] = False

    return task


# =====================================
# RESET DAY COMPLETION
# =====================================


def reset_day_completion(
    day,
):

    day["overall_progress"] = 0

    for task in day.get(
        "tasks",
        [],
    ):

        reset_task_completion(task)

    return day


# =====================================
# CLONE MULTIPLE DAYS
# =====================================


def clone_multiple_days(
    source_day,
    target_dates,
):

    days = []

    for target_date in target_dates:

        cloned = copy_tasks_to_day(
            source_day,
            target_date,
        )

        days.append(cloned)

    return days


# =====================================
# MERGE TASK LISTS
# =====================================


def merge_task_lists(
    tasks1,
    tasks2,
):

    merged = []

    seen = set()

    for task in tasks1 + tasks2:

        name = task.get(
            "task_name",
            "",
        )

        if name in seen:

            continue

        seen.add(name)

        merged.append(task)

    return merged


# =====================================
# DUPLICATE DAY
# =====================================


def duplicate_day_structure(
    day,
    new_date,
):

    duplicated = deep_clone(day)

    duplicated["date"] = new_date

    duplicated["overall_progress"] = 0

    for task in duplicated.get(
        "tasks",
        [],
    ):

        task["completed"] = False

        task["progress"] = 0

    return duplicated
