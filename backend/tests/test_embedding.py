"""
Test embedding generation.
"""

from langchain_ollama import OllamaEmbeddings

embedding_model = OllamaEmbeddings(
    model="nomic-embed-text"
)

text = "Employees receive 25 annual leave days."

vector = embedding_model.embed_query(text)

print(f"Vector length: {len(vector)}")

print(vector[:10])  # Print the first 10 elements of the vector
