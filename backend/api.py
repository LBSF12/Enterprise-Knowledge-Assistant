"""
api.py

Purpose:
    Expose the Enterprise Knowledge Assistant through a REST API.
"""
from fastapi.middleware.cors import CORSMiddleware

from fastapi import FastAPI

from backend.models import (
    QuestionRequest,
    AnswerResponse,
)

from backend.rag import ask_company_assistant

app = FastAPI(
    title="Enterprise Knowledge Assistant",
    version="1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5500",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post(
    "/ask",
    response_model=AnswerResponse,
)
def ask_question(request: QuestionRequest):

    answer = ask_company_assistant(
        request.question
    )

    return AnswerResponse(
        answer=answer
    )