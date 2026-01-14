def test_metadata_agent_returns_output():
    from agents.metadata_agent import generate_metadata

    result = generate_metadata("This is a test README")
    assert result is not None
    assert isinstance(result, dict)
