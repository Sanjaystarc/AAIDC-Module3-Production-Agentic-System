from tools.readme_checker import check_missing_sections

def reviewer_agent(state: dict) -> dict:
    """
    Agent: Reviewer / Critic
    Reviews README completeness
    """
    readme = state.get("readme", "")
    missing = check_missing_sections(readme)

    if missing:
        state["review_feedback"] = f"Missing sections: {missing}"
    else:
        state["review_feedback"] = "README looks complete."

    return state
