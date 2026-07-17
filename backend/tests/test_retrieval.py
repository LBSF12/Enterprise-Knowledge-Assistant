from backend.retrieval import search_documents

results = search_documents(
    "How many leave days do employees receive?"
)

print(f"Results returned: {len(results)}")

print()

for i, result in enumerate(results, start=1):

    print("=" * 70)

    print(f"Result #{i}")
    print(f"Similarity : {result.score:.4f}")
    print(f"Department : {result.payload['department']}")
    print(f"Source     : {result.payload['source']}")

    print()
    print(result.payload["text"])
    print("=" * 70)
    print()