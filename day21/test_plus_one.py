from plus_one import Solution


def test_basic():
    assert Solution().plusOne([1, 2, 3]) == [1, 2, 4]


def test_carry_middle():
    assert Solution().plusOne([1, 9]) == [2, 0]


def test_all_nines():
    assert Solution().plusOne([9, 9, 9]) == [1, 0, 0, 0]


def test_zero():
    assert Solution().plusOne([0]) == [1]


def test_leading_chain():
    assert Solution().plusOne([8, 9, 9]) == [9, 0, 0]
