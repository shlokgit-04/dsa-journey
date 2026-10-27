from valid_parentheses import Solution

def test_basic():
    assert Solution().isValid("()[]{}") is True
    assert Solution().isValid("([{}])") is True

def test_failures():
    assert Solution().isValid("(]") is False
    assert Solution().isValid("([)]") is False
    assert Solution().isValid("{]") is False

def test_edges():
    assert Solution().isValid("") is True
    assert Solution().isValid("(") is False
    assert Solution().isValid("]") is False
    assert Solution().isValid("((") is False
