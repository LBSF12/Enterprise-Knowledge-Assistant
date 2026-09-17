from backend.retrieval import search_documents

results = search_documents(
    "How can i use my leave days?",
)

print(f"Results returned: {len(results)}")

print()

for i, result in enumerate(results, start=1):

    print("=" * 70)

    print(f"Result #{i}")
    print(f"Similarity : {result['score']:.4f}")
    print(f"Department : {result['department']}")
    print(f"Source     : {result['source']}")

    print()
    print(result["text"])
    print("=" * 70)
    print()