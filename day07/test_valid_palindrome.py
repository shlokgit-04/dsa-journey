from valid_palindrome import is_palindrome, Solution

def test_examples():
    assert is_palindrome("A man, a plan, a canal: Panama") is True
    assert is_palindrome("race a car") is False
    assert is_palindrome(" ") is True

def test_edge_cases():
    assert is_palindrome("") is True
    assert is_palindrome("0P") is False
    assert is_palindrome(".," ) is True

def test_solution_class():
    assert Solution().isPalindrome("Able was I, ere I saw Elba") is True
    assert Solution().isPalindrome("abc") is False
