from day16.valid_parentheses import is_valid


def test_simple_pair():
    assert is_valid("()") is True


def test_nested():
    assert is_valid("()[]{}") is True


def test_wrong_order():
    assert is_valid("(]") is False


def test_interleaved():
    assert is_valid("([)]") is False


def test_unclosed():
    assert is_valid("(") is False
