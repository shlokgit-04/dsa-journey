from day28.reverse_string import Solution


def test_basic():
    a = ["h", "e", "l", "l", "o"]
    Solution().reverseString(a)
    assert a == ["o", "l", "l", "e", "h"]


def test_even_length():
    b = ["H", "a", "n", "n", "a", "h"]
    Solution().reverseString(b)
    assert b == ["h", "a", "n", "n", "a", "H"]


def test_single():
    c = ["x"]
    Solution().reverseString(c)
    assert c == ["x"]


def test_two():
    d = ["a", "b"]
    Solution().reverseString(d)
    assert d == ["b", "a"]


def test_palindrome_unchanged():
    e = ["a", "b", "a"]
    Solution().reverseString(e)
    assert e == ["a", "b", "a"]
