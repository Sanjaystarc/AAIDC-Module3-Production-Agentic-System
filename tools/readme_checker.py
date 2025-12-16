def check_missing_sections(readme_text: str) -> list:
    """
    Tool: Checks for missing README sections
    """
    required_sections = ["installation", "usage", "license"]
    text = readme_text.lower()

    missing = []
    for section in required_sections:
        if section not in text:
            missing.append(section)

    return missing
