from .palindrome_number import is_palindrome


def test_examples():
    assert is_palindrome(121) is True
    assert is_palindrome(-121) is False
    assert is_palindrome(10) is False

def test_zero_and_single_digits():
    assert is_palindrome(0) is True
    assert is_palindrome(7) is True
    assert is_palindrome(9) is True

def test_edge_ints():
    assert is_palindrome(-2**31) is False
    assert is_palindrome(2**31 - 1) is False

def test_multi_digit():
    assert is_palindrome(12321) is True
    assert is_palindrome(1231) is False
