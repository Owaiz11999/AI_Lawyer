import re

def extract_clauses(text):
    clauses = {}
    patterns = {
        "Confidentiality": r"confidentiality.*?\n",
        "Termination": r"terminate.*?\n",
        "Governing Law": r"governing law.*?\n",
        "Dispute Resolution": r"arbitration.*?\n",
    }
    for label, pattern in patterns.items():
        match = re.search(pattern, text, re.IGNORECASE | re.DOTALL)
        if match:
            clauses[label] = match.group().strip()
    return clauses