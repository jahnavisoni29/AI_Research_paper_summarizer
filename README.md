# AI Research Paper Summarizer

This is a Streamlit-based web application that allows users to upload research papers in PDF format and get clean, AI-generated summaries in various formats. Users can also ask questions about the content of the paper using an integrated Gemini AI model.

---

##  Features

-  PDF Upload and Text Extraction
-  Summarization in 3 styles:
  - Simple Summary
  - Bullet Points
  - Section-wise Summary
-  Length Options:
  - Short (~100 words)
  - Medium (~300 words)
  - Long (~500+ words)
-  Download summary as TXT or PDF
-  Ask questions about the paper content using Gemini AI

---

##  Requirements

Install the dependencies using:

```
pip install -r requirements.txt
```

**Required packages:**

- `streamlit`
- `PyPDF2`
- `google-generativeai`
- `python-dotenv`
- `reportlab`

---

##  Setup

1. Create a `.env` file in the root directory and add your Gemini API key:

```
GEMINI_API_KEY=your_google_generative_ai_key
```

2. Run the app with:

```
streamlit run app.py
```

---

##  Project Structure

```
├── app.py                  # Streamlit UI
├── summarizer.py          # Gemini-based summarization and Q&A
├── pdf_reader.py          # PDF text extraction
├── requirements.txt
├── README.md
└── .env                   # (Not included) Your Gemini API key
```

---

##  Example Use Cases

- Quickly understand research papers
- Create summaries for reports or presentations
- Interact with long PDFs in a conversational way

---

##  Disclaimer

This is an educational project. Gemini responses may not always be 100% accurate; always verify important information.
