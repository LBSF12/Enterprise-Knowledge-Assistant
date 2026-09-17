I built a fully local Retrieval-Augmented Generation (RAG) system called "Enterprise Knowledge Assistant" as an AI engineering learning project. I want your help turning what I learned into (1) a LinkedIn post and (2) a detailed technical documentation article. Here is the full architecture and every module I implemented:

PROJECT GOAL
A local RAG assistant that lets employees ask natural-language questions and get answers grounded in internal company documents (PDFs), instead of relying on an LLM's built-in knowledge. Everything runs locally/on-prem so company data never leaves the machine.

ARCHITECTURE FLOW
User → Frontend (HTML/CSS/JS) → FastAPI backend → RAG service → Semantic search (Qdrant) + Local LLM (Phi-4 via Ollama) → Answer with sources

TECH STACK
- Python (backend)
- FastAPI + Pydantic + Uvicorn (REST API, request/response models, Swagger/OpenAPI docs)
- LangChain (embeddings/LLM integration glue)
- Ollama running Phi-4 as the local LLM (no cloud API calls)
- Qdrant vector database (running in Docker) for storing and searching embeddings
- Docker Compose for orchestrating Qdrant + Open WebUI
- Vanilla HTML/CSS/JavaScript frontend (no framework), served locally, calling the API via fetch()
- Git/GitHub for version control

BACKEND MODULES (each is its own file with a single responsibility):
- loaders.py — loads and extracts raw text from source documents (PDF loader, expandable to docx/excel)
- chunker.py — splits extracted text into overlapping chunks sized for embedding/retrieval
- embeddings.py — generates vector embeddings for each text chunk
- vector_store.py — manages the Qdrant collection: recreating it and storing chunks with their embeddings + metadata (source filename, department)
- ingest.py — the end-to-end ingestion pipeline that ties loaders → chunker → embeddings → vector_store together for every document in sample_documents/ (organized by department: HR, IT, Cloud)
- retrieval.py — performs semantic search against Qdrant to find the most relevant chunks for a user's question
- rag.py — the core RAG orchestration: takes a question, retrieves relevant context, builds a prompt, and calls the LLM
- llm.py — handles the integration with the local Phi-4 model via Ollama
- models.py — Pydantic request/response models (QuestionRequest, AnswerResponse) for API validation
- api.py — FastAPI app exposing a POST /ask endpoint, with CORS configured for the local frontend, and auto-generated Swagger docs

FRONTEND
- index.html / style.css / script.js — a simple chat-style UI (question input, ask button, chat message thread rendering user/assistant messages and cited sources) that calls the backend's /ask endpoint via fetch and displays the streamed answer with source attribution

INFRASTRUCTURE
- docker-compose.yml spins up Qdrant (vector DB, port 6333) and Open WebUI (alternate local chat interface, port 3000) as containers
- Ollama runs locally on the host (outside Docker) serving the Phi-4 model
- The FastAPI backend runs locally with Uvicorn; frontend is served locally as static files

CURRENT STATUS
- Complete document ingestion pipeline (load → chunk → embed → store)
- Working semantic retrieval over Qdrant
- Local LLM integration with Phi-4
- FastAPI backend with Swagger documentation
- Frontend built and being connected to the backend API

WHAT I LEARNED
- How RAG pipelines work end-to-end (retrieval + augmentation + generation)
- Vector databases and embedding-based semantic search (Qdrant)
- Chunking strategies for document retrieval
- Building and documenting a REST API with FastAPI/Pydantic
- Running LLMs fully locally/offline with Ollama for data privacy
- Containerizing infrastructure with Docker Compose
- Connecting a vanilla JS frontend to a Python backend, including CORS handling
- Structuring a real backend into clean, single-responsibility modules

FUTURE ROADMAP
- Document upload via the web UI
- Conversation history and streaming responses
- Source citations in the UI
- Microsoft Entra ID authentication
- SharePoint Online and Azure Blob Storage integration
- Azure deployment and Microsoft Teams integration

# Author

Built as part of an AI Engineering learning journey focused on enterprise Retrieval-Augmented Generation (RAG) systems.
