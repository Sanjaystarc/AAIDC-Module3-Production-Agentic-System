from tools.repo_reader import read_readme_text

def repo_analyzer_agent(state: dict) -> dict:
    """
    Agent: Repo Analyzer
    Reads and stores README content in shared state
    """
    readme_text = state.get("readme", "")
    state["readme"] = read_readme_text(readme_text)
    return state
