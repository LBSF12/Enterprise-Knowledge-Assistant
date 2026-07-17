"""
test_context.py

Purpose:
    Test context generation for the RAG pipeline.
"""

from backend.rag import build_context


question = "How many annual leave days do employees receive?"

context = build_context(question)

print()

print("=" * 80)

print(context)