from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import TranscriptsDisabled, NoTranscriptFound


def get_transcript(video_id):
    try:
        transcript = YouTubeTranscriptApi().fetch(video_id)

        text = " ".join([chunk.text for chunk in transcript])

        return text

    except (TranscriptsDisabled, NoTranscriptFound):
        print(f"Transcript not available for {video_id}")
        return None

    except Exception as e:
        print(f"Unexpected error for {video_id}: {e}")
        return None