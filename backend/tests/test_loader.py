from pathlib import Path

from backend.loaders import load_pdf

pdf = Path("sample_documents/HR/Leave_Policy.pdf")

text = load_pdf(pdf)

print(text)