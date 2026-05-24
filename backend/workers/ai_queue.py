import queue
import threading
import traceback
import time

from workers.queue_manager import (
    add_job,
    get_job,
    complete_job,
    fail_job,
    get_queue_status,
)

from workers.worker_state import (
    set_worker_started,
    set_worker_stopped,
    register_worker_thread,
    job_started,
    job_success,
    job_failed,
    get_worker_state,
)

from workers.video_worker import (
    process_video_job,
)

# =====================================
# AI QUEUE STATE
# =====================================

ai_worker_running = False

ai_worker_thread = None

ai_worker_lock = threading.Lock()

# =====================================
# START AI WORKER
# =====================================


def start_ai_worker():

    global ai_worker_running
    global ai_worker_thread

    with ai_worker_lock:

        if ai_worker_running:

            return {"status": "already_running"}

        ai_worker_running = True

        ai_worker_thread = threading.Thread(
            target=ai_worker_loop,
            daemon=True,
        )

        ai_worker_thread.start()

        register_worker_thread(ai_worker_thread)

        set_worker_started()

        print("""
🚀 AI WORKER STARTED
""")

        return {"status": "started"}


# =====================================
# STOP AI WORKER
# =====================================


def stop_ai_worker():

    global ai_worker_running

    with ai_worker_lock:

        ai_worker_running = False

        set_worker_stopped()

    print("""
🛑 AI WORKER STOPPED
""")

    return {"status": "stopped"}


# =====================================
# AI WORKER LOOP
# =====================================


def ai_worker_loop():

    global ai_worker_running

    print("""
🧠 AI WORKER LOOP ACTIVE
""")

    while ai_worker_running:

        try:

            # =====================================
            # GET JOB
            # =====================================

            job = get_job(timeout=1)

            if not job:

                time.sleep(0.3)

                continue

            print(f"""
🎯 AI JOB RECEIVED

JOB:
{job}
""")

            # =====================================
            # START JOB
            # =====================================

            job_started()

            # =====================================
            # PROCESS
            # =====================================

            process_video_job(job)

            # =====================================
            # COMPLETE
            # =====================================

            complete_job(job)

            job_success()

        except queue.Empty:

            continue

        except Exception as e:

            print(f"""
❌ AI WORKER ERROR

ERROR:
{e}
""")

            traceback.print_exc()

            try:

                fail_job(job)

            except Exception:

                traceback.print_exc()

            job_failed()

    print("""
🛑 AI LOOP CLOSED
""")


# =====================================
# ADD VIDEO JOB
# =====================================


def add_video_job(
    video_id,
    youtube_video_id,
):

    job = {
        "video_id": video_id,
        "youtube_video_id": youtube_video_id,
    }

    return add_job(job)


# =====================================
# AI QUEUE STATUS
# =====================================


def get_ai_queue_status():

    queue_status = get_queue_status()

    worker_status = get_worker_state()

    return {
        "ai_worker_running": ai_worker_running,
        "queue": queue_status,
        "worker": worker_status,
    }


# =====================================
# RESTART AI WORKER
# =====================================


def restart_ai_worker():

    stop_ai_worker()

    time.sleep(1)

    start_ai_worker()

    return {"status": "restarted"}


# =====================================
# AI WORKER HEALTH
# =====================================


def ai_worker_health():

    healthy = ai_worker_running and ai_worker_thread and ai_worker_thread.is_alive()

    return {
        "healthy": healthy,
        "running": ai_worker_running,
        "thread_alive": (ai_worker_thread.is_alive() if ai_worker_thread else False),
    }
