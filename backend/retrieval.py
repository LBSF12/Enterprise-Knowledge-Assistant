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

    # -----------------------------------------
    # 1. Convert the question into an embedding
    # -----------------------------------------

    question_embedding = generate_embedding(question)


    # -----------------------------------------
    # 2. Search Qdrant
    # -----------------------------------------

    results = client.query_points(
        collection_name=COLLECTION_NAME,
        query=question_embedding,
        limit=limit,
    )


    # -----------------------------------------
    # 3. Prepare our results
    # -----------------------------------------

    search_results = []


    # -----------------------------------------
    # 4. Process every retrieved chunk
    # -----------------------------------------

    for point in results.points:

        # Ignore chunks below our similarity threshold
        if point.score < threshold:
            continue


        search_results.append(
            {
                "score": point.score,
                "text": point.payload["text"],
                "source": point.payload["source"],
                "department": point.payload["department"],
            }
        )


    # -----------------------------------------
    # 5. Return relevant chunks
    # -----------------------------------------

    return search_results