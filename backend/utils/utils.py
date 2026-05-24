# 🔥 URL PARSE
from urllib.parse import (
    urlparse,
    parse_qs,
)

# 🔥 HTTP
import requests

# 🔥 ISO DURATION
import isodate


# 🔥 PLAYLIST ID EXTRACT
def extract_playlist_id(url: str):

    try:

        parsed = urlparse(url)

        query = parse_qs(parsed.query)

        if "list" in query:

            return query["list"][0]

        return None

    except Exception as e:

        print("❌ PLAYLIST ID HATA:", e)

        return None


# 🔥 PLAYLIST METADATA
def get_playlist_metadata(
    api_key: str,
    playlist_id: str,
):

    url = "https://www.googleapis.com" "/youtube/v3/playlists"

    params = {
        "part": "snippet,contentDetails",
        "id": playlist_id,
        "key": api_key,
    }

    try:

        response = requests.get(
            url,
            params=params,
            timeout=15,
        )

        if response.status_code != 200:

            print("❌ PLAYLIST METADATA API:", response.text)

            return {
                "title": "Unknown Playlist",
                "channel": None,
                "thumbnail": None,
                "video_count": 0,
            }

        data = response.json()

        items = data.get("items", [])

        if not items:

            return {
                "title": "Unknown Playlist",
                "channel": None,
                "thumbnail": None,
                "video_count": 0,
            }

        item = items[0]

        snippet = item.get("snippet", {})

        content = item.get("contentDetails", {})

        thumbnails = snippet.get("thumbnails", {})

        return {
            "title": snippet.get(
                "title",
                "Unknown Playlist",
            ),
            "channel": snippet.get("channelTitle"),
            "thumbnail": thumbnails.get("high", {}).get("url"),
            "video_count": content.get(
                "itemCount",
                0,
            ),
        }

    except Exception as e:

        print("❌ PLAYLIST METADATA HATA:", e)

        return {
            "title": "Unknown Playlist",
            "channel": None,
            "thumbnail": None,
            "video_count": 0,
        }


# 🔥 VIDEO DURATIONS
def get_videos_duration_batch(
    video_ids: list,
    api_key: str,
):

    url = "https://www.googleapis.com" "/youtube/v3/videos"

    durations = {}

    print("🎬 TOPLAM VIDEO:", len(video_ids))

    try:

        for i in range(
            0,
            len(video_ids),
            50,
        ):

            chunk = video_ids[i : i + 50]

            print(f"🔥 BATCH: {len(chunk)}")

            params = {
                "part": "contentDetails",
                "id": ",".join(chunk),
                "key": api_key,
            }

            response = requests.get(
                url,
                params=params,
                timeout=15,
            )

            if response.status_code != 200:

                print("❌ DURATION API:", response.text)

                continue

            data = response.json()

            items = data.get("items", [])

            print("✅ API VIDEO:", len(items))

            for item in items:

                try:

                    vid = item["id"]

                    duration_iso = item["contentDetails"]["duration"]

                    duration_seconds = int(
                        isodate.parse_duration(duration_iso).total_seconds()
                    )

                    durations[vid] = duration_seconds

                except Exception as e:

                    print("❌ DURATION PARSE:", e)

    except Exception as e:

        print("❌ BATCH HATA:", e)

    return durations


# 🔥 PLAYLIST VIDEOS
def get_playlist_videos(
    playlist_id: str,
    api_key: str,
):

    url = "https://www.googleapis.com" "/youtube/v3/playlistItems"

    videos = []

    seen = set()

    next_page_token = None

    try:

        while True:

            params = {
                "part": "snippet",
                "playlistId": playlist_id,
                "maxResults": 50,
                "key": api_key,
            }

            if next_page_token:

                params["pageToken"] = next_page_token

            response = requests.get(
                url,
                params=params,
                timeout=15,
            )

            if response.status_code != 200:

                print("❌ PLAYLIST VIDEO API:", response.text)

                break

            data = response.json()

            items = data.get("items", [])

            print("📄 PAGE VIDEO:", len(items))

            for item in items:

                try:

                    snippet = item.get("snippet", {})

                    resource = snippet.get("resourceId", {})

                    video_id = resource.get("videoId")

                    title = snippet.get(
                        "title",
                        "Unknown Video",
                    )

                    # 🔥 private/deleted
                    if not video_id:
                        continue

                    # 🔥 duplicate
                    if video_id in seen:
                        continue

                    seen.add(video_id)

                    videos.append(
                        {
                            "video_id": video_id,
                            "title": title,
                        }
                    )

                except Exception as e:

                    print("❌ VIDEO PARSE:", e)

            next_page_token = data.get("nextPageToken")

            if not next_page_token:
                break

    except Exception as e:

        print("❌ PLAYLIST LOOP HATA:", e)

    print("🔥 TOPLAM VIDEO:", len(videos))

    return videos
