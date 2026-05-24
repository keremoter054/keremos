# =====================================
# START VIDEO ANALYSIS
# =====================================


def start_video_analysis_service(
    video_id,
):

    return {
        "status": "processing",
        "video_id": video_id,
    }


# =====================================
# VIDEO PROGRESS
# =====================================


def get_video_progress_service(
    video_id,
):

    return {
        "video_id": video_id,
        "status": "not_started",
        "progress": 0,
    }


# =====================================
# VIDEO RESULT
# =====================================


def get_video_result_service(
    video_id,
):

    return {
        "video_id": video_id,
        "summary": None,
        "notes": None,
        "analysis": None,
    }


# =====================================
# VIDEO TRANSCRIPT
# =====================================


def get_video_transcript_service(
    video_id,
):

    return {
        "video_id": video_id,
        "transcript": None,
    }


# =====================================
# STATUS SUMMARY
# =====================================


def get_video_status_summary_service():

    return {
        "processing": 0,
        "completed": 0,
        "failed": 0,
    }


# =====================================
# PLAYLIST VIDEOS
# =====================================


def get_playlist_videos(
    playlist_id,
):

    return []


# =====================================
# SAVE VIDEO PROGRESS
# =====================================


def save_video_progress(
    youtube_video_id,
    current_time,
):

    return {
        "status": "ok",
    }
