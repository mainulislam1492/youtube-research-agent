from googleapiclient.discovery import build
import isodate

from src.utils import get_env


def search_videos(topic):

    youtube = build(
        "youtube",
        "v3",
        developerKey=get_env(
            "YOUTUBE_API_KEY"
        )
    )

    res = youtube.search().list(
        q=topic,
        part="snippet",
        maxResults=5,
        type="video"
    ).execute()

    videos=[]

    for item in res["items"]:

        vid=item["id"]["videoId"]

        detail=youtube.videos().list(
            part="contentDetails",
            id=vid
        ).execute()

        duration=isodate.parse_duration(
            detail["items"][0]
            ["contentDetails"]
            ["duration"]
        )

        videos.append({

            "id":vid,

            "title":
            item["snippet"]["title"],

            "channel":
            item["snippet"]
            ["channelTitle"],

            "url":
            f"https://youtube.com/watch?v={vid}",

            "published":
            item["snippet"]
            ["publishedAt"],

            "duration":
            str(duration)

        })

    return videos