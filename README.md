# 🤖 ChatGpt LLM Q&A Chatbot With Live[Till Now Available On Internet] Data

**An intelligent conversational assistant powered by OpenAI’s "gpt-4o-mini" Model** — built with **Streamlit** and **LangGraph** to enable natural, context-aware interactions with persistent chat memory.  

Ask anything, get instant, context-rich responses — all within a clean, interactive web interface.  


## 🚀 Features

- Real-time conversation with the "gpt-4o-mini" model.
- Conversation history is displayed in the chat interface.
- Session memory to maintain context throughout the chat.
- The ability to ask questions and receive answers powered by OpenAI Generative AI.
- Configured to use the `dotenv` library for environment variable management.
- Real-time conversation with live data means till "now" data [Because, we are used here LangGraph's "Tool" Feature]



## 🧩 Tech Stack

| Component | Technology Used |
|------------|----------------|
| **Frontend** | Streamlit |
| **Backend** | Python 3.10+ |
| **LLM Engine** | ChatGpt via `"gpt-4o-mini"` |
| **Conversation Memory** | LangGraph |
| **Environment Management** | python-dotenv |


## Requirements
- Python 3.7+
- ChatGpt API Key for "gpt-4o-mini".
- Install the necessary Python packages listed below.

## Setup Instructions

1. Clone the Repository
```bash
git clone <repository-url>
cd CHATBOT-USING-LANGGRAPH-WITH-TOOLS
```

2. Create Virtual Environment
```bash
conda create -p env python=3.10 -y
```

3. Install Dependencies
```bash
pip install -r requirements.txt
```

4. Environment Configuration Create a .env file in the root directory:
```bash
OPENAI_API_KEY =your_api_key_here

LANGCHAIN_TRACING_V2=true
LANGCHAIN_ENDPOINT='https://api.smith.langchain.com'
LANGCHAIN_API_KEY='your_api_key_here'
LANGCHAIN_PROJECT='Your-Project-Name-Here'
