from backend.retrieval import search_documents

results = search_documents(
    "How many leave days do employees receive?"
)

print(f"Results returned: {len(results)}")

print()

for result in results:

    print(result.payload["text"])

    print("-" * 60)