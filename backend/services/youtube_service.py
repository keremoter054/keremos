import isodate
import requests
import traceback

from urllib.parse import (
    urlparse,
    parse_qs,
)

from config.settings import (
    YOUTUBE_API_KEY,
)

from config.constants import (
    YOUTUBE_BASE_URL,
)

# =====================================
# EXTRACT PLAYLIST ID
# =====================================


def extract_playlist_id(
    url,
):

    try:

        parsed = urlparse(url)

        query = parse_qs(parsed.query)

        playlist_id = query.get("list", [None])[0]

        return playlist_id

    except Exception:

        traceback.print_exc()

        return None


# =====================================
# EXTRACT VIDEO ID
# =====================================


def extract_video_id(
    url,
):

    try:

        parsed = urlparse(url)

        query = parse_qs(parsed.query)

        video_id = query.get("v", [None])[0]

        return video_id

    except Exception:

        traceback.print_exc()

        return None


# =====================================
# GET PLAYLIST METADATA
# =====================================


def get_playlist_metadata(
    playlist_id,
):

    try:

        url = f"{YOUTUBE_BASE_URL}/playlists"

        params = {
            "part": "snippet,contentDetails",
            "id": playlist_id,
            "key": YOUTUBE_API_KEY,
        }

        response = requests.get(
            url,
            params=params,
            timeout=30,
        )

        data = response.json()

        items = data.get("items", [])

        if not items:

            return None

        item = items[0]

        snippet = item["snippet"]

        content = item["contentDetails"]

        return {
            "title": snippet.get("title"),
            "channel_name": snippet.get("channelTitle"),
            "thumbnail_url": snippet.get(
                "thumbnails",
                {},
            )
            .get(
                "high",
                {},
            )
            .get("url"),
            "video_count": content.get(
                "itemCount",
                0,
            ),
        }

    except Exception:

        traceback.print_exc()

        return None


# =====================================
# GET PLAYLIST VIDEOS
# =====================================


def get_playlist_videos(
    playlist_id,
):

    videos = []

    next_page_token = None

    try:

        while True:

            url = f"{YOUTUBE_BASE_URL}/playlistItems"

            params = {
                "part": "snippet,contentDetails",
                "playlistId": playlist_id,
                "maxResults": 50,
                "pageToken": next_page_token,
                "key": YOUTUBE_API_KEY,
            }

            response = requests.get(
                url,
                params=params,
                timeout=30,
            )

            data = response.json()

            items = data.get("items", [])

            for item in items:

                snippet = item["snippet"]

                content = item["contentDetails"]

                video_id = content.get("videoId")

                title = snippet.get("title")

                videos.append(
                    {
                        "youtube_video_id": video_id,
                        "title": title,
                    }
                )

            next_page_token = data.get("nextPageToken")

            if not next_page_token:

                break

        print(f"""
✅ PLAYLIST VIDEOS FETCHED

COUNT:
{len(videos)}
""")

        return videos

    except Exception:

        traceback.print_exc()

        return []


# =====================================
# GET VIDEO DETAILS
# =====================================


def get_video_details(
    video_ids,
):

    try:

        results = []

        # =====================================
        # CHUNK 50
        # =====================================

        for i in range(
            0,
            len(video_ids),
            50,
        ):

            chunk = video_ids[i : i + 50]

            ids = ",".join(chunk)

            url = f"{YOUTUBE_BASE_URL}/videos"

            params = {
                "part": "snippet,contentDetails",
                "id": ids,
                "key": YOUTUBE_API_KEY,
            }

            response = requests.get(
                url,
                params=params,
                timeout=30,
            )

            data = response.json()

            for item in data.get(
                "items",
                [],
            ):

                snippet = item["snippet"]

                content = item["contentDetails"]

                duration_iso = content.get(
                    "duration",
                    "PT0S",
                )

                duration_seconds = int(
                    isodate.parse_duration(duration_iso).total_seconds()
                )

                results.append(
                    {
                        "youtube_video_id": item["id"],
                        "title": snippet.get("title"),
                        "channel_name": snippet.get("channelTitle"),
                        "thumbnail_url": snippet.get(
                            "thumbnails",
                            {},
                        )
                        .get(
                            "high",
                            {},
                        )
                        .get("url"),
                        "duration_seconds": duration_seconds,
                    }
                )

        print(f"""
✅ VIDEO DETAILS FETCHED

COUNT:
{len(results)}
""")

        return results

    except Exception:

        traceback.print_exc()

        return []

    except Exception:

        traceback.print_exc()

        return []


# =====================================
# FORMAT DURATION
# =====================================


def format_duration(
    seconds,
):

    try:

        seconds = int(seconds)

        hours = seconds // 3600

        minutes = (seconds % 3600) // 60

        secs = seconds % 60

        if hours > 0:

            return f"{hours}:" f"{minutes:02}:" f"{secs:02}"

        return f"{minutes}:" f"{secs:02}"

    except Exception:

        return "0:00"


# =====================================
# PLAYLIST STATS
# =====================================


def calculate_playlist_stats(
    videos,
):

    total_videos = len(videos)

    total_seconds = sum(
        video.get(
            "duration_seconds",
            0,
        )
        for video in videos
    )

    total_hours = round(
        total_seconds / 3600,
        2,
    )

    return {
        "total_videos": total_videos,
        "total_seconds": total_seconds,
        "total_hours": total_hours,
    }
