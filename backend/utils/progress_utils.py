# =====================================
# CALCULATE PROGRESS
# =====================================


def calculate_progress(
    completed,
    total,
):

    if total <= 0:

        return 0

    return round(
        (completed / total) * 100,
        1,
    )


# =====================================
# CALCULATE HOURS
# =====================================


def seconds_to_hours(
    seconds,
):

    return round(
        seconds / 3600,
        2,
    )


# =====================================
# CALCULATE REMAINING
# =====================================


def calculate_remaining(
    total,
    completed,
):

    remaining = total - completed

    if remaining < 0:

        return 0

    return remaining


# =====================================
# ESTIMATED DAYS
# =====================================


def estimate_days(
    remaining_tasks,
    daily_capacity=5,
):

    if daily_capacity <= 0:

        return 0

    return round(
        remaining_tasks / daily_capacity,
        1,
    )


# =====================================
# PLAYLIST PROGRESS
# =====================================


def calculate_playlist_progress(
    total_seconds,
    watched_seconds,
):

    total_hours = seconds_to_hours(total_seconds)

    watched_hours = seconds_to_hours(watched_seconds)

    progress = calculate_progress(
        watched_seconds,
        total_seconds,
    )

    return {
        "total_hours": total_hours,
        "watched_hours": watched_hours,
        "progress": progress,
    }


# =====================================
# GOAL PROGRESS
# =====================================


def calculate_goal_progress(
    requirements,
):

    total = len(requirements)

    completed = len([r for r in requirements if r.get("completed")])

    progress = calculate_progress(
        completed,
        total,
    )

    return {
        "total": total,
        "completed": completed,
        "progress": progress,
    }


# =====================================
# PRODUCTIVITY SCORE
# =====================================


def calculate_productivity_score(
    average_progress,
    consistency=1,
):

    score = average_progress * consistency

    if score > 100:

        score = 100

    return round(
        score,
        1,
    )


# =====================================
# VIDEO COMPLETION RATE
# =====================================


def calculate_completion_rate(
    completed_videos,
    total_videos,
):

    return calculate_progress(
        completed_videos,
        total_videos,
    )


# =====================================
# GLOBAL SYSTEM PROGRESS
# =====================================


def calculate_global_progress(
    sections,
):

    if not sections:

        return 0

    total = sum(sections)

    return round(
        total / len(sections),
        1,
    )
