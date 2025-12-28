import PyPDF2
from io import BytesIO

def extract_text_from_pdf(pdf_file_object):
    """
    Extracts text from a given PDF file object (BytesIO or file path).
    Returns extracted text or raises ValueError if extraction fails.
    """
    text = ""

    try:
        # Handle Streamlit uploaded file (BytesIO-like)
        if isinstance(pdf_file_object, BytesIO):
            pdf_file_object.seek(0)
            reader = PyPDF2.PdfReader(pdf_file_object)
        else:
            with open(pdf_file_object, "rb") as file:
                reader = PyPDF2.PdfReader(file)

        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"

        # ❗ Stop pipeline if no text extracted
        if not text.strip():
            raise ValueError(
                "No text could be extracted. The PDF may be scanned, image-only, or empty."
            )

        return text

    except Exception as e:
        raise ValueError(
            f"PDF text extraction failed: {str(e)}"
        )
