"""
retrieval.py

Purpose:
    Search the vector database for relevant document chunks.
"""

from backend.embeddings import generate_embedding
from backend.vector_store import client, COLLECTION_NAME


def search_documents(
        question: str, 
        limit: int = 3,
        threshold: float = 0.60,
    ):
    """
    Search the vector database using semantic similarity.
    """

    question_embedding = generate_embedding(question)

    results = client.query_points(
        collection_name=COLLECTION_NAME,
        query=question_embedding,
        limit=limit,
    )

    search_results = []

    for point in results.points:

        if point.score >= threshold:

            search_results.append(
                {
                    "score": point.score,
                    "text": point.payload["text"],
                    "source": point.payload["source"],
                    "department": point.payload["department"],
                }
            )

    return search_results