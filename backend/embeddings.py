"""
embeddings.py

Purpose:
    Generate embeddings using Ollama.
"""

from langchain_ollama import OllamaEmbeddings

embedding_model = OllamaEmbeddings(
    model="nomic-embed-text"
)


def generate_embedding(text: str):
    """
    Generate an embedding vector.
    """

    return embedding_model.embed_query(text)