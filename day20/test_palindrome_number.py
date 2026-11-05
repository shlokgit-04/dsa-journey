from palindrome_number import Solution

s = Solution()


def test_positive():
    assert s.isPalindrome(121) is True


def test_negative():
    assert s.isPalindrome(-121) is False


def test_trailing_zero():
    assert s.isPalindrome(10) is False


def test_zero():
    assert s.isPalindrome(0) is True


def test_even_digits():
    assert s.isPalindrome(1221) is True


def test_odd_digits():
    assert s.isPalindrome(12321) is True


def test_not_palindrome():
    assert s.isPalindrome(1000021) is False
