# 🤖 Chandu AI — Personal AI Assistant

> A full-stack AI chatbot built from scratch — from a Python terminal script to a complete web application with memory, voice, and sentiment intelligence.

![Python](https://img.shields.io/badge/Python-3.11-blue?style=flat-square&logo=python)
![Flask](https://img.shields.io/badge/Flask-3.1-black?style=flat-square&logo=flask)
![Groq](https://img.shields.io/badge/Groq-LLaMA_3.1-orange?style=flat-square)
![JavaScript](https://img.shields.io/badge/JavaScript-ES6-yellow?style=flat-square&logo=javascript)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)

---

## ✨ What is Chandu?

Chandu is a personal AI assistant that remembers who you are, understands how you feel, and responds like a real conversation — not a generic chatbot.

It started as a 50-line Python terminal script. It evolved into a full-stack web application with a custom UI, persistent memory, voice input, and multiple chat sessions.

---

## ✨ Live Features

| Feature | Description |
|---------|-------------|
| 🧠 AI Conversation | Powered by LLaMA 3.1 8B via Groq API — fast, free, smart |
| 💾 Memory System | Remembers your name, location, interests and mood automatically |
| 🎭 Sentiment Detection | Tags every message as positive, negative or neutral in real time |
| 🌙 Dark UI | Clean dark sidebar with live memory panel and typing indicator |

## 🔨 In Progress

| Feature | Status |
|---------|--------|
| 🎤 Voice Input | Coming soon — Web Speech Recognition API |
| 💬 Multiple Sessions | Coming soon — localStorage sessions |
| 🔄 Chat History | Coming soon — persist across refresh |

---

## 🖥️ Screenshots

> Chandu replying with sentiment detection and memory panel live
[Add a screenshot here — drag and drop an image into GitHub]

---

## 🏗️ How It Works
User types or speaks
↓
script.js captures input
↓
POST /chat → app.py (Flask)
↓
Groq API → LLaMA 3.1 8B
↓
Reply streams back to browser
↓
Bubble renders with sentiment tag

- Every message includes **full conversation history** so Chandu remembers context across the whole chat
- **Memory is auto-extracted** — "my name is Raj" → sidebar updates instantly
- **Sentiment** is detected client-side using keyword matching, zero extra API calls
- **Sessions** stored in localStorage — no database needed for persistence

---

## 🗂️ Project Structure
chandu-ai/
│
├── app.py              # Flask backend — /chat endpoint + static file serving
├── chat.py             # Original v1 terminal chatbot (the foundation)
│
├── index.html          # UI structure — sidebar, chat area, input bar
├── style.css           # Full styling — dark theme, bubbles, animations
├── script.js           # Frontend brain — messages, voice, sessions, memory
│
├── responses.json      # Intent patterns for rule-based matching
├── memory.json         # Persistent user memory store
│
├── .env                # API keys (never committed)
├── .gitignore          # Ignores node_modules, .env, pycache
└── README.md           # You are here

---

## ⚙️ Getting Started

### Prerequisites
- Python 3.8+
- A free Groq API key from [console.groq.com](https://console.groq.com)
- Chrome browser (for voice input)

### Installation

**1. Clone the repository**
```bash
git clone https://github.com/coder28-cloud/chandu-ai.git
cd chandu-ai
```

**2. Install Python dependencies**
```bash
pip install flask flask-cors requests python-dotenv
```

**3. Create your `.env` file**
```bash
# create a file called .env in the root folder
GROQ_API_KEY=your_groq_api_key_here
```

**4. Run the server**
```bash
python app.py
```

**5. Open in browser**
http://127.0.0.1:3000

---

## 🧪 Try These Commands

Once Chandu is running, try saying:
"My name is [your name]"        → Chandu remembers you
"I live in Delhi"               → Stores your location
"I love coding"                 → Saves your interests
"I am feeling sad today"        → Detects negative sentiment
"What is machine learning?"     → Full AI response
"What's my name?"               → Recalls from memory

---

## 🛠️ Tech Stack
Backend      →  Python 3.11, Flask 3.1, flask-cors
AI Model     →  LLaMA 3.1 8B Instant via Groq API
Frontend     →  Vanilla HTML5, CSS3, JavaScript ES6
Voice        →  Web Speech Recognition API (Chrome built-in)
Storage      →  localStorage (browser-native, no DB needed)
Environment  →  python-dotenv
Version ctrl →  Git + GitHub

---

## 📈 Project Evolution

This project went through 3 clear stages:

**Stage 1 — Terminal chatbot (`chat.py`)**
- Pure Python, runs in terminal
- `difflib` for intent matching
- `responses.json` for pre-written replies
- Basic memory with `memory.json`
- Groq API for AI fallback

**Stage 2 — Web backend (`app.py`)**
- Rewrote brain as a Flask REST API
- Full conversation history passed to Groq
- Memory injected as context on every request
- Serves static files to browser

**Stage 3 — Full web UI**
- Custom dark chat interface built from scratch
- Real-time sentiment detection
- Voice input via Speech Recognition API
- Multiple sessions with localStorage persistence
- Live memory panel in sidebar

---

## 🔮 Upcoming Features

- [ ] SQLite database for long-term memory
- [ ] Whisper API for accurate voice transcription
- [ ] ElevenLabs TTS — Chandu speaks back
- [ ] Web search tool — real-time information
- [ ] Emotion-aware responses using voice tone analysis
- [ ] Deploy to Railway — publicly accessible URL

---

## 💡 What I Learned

Building this project taught me:

- How to build and connect a **Python Flask REST API** to a browser frontend
- How **LLM conversation history** works — role/content message arrays
- How to use the **Web Speech Recognition API** for zero-dependency voice input
- **CSS Flexbox** layout for building real application UIs
- **localStorage** for client-side persistence without a database
- How to manage **API keys securely** with .env and .gitignore
- The full **Git workflow** — init, commit, push, force push, merge conflicts
- Debugging real errors — wrong node-fetch version, CORS issues, Flask static files

---

## 👨‍💻 Author

**coder28-cloud**

Started this project knowing only Python. Built the AI brain in chat.py first,
then learned enough HTML, CSS and JavaScript to bring it to life as a web app.
Currently deepening my frontend skills.

> "Don't just learn to code. Build something."

## 📄 License

MIT License — free to use, modify and share.

---

⭐ If you found this useful, consider giving it a star!