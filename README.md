# 🎥 YouTube Research AI Agent

**Author:** Mainul Islam Mahim

An AI-powered research assistant that automatically searches YouTube, extracts video transcripts, summarizes content using an LLM, and generates structured study notes.

The system also integrates with a Telegram bot to deliver results instantly as a chatbot.

---

## 🚀 Features

- 🔍 YouTube video search using YouTube Data API v3  
- 🎬 Automatic transcript extraction from videos  
- 🧠 AI-powered summarization using Groq LLM  
- 📚 Structured study notes generation  
- 📩 Telegram bot integration for real-time interaction  
- ⚙️ Modular and scalable architecture  

---

## 🧠 How It Works

```text
User enters a topic
        ↓
YouTube API searches relevant videos
        ↓
Transcript is extracted from each video
        ↓
AI (Groq LLM) summarizes content
        ↓
Notes are generated in structured format
        ↓
Result is sent via Telegram and saved as a file
```

---

## 🏗️ Project Structure

```text
youtube-research-agent/
│
├── main.py
├── bot.py
├── requirements.txt
├── .env
│
├── src/
│   ├── youtube_search.py
│   ├── transcript.py
│   ├── summarizer.py
│   ├── notes_generator.py
│   └── utils.py
│
├── output/
│   └── notes.md
│
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/mainulislam1492/youtube-research-agent.git
cd youtube-research-agent
```

---

### 2. Create virtual environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
source venv/bin/activate  # Mac/Linux
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Create `.env` file

```env
YOUTUBE_API_KEY=your_youtube_api_key
GROQ_API_KEY=your_groq_api_key
TELEGRAM_BOT_TOKEN=your_telegram_bot_token
```

---

### 5. Run Telegram Bot

```bash
python bot.py
```

---

## 📜 License

This project is for educational purposes.

---

## 👨‍💻 Author

**Mainul Islam Mahim**
