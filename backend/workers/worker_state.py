import threading
import time

# =====================================
# WORKER GLOBAL STATE
# =====================================

worker_running = False

worker_started_at = None

worker_last_job_at = None

worker_name = "KeremOS-Worker"

worker_version = "1.0.0"

worker_lock = threading.Lock()

# =====================================
# JOB STATS
# =====================================

processed_jobs = 0

failed_jobs = 0

active_jobs = 0

# =====================================
# THREAD INFO
# =====================================

worker_thread = None

worker_thread_id = None

# =====================================
# WORKER START
# =====================================


def set_worker_started():

    global worker_running
    global worker_started_at

    with worker_lock:

        worker_running = True

        worker_started_at = time.time()

    print("""
🚀 WORKER STATE STARTED
""")


# =====================================
# WORKER STOP
# =====================================


def set_worker_stopped():

    global worker_running

    with worker_lock:

        worker_running = False

    print("""
🛑 WORKER STATE STOPPED
""")


# =====================================
# JOB START
# =====================================


def job_started():

    global active_jobs
    global worker_last_job_at

    with worker_lock:

        active_jobs += 1

        worker_last_job_at = time.time()


# =====================================
# JOB SUCCESS
# =====================================


def job_success():

    global processed_jobs
    global active_jobs

    with worker_lock:

        processed_jobs += 1

        active_jobs -= 1

        if active_jobs < 0:

            active_jobs = 0


# =====================================
# JOB FAILED
# =====================================


def job_failed():

    global failed_jobs
    global active_jobs

    with worker_lock:

        failed_jobs += 1

        active_jobs -= 1

        if active_jobs < 0:

            active_jobs = 0


# =====================================
# REGISTER THREAD
# =====================================


def register_worker_thread(
    thread,
):

    global worker_thread
    global worker_thread_id

    worker_thread = thread

    worker_thread_id = thread.ident


# =====================================
# GET WORKER STATE
# =====================================


def get_worker_state():

    uptime_seconds = 0

    if worker_started_at:

        uptime_seconds = int(time.time() - worker_started_at)

    return {
        "worker_running": worker_running,
        "worker_name": worker_name,
        "worker_version": worker_version,
        "worker_started_at": worker_started_at,
        "worker_last_job_at": worker_last_job_at,
        "uptime_seconds": uptime_seconds,
        "processed_jobs": processed_jobs,
        "failed_jobs": failed_jobs,
        "active_jobs": active_jobs,
        "thread_alive": (worker_thread.is_alive() if worker_thread else False),
        "thread_id": worker_thread_id,
    }


# =====================================
# RESET WORKER STATS
# =====================================


def reset_worker_stats():

    global processed_jobs
    global failed_jobs
    global active_jobs

    with worker_lock:

        processed_jobs = 0

        failed_jobs = 0

        active_jobs = 0

    print("""
♻️ WORKER STATS RESET
""")


# =====================================
# WORKER HEALTH
# =====================================


def worker_health():

    state = get_worker_state()

    healthy = state["worker_running"] and state["thread_alive"]

    return {
        "healthy": healthy,
        "state": state,
    }
