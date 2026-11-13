from day28.valid_palindrome import Solution


def test_classic():
    assert Solution().isPalindrome("A man, a plan, a canal: Panama") is True


def test_not_palindrome():
    assert Solution().isPalindrome("race a car") is False


def test_space_only():
    assert Solution().isPalindrome(" ") is True


def test_case_insensitive():
    assert Solution().isPalindrome("Noon") is True


def test_digits_and_punct():
    assert Solution().isPalindrome("0P") is False
