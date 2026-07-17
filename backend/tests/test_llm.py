"""
test_llm.py

Purpose:
    Verify communication with the local Phi-4 model.
"""

from backend.llm import ask_llm


answer = ask_llm(
    "Say hello in one sentence."
)

print(answer)