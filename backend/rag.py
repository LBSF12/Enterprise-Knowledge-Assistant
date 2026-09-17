"""
rag.py

Purpose:
    Orchestrate the full Retrieval-Augmented Generation (RAG) workflow.
"""

from backend.retrieval import search_documents
from backend.llm import ask_llm


def build_context(question: str):
    """
    Retrieve relevant document chunks and combine them into one context.
    """

    results = search_documents(question)

    if not results:
        return None

    context = ""

    for result in results:

        context += (
            f"Department: {result['department']}\n"
            f"Source: {result['source']}\n\n"
            f"{result['text']}\n"
            f"\n-----------------------------\n\n"
        )

    return context


def ask_company_assistant(question: str):
    """
    Full RAG pipeline.
    """

    results = search_documents(question)

    if not results:
        return {
            "answer": "I could not find relevant information in the company knowledge base.",
            "sources": []
        }

    context = ""

    sources = []

    for result in results:

        context += (
            f"Department: {result['department']}\n"
            f"Source: {result['source']}\n\n"
            f"{result['text']}\n"
            "\n-----------------------------\n\n"
        )

        sources.append(
            {
                "file": result["source"],
                "department": result["department"],
                "score": round(result["score"], 3)
            }
        )

    prompt = f"""
You are the Enterprise Knowledge Assistant.

Use ONLY the information below.

If the answer is not present, say you cannot find it.

Context:
{context}

Question:
{question}

Answer:
"""

    answer = ask_llm(prompt)

    return {
        "answer": answer,
        "sources": sources
    }