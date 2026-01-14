def test_end_to_end_execution():
    from app import process_user_input

    output = process_user_input("Analyze this repository")

    assert output is not None
