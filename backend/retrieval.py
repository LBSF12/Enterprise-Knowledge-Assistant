"""
retrieval.py

Purpose:
    Search the vector database for relevant document chunks.
"""

from backend.embeddings import generate_embedding
from backend.vector_store import client, COLLECTION_NAME

from qdrant_client.models import Filter


def search_documents(question: str, limit: int = 3):
    """
    Search Qdrant for the most relevant document chunks.
    """

    question_embedding = generate_embedding(question)

    results = client.query_points(
        collection_name=COLLECTION_NAME,
        query=question_embedding,
        limit=limit
    )

    return results.points