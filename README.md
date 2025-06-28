# AI Lawyer: Legal Document Analyzer

An AI-powered tool that analyzes legal documents to classify clauses, extract key entities, identify risks, and suggest legal improvements — all through a simple Streamlit interface.

## 🚀 Features

- 📄 Upload and parse legal documents (PDF or DOCX)
- 🧠 Classify clauses (e.g., confidentiality, indemnity)
- 🧾 Extract named entities (e.g., parties, dates, money)
- ⚠️ Detect risky clauses using custom logic and ML
- 💡 Suggest clause improvements
- 💻 Streamlit-based user interface

## 🗂️ Project Structure

├── app.py # Main Streamlit app
├── requirements.txt # Project dependencies
├── utils/
│ ├── pdf_parser.py # Text extraction from PDF/DOCX
│ ├── clause_classifier.py # Clause classification logic
│ ├── ner_extractor.py # Named entity recognition
│ ├── risk_detector.py # Risk scoring mechanism
│ ├── suggester.py # Suggestion generator
├── models/
│ ├── clause_model.pkl # Trained ML model for clauses
│ └── custom_ner_model/ # NER model files
├── data/
│ └── sample_contracts/ # Example contracts for testing


## ⚙️ Tech Stack

- **Frontend**: Streamlit
- **NLP**: spaCy, Transformers, NLTK
- **ML/DL**: Scikit-learn, PyTorch
- **Parsing**: pdfminer.six, python-docx
- **Data Handling**: Pandas

Usage:

Upload a contract file (PDF/DOCX)
Get clause classifications
View extracted entities
See risk scores
Read improvement suggestions

Future Improvements

Multi-language support
Integration with legal clause databases
Export results as annotated PDF
GPT-based legal explanation system

## 🛠️ Setup Instructions

1. Clone the repository:

```bash
git clone https://github.com/yourusername/ai-lawyer.git
cd ai-lawyer
pip install -r requirements.txt
streamlit run app.py

