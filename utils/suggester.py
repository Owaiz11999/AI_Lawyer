def suggest_improvement(phrase):
    suggestions = {
        "sole discretion": "Replace with 'reasonable discretion with prior notice'.",
        "may terminate at any time": "Define specific conditions or notice periods.",
        "indefinitely": "Add end conditions or maximum duration.",
        "not liable": "Specify exceptions or limit the scope.",
        "without notice": "Add a minimum notice period clause."
    }
    return suggestions.get(phrase, "Looks good!")