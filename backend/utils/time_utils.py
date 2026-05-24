from datetime import datetime
from datetime import timedelta

# =====================================
# CURRENT TIME
# =====================================


def current_time():

    return datetime.now()


# =====================================
# CURRENT TIMESTAMP
# =====================================


def current_timestamp():

    return int(datetime.now().timestamp())


# =====================================
# FORMAT TIME
# =====================================


def format_time(
    date_obj,
    format_string="%H:%M",
):

    return date_obj.strftime(format_string)


# =====================================
# PARSE TIME
# =====================================


def parse_time(
    time_string,
    format_string="%H:%M",
):

    return datetime.strptime(
        time_string,
        format_string,
    )


# =====================================
# SECONDS TO HMS
# =====================================


def seconds_to_hms(
    seconds,
):

    seconds = int(seconds)

    hours = seconds // 3600

    minutes = (seconds % 3600) // 60

    secs = seconds % 60

    return {
        "hours": hours,
        "minutes": minutes,
        "seconds": secs,
    }


# =====================================
# FORMAT DURATION
# =====================================


def format_duration(
    seconds,
):

    hms = seconds_to_hms(seconds)

    hours = hms["hours"]

    minutes = hms["minutes"]

    secs = hms["seconds"]

    if hours > 0:

        return f"{hours}:" f"{minutes:02}:" f"{secs:02}"

    return f"{minutes}:" f"{secs:02}"


# =====================================
# MINUTES TO SECONDS
# =====================================


def minutes_to_seconds(
    minutes,
):

    return int(minutes * 60)


# =====================================
# HOURS TO SECONDS
# =====================================


def hours_to_seconds(
    hours,
):

    return int(hours * 3600)


# =====================================
# ADD MINUTES
# =====================================


def add_minutes(
    time_string,
    minutes,
):

    parsed = parse_time(time_string)

    new_time = parsed + timedelta(minutes=minutes)

    return format_time(new_time)


# =====================================
# TIME DIFFERENCE
# =====================================


def time_difference_minutes(
    start_time,
    end_time,
):

    start = parse_time(start_time)

    end = parse_time(end_time)

    delta = end - start

    return int(delta.total_seconds() / 60)


# =====================================
# IS TIME BETWEEN
# =====================================


def is_time_between(
    current,
    start,
    end,
):

    current = parse_time(current)

    start = parse_time(start)

    end = parse_time(end)

    return start <= current <= end


# =====================================
# ESTIMATED FINISH TIME
# =====================================


def estimate_finish_time(
    start_time,
    duration_minutes,
):

    return add_minutes(
        start_time,
        duration_minutes,
    )


# =====================================
# TIMER TEXT
# =====================================


def timer_text(
    seconds,
):

    hms = seconds_to_hms(seconds)

    parts = []

    if hms["hours"] > 0:

        parts.append(f"{hms['hours']}h")

    if hms["minutes"] > 0:

        parts.append(f"{hms['minutes']}m")

    if hms["seconds"] > 0:

        parts.append(f"{hms['seconds']}s")

    return " ".join(parts)


# =====================================
# WORK SESSION BLOCK
# =====================================


def create_work_block(
    start_time,
    duration_minutes,
    title="Work Session",
):

    end_time = estimate_finish_time(
        start_time,
        duration_minutes,
    )

    return {
        "title": title,
        "start_time": start_time,
        "end_time": end_time,
        "duration_minutes": duration_minutes,
    }
