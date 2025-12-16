MAX_INPUT_CHARS = 4000

BLOCKED_PHRASES = [
    "ignore previous instructions",
    "system prompt",
    "act as system"
]

def validate_input(text: str) -> str:
    """
    Validates user input for safety and size limits
    """
    if not text or not text.strip():
        raise ValueError("Input cannot be empty.")

    if len(text) > MAX_INPUT_CHARS:
        raise ValueError("Input too long. Please shorten the text.")

    lower_text = text.lower()
    for phrase in BLOCKED_PHRASES:
        if phrase in lower_text:
            raise ValueError("Potential prompt injection detected.")

    return text.strip()
