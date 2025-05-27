# 🧠 AI-Powered Study Assistant Chatbot

A full-stack chatbot built for educational platforms to assist students with study-related queries in English, powered by a fine-tuned GPT-2 model. This chatbot can be deployed locally or integrated into any website and supports real-time, multi-user interaction.

## 🚀 Features

* ✅ Natural Language Understanding using HuggingFace GPT-2
* ✅ FastAPI Backend with RESTful /chat endpoint
* ✅ Real-time User Interaction via Web UI (HTML, CSS, JS)
* ✅ User-friendly Chat Interface
* ✅ Supports Multi-user Communication
* ✅ Completely Free and Offline Deployable
* ✅ Easy to extend with new features/tasks (Bengali support, FAQ mode, voice input, etc.)

## 🛠️ Tech Stack

| Component           | Technology              |
|---------------------|--------------------------|
| Language Model      | GPT-2 (HuggingFace)     |
| Backend             | FastAPI, Uvicorn        |
| Frontend            | HTML, CSS, JavaScript   |
| Hosting (Local)     | Python http.server      |


## 📦 Installation & Usage (Local)

1. Clone the repo:

```bash
git clone https://github.com/Saibhossain/AI_ChatBotUsingGPT-2.git
cd study-assistant-chatbot
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run backend:
```bash
uvicorn main: app --reload
```

4. Run frontend:

```bash
cd frontend
python3 -m http.server 5500
```

5 Open http://localhost:5500 in browser.
