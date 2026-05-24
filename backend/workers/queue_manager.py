import queue
import threading

# =====================================
# GLOBAL QUEUE
# =====================================

job_queue = queue.Queue()

queue_lock = threading.Lock()

queue_set = set()

# =====================================
# ADD JOB
# =====================================


def add_job(
    job_data,
):

    with queue_lock:

        job_key = build_job_key(job_data)

        # =====================================
        # DUPLICATE CHECK
        # =====================================

        if job_key in queue_set:

            return {
                "status": "duplicate",
                "job": job_key,
            }

        # =====================================
        # ADD
        # =====================================

        job_queue.put(job_data)

        queue_set.add(job_key)

        print(f"""
➕ JOB ADDED

JOB:
{job_key}
""")

        return {
            "status": "queued",
            "queue_size": job_queue.qsize(),
        }


# =====================================
# GET JOB
# =====================================


def get_job(
    timeout=1,
):

    try:

        job = job_queue.get(timeout=timeout)

        return job

    except queue.Empty:

        return None


# =====================================
# COMPLETE JOB
# =====================================


def complete_job(
    job_data,
):

    with queue_lock:

        job_key = build_job_key(job_data)

        if job_key in queue_set:

            queue_set.remove(job_key)

        job_queue.task_done()

        print(f"""
✅ JOB COMPLETED

JOB:
{job_key}
""")


# =====================================
# FAIL JOB
# =====================================


def fail_job(
    job_data,
):

    with queue_lock:

        job_key = build_job_key(job_data)

        if job_key in queue_set:

            queue_set.remove(job_key)

        job_queue.task_done()

        print(f"""
❌ JOB FAILED

JOB:
{job_key}
""")


# =====================================
# CLEAR QUEUE
# =====================================


def clear_queue():

    cleared = 0

    with queue_lock:

        while not job_queue.empty():

            try:

                job_queue.get_nowait()

                job_queue.task_done()

                cleared += 1

            except Exception:

                break

        queue_set.clear()

    return {
        "status": "ok",
        "cleared": cleared,
    }


# =====================================
# GET QUEUE STATUS
# =====================================


def get_queue_status():

    return {
        "queue_size": job_queue.qsize(),
        "unique_jobs": len(queue_set),
        "jobs": list(queue_set),
    }


# =====================================
# BUILD JOB KEY
# =====================================


def build_job_key(
    job_data,
):

    video_id = job_data.get(
        "video_id",
        "unknown",
    )

    youtube_video_id = job_data.get(
        "youtube_video_id",
        "unknown",
    )

    return f"{video_id}_" f"{youtube_video_id}"


# =====================================
# QUEUE EMPTY
# =====================================


def is_queue_empty():

    return job_queue.empty()


# =====================================
# QUEUE SIZE
# =====================================


def queue_size():

    return job_queue.qsize()
