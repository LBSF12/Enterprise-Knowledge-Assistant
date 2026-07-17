from backend.embeddings import generate_embedding

text = "Employees receive 25 annual leave days."

vector = generate_embedding(text)

print(len(vector))

print(vector[:10])