# OpenChat 🤖

OpenChat is a simple, lightweight chat interface built with Streamlit that allows you to interact with local Large Language Models (LLMs) served by [Ollama](https://ollama.com/).

## 🚀 Features

- **Local Model Integration**: Seamlessly connect to your local Ollama server.
- **Model Selection**: Dynamically fetch and switch between all available models installed on your machine.
- **Streaming Responses**: Real-time, token-by-token response streaming for a native chat experience.
- **Chat History**: Maintains conversation state within the session.
- **Simple UI**: Clean and intuitive interface powered by Streamlit.

## 🛠️ Architecture

The project follows a simple modular structure:

- `src/openchat/app.py`: The main Streamlit application handling the UI and session state.
- `src/openchat/ollama_client.py`: A utility module that wraps the Ollama Python library to fetch models and generate streaming responses.

## 📋 Prerequisites

Before running OpenChat, ensure you have the following installed:

1. **Ollama**: Download and install from [ollama.com](https://ollama.com/).
2. **Local Models**: Pull at least one model to get started:
   ```bash
   ollama pull llama3
   ```
3. **Python 3.10+**

## ⚙️ Installation & Setup

1. **Clone the repository**:
   ```bash
   git clone <your-repo-url>
   cd openchat
   ```

2. **Install dependencies**:
   This project uses `uv` for dependency management.
   ```bash
   pip install uv
   uv sync
   ```

3. **Run the application**:
   ```bash
   uv run streamlit run src/openchat/app.py
   ```

## 📖 Usage

1. Start the app using the command above.
2. Select your desired model from the **Configuration** sidebar.
3. Type your message in the chat input at the bottom.
4. Use the **Clear Chat History** button in the sidebar to start a fresh conversation.

## 🛠️ Tech Stack

- **Frontend**: [Streamlit](https://streamlit.io/)
- **LLM Orchestration**: [Ollama](https://ollama.com/)
- **Language**: Python
- **Package Manager**: `uv`
