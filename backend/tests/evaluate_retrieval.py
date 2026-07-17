"""
evaluate_retrieval.py

Purpose:
    Evaluate the semantic retrieval quality of the Enterprise Knowledge Assistant.
    Displays similarity scores, document sources, and retrieved text for
    each evaluation question.
"""

from backend.retrieval import search_documents
from backend.tests.evaluation_questions import QUESTIONS


for question in QUESTIONS:

    print()
    print("=" * 80)
    print("QUESTION")
    print(question)
    print("=" * 80)

    results = search_documents(question)

    if not results:
        print("No matching documents found.")
        continue

    for i, result in enumerate(results, start=1):

        print(f"\nResult #{i}")
        print(f"Score      : {result['score']:.4f}")
        print(f"Department : {result['department']}")
        print(f"Source     : {result['source']}")
        print()
        print(result["text"][:180])
        print("-" * 60)