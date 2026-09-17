"""
models.py

Purpose:
    Define the request and response models for the API.
"""

from pydantic import BaseModel


class QuestionRequest(BaseModel):
    question: str


class Source(BaseModel):
    file: str
    department: str
    score: float


class AnswerResponse(BaseModel):
    answer: str
    sources: list[Source]