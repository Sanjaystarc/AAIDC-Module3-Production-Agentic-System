from agents.repo_analyzer import repo_analyzer_agent

def test_repo_analyzer_agent():
    state = {"readme": "Sample README content"}
    updated_state = repo_analyzer_agent(state)
    assert "readme" in updated_state
