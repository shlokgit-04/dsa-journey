from day28.move_zeroes import Solution


def test_example():
    a = [0, 1, 0, 3, 12]
    Solution().moveZeroes(a)
    assert a == [1, 3, 12, 0, 0]


def test_all_zero():
    b = [0, 0]
    Solution().moveZeroes(b)
    assert b == [0, 0]


def test_no_zero():
    c = [1, 2, 3]
    Solution().moveZeroes(c)
    assert c == [1, 2, 3]


def test_single_zero():
    d = [0]
    Solution().moveZeroes(d)
    assert d == [0]


def test_trailing_zero():
    e = [1, 0]
    Solution().moveZeroes(e)
    assert e == [1, 0]
