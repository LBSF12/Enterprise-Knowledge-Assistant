"""
loaders.py

Purpose:
    Read PDF documents from the sample_documents folder.
"""

from pathlib import Path
from pypdf import PdfReader


def load_pdf(pdf_path: Path):
    """
    Read a PDF and return its text.
    """

    reader = PdfReader(pdf_path)

    text = ""

    for page in reader.pages:
        extracted = page.extract_text()

        if extracted:
            text += extracted + "\n"

    return text