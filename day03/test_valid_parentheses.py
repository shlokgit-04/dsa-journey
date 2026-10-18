from day03.valid_parentheses import Solution


def test_valid():
    assert Solution().isValid("()") is True
    assert Solution().isValid("()[]{}") is True
    assert Solution().isValid("{[]}") is True


def test_invalid():
    assert Solution().isValid("(]") is False
    assert Solution().isValid("([)]") is False
    assert Solution().isValid("(") is False
    assert Solution().isValid(")") is False
    assert Solution().isValid("(((") is False
    assert Solution().isValid("") is True
