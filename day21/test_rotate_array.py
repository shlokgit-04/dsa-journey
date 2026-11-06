from rotate_array import Solution


def test_basic():
    nums = [1, 2, 3, 4, 5, 6, 7]
    Solution().rotate(nums, 3)
    assert nums == [5, 6, 7, 1, 2, 3, 4]


def test_k_equals_n():
    nums = [1, 2, 3]
    Solution().rotate(nums, 3)
    assert nums == [1, 2, 3]


def test_k_greater_than_n():
    nums = [1, 2]
    Solution().rotate(nums, 5)
    assert nums == [2, 1]


def test_single():
    nums = [9]
    Solution().rotate(nums, 100)
    assert nums == [9]


def test_k_zero():
    nums = [1, 2, 3]
    Solution().rotate(nums, 0)
    assert nums == [1, 2, 3]
