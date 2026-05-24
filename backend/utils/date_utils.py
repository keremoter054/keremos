from datetime import datetime
from datetime import timedelta

# =====================================
# TODAY DATE
# =====================================


def today_date():

    return datetime.now().strftime("%Y-%m-%d")


# =====================================
# NOW TIME
# =====================================


def now_time():

    return datetime.now().strftime("%H:%M")


# =====================================
# FORMAT DATE
# =====================================


def format_date(
    date_obj,
    format_string="%Y-%m-%d",
):

    return date_obj.strftime(format_string)


# =====================================
# PARSE DATE
# =====================================


def parse_date(
    date_string,
    format_string="%Y-%m-%d",
):

    return datetime.strptime(
        date_string,
        format_string,
    )


# =====================================
# ADD DAYS
# =====================================


def add_days(
    date_string,
    days,
):

    parsed = parse_date(date_string)

    new_date = parsed + timedelta(days=days)

    return format_date(new_date)


# =====================================
# DAYS BETWEEN
# =====================================


def days_between(
    start_date,
    end_date,
):

    start = parse_date(start_date)

    end = parse_date(end_date)

    delta = end - start

    return delta.days


# =====================================
# IS TODAY
# =====================================


def is_today(
    date_string,
):

    return date_string == today_date()


# =====================================
# WEEK START
# =====================================


def get_week_start():

    today = datetime.now()

    start = today - timedelta(days=today.weekday())

    return format_date(start)


# =====================================
# MONTH START
# =====================================


def get_month_start():

    today = datetime.now()

    start = today.replace(day=1)

    return format_date(start)


# =====================================
# DATE RANGE
# =====================================


def generate_date_range(
    start_date,
    total_days,
):

    dates = []

    for i in range(total_days):

        current = add_days(
            start_date,
            i,
        )

        dates.append(current)

    return dates


# =====================================
# ESTIMATED FINISH DATE
# =====================================


def estimate_finish_date(
    remaining_days,
):

    finish = datetime.now() + timedelta(days=remaining_days)

    return format_date(finish)


# =====================================
# DATE TO TIMESTAMP
# =====================================


def date_to_timestamp(
    date_string,
):

    parsed = parse_date(date_string)

    return int(parsed.timestamp())


# =====================================
# TIMESTAMP TO DATE
# =====================================


def timestamp_to_date(
    timestamp,
):

    return datetime.fromtimestamp(timestamp).strftime("%Y-%m-%d")
