# 🤖 Local Llama Chatbot

A private, local AI chatbot built with Streamlit and Ollama. No data ever leaves your computer.

## Features
- 💬 Multi-turn conversation with memory
- ⚡ Streaming responses (typing effect)
- 🔒 100% local — no API keys, no internet required
- 🦙 Powered by Llama 3.2

## Requirements
- Python 3.8+
- [Ollama](https://ollama.com) installed and running

## Setup

**1. Clone the repository**
```bash
git clone https://github.com/YOUR_USERNAME/local-llama-chatbot.git
cd local-llama-chatbot
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Pull the Llama model**
```bash
ollama pull llama3.2
```

**4. Run the app**
```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`

## How it works
- `streamlit` powers the chat UI
- `ollama` runs the Llama 3.2 model locally on your machine
- `st.session_state` stores the conversation history so the model remembers context
