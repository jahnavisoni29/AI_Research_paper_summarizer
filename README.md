# 🧠 AI Research Paper Summarizer

An AI-powered web application that helps users quickly understand research papers by generating concise summaries and enabling interactive question–answering over the paper content.

Built using **Streamlit** and **Google Gemini**, this tool is designed to be simple, fast, and beginner-friendly.

---

## ✨ Features

- 📄 Upload research papers in PDF format  
- 🎯 Generate summaries in different styles:
  - Simple Summary  
  - Bullet Points  
  - Section-wise Summary  
- 📏 Choose summary length (short, medium, long)  
- 💬 Ask questions directly about the research paper  
- 📥 Download the generated summary as **TXT** or **PDF**  
- 🔐 Secure API key handling using environment variables  

---

## 🛠️ Tech Stack

- Python  
- Streamlit (Web Interface)  
- Google Gemini API  
- PyPDF2 (PDF text extraction)  
- ReportLab (PDF generation)  

---

## 🚀 How It Works

1. The user uploads a research paper in PDF format.
2. The application extracts text from the PDF.
3. The extracted text is processed using the Gemini model to generate a summary.
4. Users can read the summary, download it, or ask follow-up questions about the paper.

---

## ▶️ How to Run Locally

### 1️⃣ Clone the repository
```bash
git clone https://github.com/jahnavisoni29/AI_Research_paper_summarizer.git
cd AI_Research_paper_summarizer
```

### 2️⃣ Create and activate a virtual environment
```bash
python -m venv .venv
.venv\Scripts\activate
```

### 3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Set up environment variables
Create a .env file (do NOT commit this file to GitHub):
```env
GEMINI_API_KEY=your_api_key_here
```
Alternatively, you may set the environment variable directly in your system settings.

### 5️⃣ Run the application
```bash
streamlit run app.py
```
The application will open automatically in your browser.

## ⚠️ Notes & Limitations
- Image-only or scanned PDFs may not work without OCR support.
- Summary quality depends on the clarity and structure of the research paper.
- This tool is intended for educational and research assistance purposes only.

## 📌 Future Improvements
- OCR support for scanned PDFs
- Better handling of long research papers
- Deployment on Streamlit Cloud
- Citation-aware summarization

## 👩‍💻 Author
Jahnavi Soni
GitHub: https://github.com/jahnavisoni29

## 📄 License
This project is intended for educational and learning purposes.