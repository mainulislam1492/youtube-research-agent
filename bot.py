import asyncio
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters

from src.youtube_search import search_videos
from src.transcript import get_transcript
from src.summarizer import summarize
from src.notes_generator import generate
from src.utils import get_env


TOKEN = get_env("TELEGRAM_BOT_TOKEN")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Send me a topic 🚀")


async def handle(update: Update, context: ContextTypes.DEFAULT_TYPE):

    topic = update.message.text

    await update.message.reply_text("Searching YouTube...")

    videos = search_videos(topic)

    summaries = []

    for v in videos:

        await update.message.reply_text(f"Processing:\n{v['title']}")

        text = get_transcript(v["id"])

        if not text:
            continue

        summary = summarize(text)

        if summary:
            summaries.append(summary)

    await update.message.reply_text("Generating notes...")

    notes = generate(topic, summaries)

    path = "output/notes.md"

    with open(path, "w", encoding="utf-8") as f:
        f.write(notes)

    await update.message.reply_document(open(path, "rb"))


def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle))

    print("Bot running...")
    app.run_polling()


if __name__ == "__main__":
    main()