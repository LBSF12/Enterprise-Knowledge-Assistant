"""
llm.py

Purpose:
    Send prompts to the local Phi-4 model running in Ollama.
"""

from langchain_ollama import ChatOllama


# Connect to the local model
llm = ChatOllama(
    model="phi4",
    temperature=0,
)


def ask_llm(prompt: str):
    """
    Send a prompt to Phi-4 and return its answer.
    """

    response = llm.invoke(prompt)

    return response.content