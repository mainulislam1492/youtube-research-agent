from rich import print

from src.youtube_search import search_videos
from src.transcript import get_transcript
from src.summarizer import summarize
from src.notes_generator import generate


topic = input("\nEnter topic: ")

print("\nSearching...")

videos = search_videos(topic)

summaries = []

for v in videos:

    print(f"Processing {v['title']}")

    text = get_transcript(v["id"])

    if not text:
        print("Skipping (no transcript)")
        continue

    s = summarize(text)

    if not s:
        print("Skipping (no summary)")
        continue

    summaries.append(s)

print("Generating...")

notes = generate(topic, summaries)

with open("output/notes.md", "w", encoding="utf8") as f:
    f.write(notes)

print("\nDone")
text = get_transcript(v["id"])

print("\nTRANSCRIPT SAMPLE:\n", text[:300] if text else "NO TRANSCRIPT")