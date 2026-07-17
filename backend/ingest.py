"""
ingest.py

Purpose:
    Main document ingestion pipeline.
"""
from backend.chunker import split_text
from backend.embeddings import generate_embedding
from backend.vector_store import (
    create_collection,
    store_chunk,
)
from pathlib import Path

from backend.loaders import load_pdf

documents = Path("sample_documents")

pdf_files = list(documents.rglob("*.pdf"))

print(f"Found {len(pdf_files)} PDF files.\n")

for pdf in pdf_files:

    print(f"\nProcessing: {pdf.name}")
    text = load_pdf(pdf)
    chunks = split_text(text)

    print(f"Chunks created: {len(chunks)}")
    
    for chunk in chunks:
        
        embedding = generate_embedding(chunk)
        
        store_chunk(chunk, embedding)
        
    print("Document stored successfully.")