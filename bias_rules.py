BIAS_PATTERNS = {
    "confirmation_bias": [
        "i knew i was right", "obviously true", "everyone agrees"
    ],
    "negativity_bias": [
        "always bad", "never works", "worst case", "this will fail"
    ],
    "anchoring_bias": [
        "first impression", "initial estimate", "starting point"
    ]
}

def detect_biases(text):
    found_biases = []
    text = text.lower()
    for bias, phrases in BIAS_PATTERNS.items():
        for phrase in phrases:
            if phrase in text:
                found_biases.append(bias)
                break
    return found_biases
