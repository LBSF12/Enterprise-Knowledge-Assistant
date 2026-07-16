from pathlib import Path
from pypdf import PdfReader
from langchain_text_splitters import RecursiveCharacterTextSplitter

pdf = Path("sample_documents/HR/Leave_Policy.pdf")

reader = PdfReader(pdf)

text = ""

for page in reader.pages:
    text += page.extract_text()

splitter = RecursiveCharacterTextSplitter(
    chunk_size=300,
    chunk_overlap=50
)

chunks = splitter.split_text(text)

print(f"Number of chunks: {len(chunks)}")

print("\nFirst chunk:\n")
print(chunks[0])