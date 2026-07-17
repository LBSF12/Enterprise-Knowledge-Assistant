"""
vector_store.py

Purpose:
    Manage the connection and collections in Qdrant.
"""
from uuid import uuid4

#from qdrant_client.models import PointStruct

from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams, PointStruct

COLLECTION_NAME = "company_documents"

client = QdrantClient(
    host="localhost",
    port=6333,
)


def create_collection():
    """
    Create the Qdrant collection if it doesn't already exist.
    """

    collections = client.get_collections().collections

    names = [collection.name for collection in collections]

    if COLLECTION_NAME in names:
        print(f"Collection '{COLLECTION_NAME}' already exists.")
        return

    client.create_collection(
        collection_name=COLLECTION_NAME,
        vectors_config=VectorParams(
            size=768,
            distance=Distance.COSINE
        )
    )

    print(f"Collection '{COLLECTION_NAME}' created successfully.")


def store_chunk(text: str, embedding: list):
    """
    Store one chunk and its embedding in Qdrant.
    """

    client.upsert(
        collection_name=COLLECTION_NAME,
        points=[
            PointStruct(
                id=str(uuid4()),
                vector=embedding,
                payload={
                    "text": text
                }
            )
        ]
    )    