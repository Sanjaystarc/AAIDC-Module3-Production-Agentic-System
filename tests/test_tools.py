from tools.keyword_extractor import extract_keywords
from tools.readme_checker import check_missing_sections

def test_extract_keywords_returns_list():
    text = "This project uses LangGraph and multi agent orchestration"
    keywords = extract_keywords(text)
    assert isinstance(keywords, list)

def test_check_missing_sections():
    text = "Installation steps are provided"
    missing = check_missing_sections(text)
    assert "usage" in missing
    assert "license" in missing
