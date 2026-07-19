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

# Current Architecture

```text
                 User
                   │
                   ▼
          (Future Chat Interface)
                   │
                   ▼
               FastAPI API
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
| Docker | Container management |
| Docker Compose | Multi-container orchestration |
| Ollama | Local AI model runtime |
| Phi-4 | Local Large Language Model |
| Qdrant | Vector database |
| LangChain | Embeddings and LLM integration |
| Open WebUI | Local AI interface |
| Git | Version control |
| GitHub | Source code management |

---

# Project Structure

```text
Enterprise-Knowledge-Assistant/

backend/
│
├── loaders.py
├── chunker.py
├── embeddings.py
├── vector_store.py
├── retrieval.py
├── rag.py
├── llm.py
├── ingest.py
└── tests/

sample_documents/
│
├── HR/
├── IT/
└── Cloud/

docker-compose.yml
requirements.txt
README.md
```

---

# Features Implemented

## Infrastructure

- Docker Desktop installed
- Docker Compose configured
- Ollama running locally
- Phi-4 model downloaded
- Open WebUI configured
- Qdrant Vector Database running
![Docker Containers](docs/images/docker-containers.png)

## Swagger API

![Swagger API](docs/images/swagger-api.png)

## Document Processing

- PDF document loader
- Recursive text chunking
- Embedding generation
- Vector storage in Qdrant
- Metadata storage (department & source)

## Retrieval-Augmented Generation (RAG)

- Semantic search
- Context building
- Prompt generation
- Phi-4 integration
- End-to-end RAG pipeline

## Backend API

- FastAPI project created
- REST API endpoint (`POST /ask`)
- Swagger/OpenAPI documentation
- Request & Response models using Pydantic
- CORS configuration

## Frontend

- Frontend project structure created
- Local frontend web server
- HTML/CSS application skeleton

---

# Project Structure

```text
Enterprise-Knowledge-Assistant/

backend/
    api.py
    rag.py
    retrieval.py
    embeddings.py
    chunker.py
    loaders.py
    llm.py
    vector_store.py
    ingest.py
    models.py

frontend/
    index.html
    style.css
    script.js

sample_documents/

docker-compose.yml

requirements.txt

README.md
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

✅ Complete document ingestion pipeline

✅ Semantic retrieval

✅ Local LLM integration (Phi-4)

✅ FastAPI backend

✅ Swagger API documentation

✅ Frontend project initialized

🚧 Connecting frontend to backend API

---

# Screenshots

## Project Architecture

(Add later)

---

## Docker Containers

(Add screenshot)

---

## Open WebUI

(Add screenshot)

---

## Qdrant Dashboard

(Add screenshot)

---

## Swagger API

(Add screenshot)

---

## Enterprise Chat Interface

(Coming Soon)

---

# Future Improvements

- Upload documents through the web interface
- Conversation history
- Streaming AI responses
- Source citations
- Microsoft Entra ID Authentication
- SharePoint Online integration
- Azure Blob Storage integration
- Azure deployment
- Microsoft Teams integration

---

# Author

Built as part of an AI Engineering learning journey focused on enterprise Retrieval-Augmented Generation (RAG) systems.