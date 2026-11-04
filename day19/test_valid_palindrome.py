from day19.valid_palindrome import Solution


def test_example():
    assert Solution().isPalindrome("A man, a plan, a canal: Panama") is True


def test_not_palindrome():
    assert Solution().isPalindrome("race a car") is False


def test_punctuation_only():
    assert Solution().isPalindrome(" ") is True


def test_mixed_case():
    assert Solution().isPalindrome("Madam") is True
