import streamlit as st
from utils.pdf_parser import extract_text_from_pdf, extract_text_from_docx
from utils.clause_classifier import extract_clauses
from utils.ner_extractor import extract_entities
from utils.risk_detector import detect_risky_phrases
from utils.suggester import suggest_improvement

st.set_page_config(page_title="AI Lawyer: Legal Analyzer", layout="wide")
st.title("\U0001F4DC AI Lawyer - Legal Document Analyzer")

uploaded_file = st.file_uploader("Upload a Legal Document", type=["pdf", "docx"])

if uploaded_file:
    file_ext = uploaded_file.name.split(".")[-1]
    with st.spinner("Extracting text..."):
        if file_ext == "pdf":
            text = extract_text_from_pdf(uploaded_file)
        else:
            text = extract_text_from_docx(uploaded_file)

    st.subheader("\U0001F4D9 Document Preview")
    st.text_area("Extracted Text", text, height=300)

    st.subheader("\U0001F9E0 Detected Clauses")
    clauses = extract_clauses(text)
    for title, content in clauses.items():
        st.markdown(f"**{title}**: {content}")

    st.subheader("\U0001F50D Named Entities")
    entities = extract_entities(text)
    st.write(entities)

    st.subheader("\u26A0 Risky Phrases Found")
    risks = detect_risky_phrases(text)
    for risk in risks:
        st.markdown(f"- **{risk['phrase']}** (Severity: {risk['severity']})")

    st.subheader("\U0001F4A1 Suggested Improvements")
    for risk in risks:
        suggestion = suggest_improvement(risk['phrase'])
        st.markdown(f"- **{risk['phrase']}** → _{suggestion}_")