import threading
import time

# =====================================
# GLOBAL STATE
# =====================================

worker_running = False

worker_thread = None

# =====================================
# VIDEO WORKER LOOP
# =====================================


def worker_loop():

    global worker_running

    print("""
🚀 VIDEO WORKER STARTED
""")

    while worker_running:

        try:

            # =====================================
            # WORKER TICK
            # =====================================

            time.sleep(1)

        except Exception as e:

            print(f"""
❌ WORKER ERROR

{e}
""")


# =====================================
# START WORKER
# =====================================


def start_video_worker():

    global worker_running
    global worker_thread

    if worker_running:

        print("""
⚠️ WORKER ALREADY RUNNING
""")

        return

    worker_running = True

    worker_thread = threading.Thread(
        target=worker_loop,
        daemon=True,
    )

    worker_thread.start()

    print("""
✅ VIDEO WORKER INITIALIZED
""")


# =====================================
# STOP WORKER
# =====================================


def stop_video_worker():

    global worker_running

    worker_running = False

    print("""
🛑 VIDEO WORKER STOPPED
""")


# =====================================
# WORKER STATUS
# =====================================


def get_worker_status():

    return {
        "running": worker_running,
    }


# =====================================
# PROCESS VIDEO JOB
# =====================================


def process_video_job(
    job,
):

    print(f"""
🎬 PROCESSING VIDEO JOB

JOB:
{job}
""")

    return {
        "status": "completed",
    }
