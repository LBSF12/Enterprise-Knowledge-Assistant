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
    Full RAG pipeline:
    - retrieve relevant chunks
    - build prompt
    - ask Phi-4
    - return final answer
    """

    context = build_context(question)

    if not context:
        return "I could not find relevant information in the company knowledge base."

    prompt = f"""
You are the Enterprise Knowledge Assistant.

Use ONLY the information provided in the context below.

If the answer is not present in the context, say:
'I could not find that information in the company knowledge base.'

Context:
{context}

Question:
{question}

Answer:
"""

    answer = ask_llm(prompt)

    return answer