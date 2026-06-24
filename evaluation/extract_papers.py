import os
from PyPDF2 import PdfReader

def extract_text_from_pdf(pdf_path):
    """Extract all text from a PDF file."""
    reader = PdfReader(pdf_path)
    text = ""
    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + "\n"
    return text

def build_paper_list(pdf_folder):
    """
    Scans a folder of PDFs and builds the `papers` list structure
    needed by run_latency_test(), including page count and word count.
    """
    papers = []
    pdf_files = sorted([f for f in os.listdir(pdf_folder) if f.lower().endswith(".pdf")])

    for i, fname in enumerate(pdf_files, start=1):
        path = os.path.join(pdf_folder, fname)
        reader = PdfReader(path)
        num_pages = len(reader.pages)
        text = extract_text_from_pdf(path)
        word_count = len(text.split())

        papers.append({
            "id": i,
            "filename": fname,
            "pages": num_pages,
            "word_count": word_count,
            "text": text
        })
        print(f"[{i}] {fname} | {num_pages} pages | {word_count} words")

    return papers

if __name__ == "__main__":
    # Point this at the folder containing your 5+ PDF papers
    pdf_folder = "."
    papers = build_paper_list(pdf_folder)
    print(f"\nExtracted {len(papers)} papers.")