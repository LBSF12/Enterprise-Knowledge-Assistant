"""
test_chunking.py

Purpose:
    Demonstrates how to split extracted document text into chunks
    before generating embeddings.
"""

from pathlib import Path
from pypdf import PdfReader

from backend.chunker import split_text

pdf = Path("sample_documents/HR/Leave_Policy.pdf")

reader = PdfReader(pdf)

text = ""

for page in reader.pages:
    text += page.extract_text()

chunks = split_text(text)

print(f"Chunks created: {len(chunks)}")

print()

print(chunks[0])