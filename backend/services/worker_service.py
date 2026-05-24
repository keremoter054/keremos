import threading
import traceback
import queue
import time

from workers.video_worker import (
    process_video_job,
)

# =====================================
# GLOBAL WORKER STATE
# =====================================

job_queue = queue.Queue()

worker_thread = None

worker_running = False

worker_lock = threading.Lock()

processed_jobs = 0

failed_jobs = 0

# =====================================
# WORKER LOOP
# =====================================


def worker_loop():

    global worker_running
    global processed_jobs
    global failed_jobs

    print("""
🚀 WORKER STARTED
""")

    while worker_running:

        try:

            # =====================================
            # GET JOB
            # =====================================

            job = job_queue.get(timeout=1)

            print(f"""
🎯 PROCESSING JOB

JOB:
{job}
""")

            # =====================================
            # PROCESS
            # =====================================

            process_video_job(job)

            processed_jobs += 1

            job_queue.task_done()

        except queue.Empty:

            continue

        except Exception as e:

            failed_jobs += 1

            print(f"""
❌ WORKER ERROR

ERROR:
{e}
""")

            traceback.print_exc()

    print("""
🛑 WORKER STOPPED
""")


# =====================================
# START WORKER
# =====================================


def start_worker_service():

    global worker_thread
    global worker_running

    with worker_lock:

        if worker_running:

            return {"status": "already_running"}

        worker_running = True

        worker_thread = threading.Thread(
            target=worker_loop,
            daemon=True,
        )

        worker_thread.start()

    return {"status": "started"}


# =====================================
# STOP WORKER
# =====================================


def stop_worker_service():

    global worker_running

    with worker_lock:

        worker_running = False

    return {"status": "stopped"}


# =====================================
# RESTART WORKER
# =====================================


def restart_worker_service():

    stop_worker_service()

    time.sleep(1)

    start_worker_service()

    return {"status": "restarted"}


# =====================================
# GET WORKER STATUS
# =====================================


def get_worker_status_service():

    return {
        "worker_running": worker_running,
        "processed_jobs": processed_jobs,
        "failed_jobs": failed_jobs,
        "queue_size": job_queue.qsize(),
        "thread_alive": (worker_thread.is_alive() if worker_thread else False),
    }


# =====================================
# GET QUEUE STATUS
# =====================================


def get_queue_status_service():

    return {
        "queue_size": job_queue.qsize(),
        "processed_jobs": processed_jobs,
        "failed_jobs": failed_jobs,
    }


# =====================================
# CLEAR QUEUE
# =====================================


def clear_queue_service():

    cleared = 0

    while not job_queue.empty():

        try:

            job_queue.get_nowait()

            job_queue.task_done()

            cleared += 1

        except Exception:

            break

    return {
        "status": "ok",
        "cleared": cleared,
    }


# =====================================
# ADD JOB
# =====================================


def add_job(
    job_data,
):

    job_queue.put(job_data)

    print(f"""
➕ JOB ADDED

JOB:
{job_data}
""")

    return {
        "status": "queued",
        "queue_size": job_queue.qsize(),
    }
