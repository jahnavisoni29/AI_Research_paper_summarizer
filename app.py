import streamlit as st
from pdf_reader import extract_text_from_pdf
from summarizer import summarize_text, ask_question_about_text
from io import BytesIO
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.enums import TA_JUSTIFY

# ---------------------- #
# Page Config
# ---------------------- #
st.set_page_config(page_title="AI Research Paper Summarizer", layout="centered")

st.title("🧠 AI Research Paper Summarizer")
st.markdown("""
Upload a research paper PDF, choose summary preferences, and get an AI-generated summary instantly.
""")

# Session state
if "extracted_text" not in st.session_state:
    st.session_state.extracted_text = ""
if "summary" not in st.session_state:
    st.session_state.summary = ""

# ---------------------- #
# Upload PDF
# ---------------------- #
st.header("📄 1. Upload Research Paper")
uploaded_file = st.file_uploader("Upload a research paper PDF", type="pdf")

# ---------------------- #
# Summary Options
# ---------------------- #
st.header("🎯 2. Summary Style")
style = st.selectbox("Choose summary style:", [
    "Simple Summary",
    "Bullet Points",
    "Section-wise Summary"
])

st.header("📏 3. Summary Length")
length = st.selectbox("Choose summary length:", [
    "Short (~100 words)",
    "Medium (~300 words)",
    "Long (~500+ words)"
])

# ---------------------- #
# Summarize
# ---------------------- #
if uploaded_file and st.button("🚀 Summarize"):
    try:
        with st.spinner("⏳ Extracting text from PDF..."):
            text = extract_text_from_pdf(uploaded_file)

        st.session_state.extracted_text = text

        with st.spinner("🧠 Generating summary..."):
            summary = summarize_text(text[:3000], style, length)

        st.session_state.summary = summary

        st.success("✅ Summary generated successfully!")

    except ValueError as e:
        st.error(str(e))

# ---------------------- #
# Display Summary
# ---------------------- #
if st.session_state.summary:
    st.header("📋 4. Summary")
    st.write(st.session_state.summary)

    # Download TXT
    st.download_button(
        "📄 Download Summary as TXT",
        st.session_state.summary.encode("utf-8"),
        file_name="summary.txt",
        mime="text/plain"
    )

    # Download PDF
    pdf_buffer = BytesIO()
    doc = SimpleDocTemplate(pdf_buffer, pagesize=letter)
    styles = getSampleStyleSheet()
    custom_style = ParagraphStyle(
        "CustomStyle",
        parent=styles["Normal"],
        fontSize=11,
        leading=14,
        alignment=TA_JUSTIFY
    )

    story = []
    for para in st.session_state.summary.split("\n"):
        if para.strip():
            story.append(Paragraph(para, custom_style))
            story.append(Spacer(1, 12))

    doc.build(story)
    pdf_buffer.seek(0)

    st.download_button(
        "📝 Download Summary as PDF",
        pdf_buffer.getvalue(),
        file_name="summary.pdf",
        mime="application/pdf"
    )

# ---------------------- #
# Chat with Paper
# ---------------------- #
if st.session_state.extracted_text:
    st.header("💬 5. Chat with Paper")

    user_question = st.text_input("Ask a question about the paper:")

    if user_question:
        with st.spinner("🤖 Thinking..."):
            answer = ask_question_about_text(
                st.session_state.extracted_text,
                user_question
            )

        st.success("📢 Answer:")
        st.write(answer)
