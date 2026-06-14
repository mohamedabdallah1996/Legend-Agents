# Legend Agents

A conversational AI game that brings historical legends to life as interactive agents, allowing users to explore ideas, stories, and perspectives from the greatest minds in history.

## Available Legends

| ID | Name |
|---|---|
| `einstein` | Albert Einstein |
| `newton` | Isaac Newton |
| `turing` | Alan Turing |
| `gandhi` | Mahatma Gandhi |
| `mandela` | Nelson Mandela |
| `saladin` | Salah El-din |

## Prerequisites

- Python 3.11+
- [uv](https://docs.astral.sh/uv/getting-started/installation/)
- A [Groq](https://console.groq.com/) API key

## Setup

```bash
cd legendagents-api
uv sync
```

Copy the example env file and fill in your keys:

```bash
cp .env.example .env
```

**.env fields:**

```env
# Required
GROQ_API_KEY=your_groq_api_key

# Optional — LangSmith tracing
LANGSMITH_API_KEY=your_langsmith_key

# Optional — Opik prompt versioning (Comet ML)
COMET_API_KEY=your_comet_key
COMET_PROJECT=legend-agents
```

## Running the API

```bash
cd legendagents-api
uv run fastapi dev src/legendagents/infrastructure/api.py --port 8888
```

The server starts at `http://127.0.0.1:8888`.  
Interactive docs are available at `http://127.0.0.1:8888/docs`.

## Calling the `/chat` endpoint

**curl:**

```bash
curl -X POST http://localhost:8888/chat \
  -H "Content-Type: application/json" \
  -d '{"legend_id": "einstein", "message": "What is your theory of relativity?"}'
```

**Response:**

```json
{
  "response": "Imagine you are on a train moving at the speed of light..."
}
```

**Python (httpx):**

```python
import httpx

response = httpx.post(
    "http://localhost:8888/chat",
    json={"legend_id": "gandhi", "message": "How should we respond to injustice?"}
)
print(response.json()["response"])
```

## Running Tests

```bash
cd legendagents-api

# Unit tests (no API key needed)
uv run pytest -m "not integration"

# Integration tests (calls Groq API)
uv run pytest -m integration
```

## LangGraph Studio

Visualise and debug the conversation graph interactively:

```bash
cd legendagents-api
uv run langgraph dev --tunnel
```

Open the Studio URL printed in the terminal. Add `http://127.0.0.1:2024` to the allowed domains list in LangSmith Advanced Settings if you prefer running without a tunnel.
