"""
chunker.py

Purpose:
    Split document text into smaller chunks before creating embeddings.
"""

from langchain_text_splitters import RecursiveCharacterTextSplitter


def split_text(text: str):
    """
    Split text into overlapping chunks.
    """

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=250,
        chunk_overlap=40
    )

    return splitter.split_text(text)