RISKY_PHRASES = {
    "sole discretion": 4,
    "may terminate at any time": 5,
    "indefinitely": 3,
    "not liable": 4,
    "without notice": 5
}

def detect_risky_phrases(text):
    found = []
    for phrase, severity in RISKY_PHRASES.items():
        if phrase in text.lower():
            found.append({"phrase": phrase, "severity": severity})
    return found
