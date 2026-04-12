from task_utils import slugify, truncate_description, validate_priority


def test_slugify_converts_text_to_hyphenated_identifier():
    assert slugify("Hello World from QA") == "hello-world-from-qa"


def test_validate_priority_accepts_valid_values():
    assert validate_priority("high") is True
    assert validate_priority("medium") is True
    assert validate_priority("low") is True


def test_truncate_description_limits_length():
    long_text = "This is a very long sentence that needs to be truncated for card rendering in the task board."
    result = truncate_description(long_text, max_len=30)

    assert result == "This is a very long sentenc..."
