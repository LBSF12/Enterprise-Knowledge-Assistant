"""
test_rag.py

Purpose:
    Test the complete Enterprise Knowledge Assistant.
"""

from backend.rag import ask_company_assistant


#question = "How many annual leave days do employees receive?"
question = "Who approves leave requests?"


print("\nQUESTION")
print(question)

print("\nGenerating answer...\n")

answer = ask_company_assistant(question)

print("ANSWER")
print(answer)