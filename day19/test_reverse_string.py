from day19.reverse_string import Solution


def test_example():
    s = ["h", "e", "l", "l", "o"]
    Solution().reverseString(s)
    assert s == ["o", "l", "l", "e", "h"]


def test_even_length():
    s = ["H", "a", "n", "n", "a", "h"]
    Solution().reverseString(s)
    assert s == ["h", "a", "n", "n", "a", "H"]


def test_single():
    s = ["x"]
    Solution().reverseString(s)
    assert s == ["x"]


def test_two():
    s = ["a", "b"]
    Solution().reverseString(s)
    assert s == ["b", "a"]
