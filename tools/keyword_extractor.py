def extract_keywords(text: str) -> list:
    """
    Tool: Extracts simple keywords from text
    """
    words = text.lower().split()
    keywords = set()

    for word in words:
        clean = word.strip(".,()[]{}")
        if len(clean) > 6:
            keywords.add(clean)

    return list(keywords)[:8]
