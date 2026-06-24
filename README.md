# AI Research Paper Summarizer

An AI-powered web application that helps users quickly understand academic research papers by generating concise summaries, answering questions about paper content, and evaluating summary quality using standard NLP metrics.

Built using Streamlit, Google Gemini 2.5 Flash, and Python, this project provides an intuitive interface for research paper analysis while incorporating quantitative evaluation through ROUGE, BERTScore, and latency benchmarking.

---

# Features

## Research Paper Analysis

* Upload research papers in PDF format
* Automatic text extraction using PyPDF2
* Support for multi-page academic documents

## Flexible Summarization

Generate summaries in multiple styles:

* Simple Summary
* Bullet Points
* Section-wise Summary

Choose summary length:

* Short (~100 words)
* Medium (~300 words)
* Long (~500 words)

## Question Answering

* Ask natural language questions about the uploaded paper
* Context-aware responses powered by Google Gemini

## Export Options

* Download generated summaries as TXT
* Download generated summaries as PDF

## Secure Configuration

* API key management using environment variables
* Sensitive credentials excluded using .gitignore

## Evaluation Framework

* ROUGE-1 Evaluation
* ROUGE-2 Evaluation
* ROUGE-L Evaluation
* BERTScore Evaluation
* Latency Testing
* Prompt Variant Comparison

---

# Tech Stack

## Languages

* Python

## Frameworks and Libraries

* Streamlit
* Google Gemini API
* PyPDF2
* ReportLab
* Python-dotenv

## Evaluation Libraries

* ROUGE Score
* BERTScore

## Concepts Used

* Large Language Models (LLMs)
* Prompt Engineering
* Natural Language Processing (NLP)
* Research Paper Summarization
* Performance Evaluation

---

# How It Works

1. User uploads a research paper PDF.
2. Text is extracted from the document.
3. Gemini 2.5 Flash processes the extracted content.
4. A summary is generated according to user preferences.
5. Users can:

   * Read the summary
   * Download the summary
   * Ask questions about the paper
6. Evaluation scripts measure summary quality and performance.

---

# Project Structure

```text
AI_Research_Paper_Summarizer/
│
├── app.py
├── pdf_reader.py
├── summarizer.py
├── requirements.txt
├── README.md
│
├── evaluation/
│   ├── abstracts.py
│   ├── summaries.py
│   ├── extract_papers.py
│   ├── run_test.py
│   ├── evaluate_variants.py
│   ├── bertscore.py
│   └── rouge_score_of_5_papers.py
│
└── papers/ (ignored)
Note:
The `papers/` directory contains evaluation PDFs used during testing and is excluded from version control through `.gitignore`. Users can add their own research papers locally when running evaluation scripts.
```

---

# Evaluation Methodology

To assess the quality and efficiency of generated summaries, the project includes a dedicated evaluation pipeline.

## Summary Quality Metrics

### ROUGE Evaluation

Measures lexical overlap between generated summaries and reference abstracts.

* ROUGE-1
* ROUGE-2
* ROUGE-L

### BERTScore Evaluation

Measures semantic similarity between generated summaries and reference abstracts using contextual embeddings.

## Performance Metrics

### Latency Testing

Measures:

* Minimum response time
* Maximum response time
* Average response time
* Standard deviation

across multiple research papers of varying lengths.

---

# Prompt Engineering Experiments

Multiple prompt variants were designed and compared to improve summary quality.

## Variant A – Baseline

Standard instructional prompt.

## Variant B – Expert Role Prompt

Assigns the model the role of an academic summarizer and prioritizes:

* Problem statement
* Methodology
* Key findings

## Variant C – Structured Output Prompt

Uses a stricter output format and response constraints.

The variants were evaluated using:

* ROUGE metrics
* Latency measurements

to identify the most effective prompting strategy.

---

# Running the Project Locally

## 1. Clone the Repository

```bash
git clone https://github.com/jahnavisoni29/AI_Research_paper_summarizer.git

cd AI_Research_paper_summarizer
```

## 2. Create a Virtual Environment

```bash
python -m venv .venv
```

Activate the environment:

### Windows

```bash
.venv\Scripts\activate
```

### macOS/Linux

```bash
source .venv/bin/activate
```

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

## 4. Configure Environment Variables

Set your Gemini API key in the terminal before running the application.

### Windows PowerShell

```powershell
$env:GEMINI_API_KEY="your_api_key_here"
```

### macOS/Linux

```bash
export GEMINI_API_KEY="your_api_key_here"
```
Note: The API key can also be provided through a .env file

## 5. Run the Application

```bash
streamlit run app.py
```

The application will open automatically in your browser.

---

# Requirements

```text
streamlit
PyPDF2
google-generativeai
python-dotenv
reportlab
rouge-score
bert-score
```

---

# Limitations

* Scanned or image-only PDFs are not currently supported.
* Very large research papers may require text truncation.
* Summary quality depends on the quality of extracted text.
* Generated summaries should be reviewed before academic or professional use.

---

# Future Improvements

* OCR support for scanned PDFs
* Citation-aware summarization
* Multi-document summarization
* Research paper comparison mode
* Streamlit Cloud deployment
* Evaluation dashboard
* Semantic search across uploaded papers

---

# Author

Jahnavi Soni

B.Tech, Mechanical and Automation Engineering
Indira Gandhi Delhi Technical University for Women (IGDTUW)

GitHub: https://github.com/jahnavisoni29

---

# License

This project is intended for educational, research, and learning purposes.
