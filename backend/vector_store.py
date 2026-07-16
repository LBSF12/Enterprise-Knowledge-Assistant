"""
vector_store.py

Purpose:
    Connect to the local Qdrant vector database.
"""

from qdrant_client import QdrantClient

client = QdrantClient(
    host="localhost",
    port=6333,
)

print("✅ Connected to Qdrant")