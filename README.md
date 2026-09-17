# Enterprise Knowledge Assistant

A fully local Retrieval-Augmented Generation (RAG) AI assistant that answers employee questions using company documents.

The project is being built from scratch as a learning journey into AI Engineering, Docker, Python, Vector Databases, and Enterprise AI solutions.

---

# Project Overview

The Enterprise Knowledge Assistant allows employees to ask questions in natural language and receive answers generated from internal company documents rather than relying only on the language model's built-in knowledge.

The entire solution runs locally using Ollama and Qdrant, ensuring company data remains private.

Current focus:
- Build the complete RAG pipeline
- Learn each component step by step
- Document every stage of the project
- Produce a portfolio-quality enterprise application

---

# Architecture

```text
                 User
                   │
                   ▼
        Frontend (HTML / CSS / JS)
                   │
                   ▼
               FastAPI API
              (POST /ask)
                   │
                   ▼
              RAG Service
                   │
      ┌────────────┴────────────┐
      ▼                         ▼
Semantic Search            Phi-4 (Ollama)
      │
      ▼
   Qdrant
      │
      ▼
Company Documents (PDF)
```

---

# Technologies

| Technology | Purpose |
|------------|---------|
| Python | Backend development |
| FastAPI | REST API framework |
| Pydantic | Request/response validation (`QuestionRequest`, `AnswerResponse`) |
| Uvicorn | ASGI server for the API |
| Docker / Docker Compose | Running Qdrant and Open WebUI as containers |
| Ollama | Local AI model runtime |
| Phi-4 | Local LLM used to generate answers |
| nomic-embed-text | Local embedding model used for semantic search |
| Qdrant | Vector database storing document chunk embeddings |
| LangChain (`langchain-ollama`, `langchain-text-splitters`) | LLM/embedding integration and text chunking |
| pypdf | PDF text extraction |
| HTML / CSS / JavaScript (vanilla) | Frontend chat interface |
| Git / GitHub | Version control |

---

# Project Structure

```text
Enterprise-Knowledge-Assistant/

backend/
├── api.py            # FastAPI app, POST /ask endpoint, CORS config
├── models.py          # Pydantic request/response models
├── rag.py             # RAG orchestration (retrieve -> build prompt -> ask LLM)
├── retrieval.py        # Semantic search against Qdrant
├── vector_store.py      # Qdrant client, collection management, chunk storage
├── embeddings.py        # Embedding generation (nomic-embed-text via Ollama)
├── chunker.py          # Recursive text chunking (chunk_size=250, overlap=40)
├── loaders.py          # PDF text extraction
├── ingest.py           # End-to-end ingestion pipeline (loaders -> chunker -> embeddings -> vector_store)
└── tests/             # Manual verification scripts for each module

frontend/
├── index.html
├── style.css
└── script.js          # Chat UI, calls POST http://127.0.0.1:8000/ask, renders answer + sources

sample_documents/
├── HR/
├── IT/
├── Cloud/
└── General/

docker-compose.yml       # Qdrant + Open WebUI containers
requirements.txt
README.md
```

---

# Features Implemented

## Infrastructure
- Docker Compose running Qdrant (vector database) and Open WebUI (alternate local chat interface)
- Ollama running locally, serving `phi4` (LLM) and `nomic-embed-text` (embeddings)

## Document Ingestion
- PDF text extraction (`loaders.py`)
- Recursive text chunking with overlap (`chunker.py`)
- Embedding generation via Ollama (`embeddings.py`)
- Vector storage in Qdrant with metadata (`source` filename + `department`) (`vector_store.py`)
- `ingest.py` walks `sample_documents/` recursively and rebuilds the Qdrant collection from every `.pdf` file found

> Note: `python-docx` and `openpyxl` are in `requirements.txt` for future `.docx`/`.xlsx` support, but only PDF loading is implemented so far — non-PDF files in `sample_documents/` are not yet ingested.

## Retrieval-Augmented Generation (RAG)
- Semantic search over Qdrant with a similarity score threshold (`retrieval.py`)
- Context assembly from the top matching chunks, grouped with their source/department
- Prompt construction that restricts the LLM to the retrieved context
- Answer generation via Phi-4 (`llm.py`)
- Structured response with per-source similarity scores (`rag.py`)

## Backend API
- FastAPI app with a single `POST /ask` endpoint
- Pydantic request/response validation
- Swagger/OpenAPI docs auto-generated at `/docs`
- CORS restricted to the local frontend origin (`http://localhost:5500`)

## Frontend
- Chat-style UI (question input, message thread, avatars)
- Connected to the backend `/ask` endpoint
- Displays the assistant's answer along with cited sources (file name, department, similarity score)

---

# Requirements

Before running the project, make sure you have:

- **Python 3.10+**
- **Docker Desktop** (for Qdrant and Open WebUI)
- **[Ollama](https://ollama.com)** installed locally, with these models pulled:
  ```
  ollama pull phi4
  ollama pull nomic-embed-text
  ```
- Python dependencies from `requirements.txt`

---

# How to Run

**1. Start the containers** (Qdrant + Open WebUI):
```bash
docker-compose up -d
```
- Qdrant → http://localhost:6333
- Open WebUI → http://localhost:3000

**2. Make sure Ollama is running** with `phi4` and `nomic-embed-text` pulled (see Requirements above).

**3. Install Python dependencies** (from the project root):
```bash
pip install -r requirements.txt
```

**4. Ingest the sample documents** into Qdrant (from the project root, so the `backend.` imports resolve):
```bash
python -m backend.ingest
```
This recreates the Qdrant collection and embeds every `.pdf` under `sample_documents/`.

**5. Start the backend API** on port 8000 (required — the frontend calls `http://127.0.0.1:8000/ask`):
```bash
uvicorn backend.api:app --reload --port 8000
```
Swagger docs: http://127.0.0.1:8000/docs

**6. Serve the frontend** on port 5500 (required — the API's CORS policy only allows `http://localhost:5500`):
```bash
cd frontend
python -m http.server 5500
```
Then open http://localhost:5500 in your browser.

---

# Testing

`backend/tests/` contains standalone scripts (not a pytest suite) for manually verifying each stage of the pipeline. Run any of them from the project root, e.g.:

```bash
python -m backend.tests.test_loader
python -m backend.tests.test_chunking
python -m backend.tests.test_embedding
python -m backend.tests.test_vector_store
python -m backend.tests.test_retrieval
python -m backend.tests.test_rag
python -m backend.tests.test_llm
python -m backend.tests.evaluate_retrieval
```

---

# Learning Objectives

This project is designed to learn:

- Retrieval-Augmented Generation (RAG)
- Vector Databases
- Embedding Models
- FastAPI
- REST APIs
- Docker
- Enterprise AI Architecture
- Git & GitHub
- AI Engineering Best Practices

---

# Current Status

✅ Complete document ingestion pipeline (PDF only)

✅ Semantic retrieval with similarity thresholding

✅ Local LLM integration (Phi-4)

✅ FastAPI backend with Swagger documentation

✅ Frontend chat UI connected to the backend API

🚧 Document loaders for `.docx` / `.xlsx`

🚧 Conversation history, streaming responses

---

# Future Improvements

- `.docx` / `.xlsx` document loaders
- Upload documents through the web interface
- Conversation history
- Streaming AI responses
- Microsoft Entra ID Authentication
- SharePoint Online integration
- Azure Blob Storage integration
- Azure deployment
- Microsoft Teams integration

---

# Author

Built as part of an AI Engineering learning journey focused on enterprise Retrieval-Augmented Generation (RAG) systems.
