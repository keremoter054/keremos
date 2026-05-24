from urllib.parse import (
    urlparse,
    parse_qs,
)

import requests
import isodate

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

        if "list" in query:

            return query["list"][0]

        return None

    except Exception as e:

        print(f"""
❌ PLAYLIST ID ERROR

{e}
""")

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

        if "v" in query:

            return query["v"][0]

        return None

    except Exception as e:

        print(f"""
❌ VIDEO ID ERROR

{e}
""")

        return None


# =====================================
# GET PLAYLIST METADATA
# =====================================


def get_playlist_metadata(
    playlist_id,
):

    url = f"{YOUTUBE_BASE_URL}/playlists"

    params = {
        "part": "snippet,contentDetails",
        "id": playlist_id,
        "key": YOUTUBE_API_KEY,
    }

    try:

        response = requests.get(
            url,
            params=params,
            timeout=15,
        )

        if response.status_code != 200:

            print(f"""
❌ PLAYLIST METADATA API

{response.text}
""")

            return None

        data = response.json()

        items = data.get("items", [])

        if not items:

            return None

        item = items[0]

        snippet = item.get(
            "snippet",
            {},
        )

        content = item.get(
            "contentDetails",
            {},
        )

        thumbnails = snippet.get(
            "thumbnails",
            {},
        )

        return {
            "title": snippet.get(
                "title",
                "Unknown Playlist",
            ),
            "channel_name": snippet.get("channelTitle"),
            "thumbnail_url": thumbnails.get(
                "high",
                {},
            ).get("url"),
            "video_count": content.get(
                "itemCount",
                0,
            ),
        }

    except Exception as e:

        print(f"""
❌ PLAYLIST METADATA ERROR

{e}
""")

        return None


# =====================================
# GET PLAYLIST VIDEOS
# =====================================


def get_playlist_videos(
    playlist_id,
):

    url = f"{YOUTUBE_BASE_URL}/playlistItems"

    videos = []

    seen = set()

    next_page_token = None

    try:

        while True:

            params = {
                "part": "snippet",
                "playlistId": playlist_id,
                "maxResults": 50,
                "key": YOUTUBE_API_KEY,
            }

            if next_page_token:

                params["pageToken"] = next_page_token

            response = requests.get(
                url,
                params=params,
                timeout=15,
            )

            if response.status_code != 200:

                print(f"""
❌ PLAYLIST VIDEO API

{response.text}
""")

                break

            data = response.json()

            items = data.get("items", [])

            for item in items:

                try:

                    snippet = item.get(
                        "snippet",
                        {},
                    )

                    resource = snippet.get(
                        "resourceId",
                        {},
                    )

                    video_id = resource.get("videoId")

                    title = snippet.get(
                        "title",
                        "Unknown Video",
                    )

                    if not video_id:

                        continue

                    if video_id in seen:

                        continue

                    seen.add(video_id)

                    videos.append(
                        {
                            "youtube_video_id": video_id,
                            "title": title,
                        }
                    )

                except Exception as e:

                    print(f"""
❌ VIDEO PARSE ERROR

{e}
""")

            next_page_token = data.get("nextPageToken")

            if not next_page_token:

                break

        print(f"""
✅ PLAYLIST VIDEOS FETCHED

COUNT:
{len(videos)}
""")

        return videos

    except Exception as e:

        print(f"""
❌ PLAYLIST LOOP ERROR

{e}
""")

        return []


# =====================================
# GET VIDEO DETAILS
# =====================================


def get_video_details(
    video_ids,
):

    url = f"{YOUTUBE_BASE_URL}/videos"

    if isinstance(
        video_ids,
        list,
    ):

        video_ids = ",".join(video_ids)

    params = {
        "part": "snippet,contentDetails",
        "id": video_ids,
        "key": YOUTUBE_API_KEY,
    }

    try:

        response = requests.get(
            url,
            params=params,
            timeout=15,
        )

        if response.status_code != 200:

            print(f"""
❌ VIDEO DETAILS API

{response.text}
""")

            return []

        data = response.json()

        items = data.get("items", [])

        results = []

        for item in items:

            try:

                snippet = item.get(
                    "snippet",
                    {},
                )

                content = item.get(
                    "contentDetails",
                    {},
                )

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

            except Exception as e:

                print(f"""
❌ VIDEO DETAIL PARSE ERROR

{e}
""")

        return results

    except Exception as e:

        print(f"""
❌ VIDEO DETAILS ERROR

{e}
""")

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
# CALCULATE PLAYLIST STATS
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
