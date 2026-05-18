# 🤖 Local Llama Chatbot + Evaluation Pipeline

A private, local AI chatbot built with Streamlit and Ollama, with a built-in evaluation pipeline to measure response quality. No data ever leaves your computer.

## Features
- 💬 Multi-turn conversation with memory
- ⚡ Streaming responses (typing effect)
- 🔒 100% local — no API keys, no internet required
- 🦙 Powered by Llama 3.2
- 📊 Evaluation pipeline to measure answer quality

## Files
- `app.py` — The chatbot app
- `eval_pipeline.py` — Evaluation pipeline to test response quality

## Requirements
- Python 3.8+
- [Ollama](https://ollama.com) installed and running

## Setup

**1. Clone the repository**
```bash
git clone https://github.com/josephwelbeck/local-llama-chatbot.git
cd local-llama-chatbot
```

**2. Install chatbot dependencies**
```bash
pip install streamlit ollama
```

**3. Install evaluation dependencies**
```bash
pip install transformers sentence-transformers faiss-cpu pandas scikit-learn
```

**4. Pull the Llama model**
```bash
ollama pull llama3.2
```

**5. Run the chatbot**
```bash
streamlit run app.py
```

**6. Run the evaluation pipeline**
```bash
python eval_pipeline.py
```

## Evaluation Metrics
- **Similarity** — how close the AI's answer is to the expected answer
- **Context Score** — how well the retriever found the right information
- **Groundedness** — whether the AI used the retrieved context or made things up