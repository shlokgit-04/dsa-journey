from day26.house_robber import Solution


def test_example_one():
    assert Solution().rob([1, 2, 3, 1]) == 4


def test_example_two():
    assert Solution().rob([2, 7, 9, 3, 1]) == 12


def test_single_house():
    assert Solution().rob([5]) == 5


def test_two_houses():
    assert Solution().rob([2, 3]) == 3


def test_all_equal():
    assert Solution().rob([4, 4, 4, 4]) == 8
