def test_multi_agent_workflow():
    from graph.workflow import run_workflow

    sample_input = {
        "readme": "## Project Title\nThis is a sample project."
    }

    result = run_workflow(sample_input)

    assert "title" in result
    assert "tags" in result
