from pathlib import Path
from pypdf import PdfReader

DOCUMENT_FOLDER = Path("sample_documents")

for file in DOCUMENT_FOLDER.rglob("*.pdf"):

    print("=" * 50)
    print(f"Reading: {file.name}")

    reader = PdfReader(file)

    print(f"Pages: {len(reader.pages)}")
    for page in reader.pages:
        text = page.extract_text()
        print(text)