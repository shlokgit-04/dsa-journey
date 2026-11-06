from remove_element import Solution


def test_basic():
    nums = [3, 2, 2, 3]
    k = Solution().removeElement(nums, 3)
    assert k == 2
    assert sorted(nums[:k]) == [2, 2]


def test_no_match():
    nums = [1, 2, 3]
    k = Solution().removeElement(nums, 9)
    assert k == 3 and nums[:k] == [1, 2, 3]


def test_all_match():
    nums = [4, 4, 4]
    k = Solution().removeElement(nums, 4)
    assert k == 0


def test_empty():
    assert Solution().removeElement([], 1) == 0


def test_keeps_order():
    nums = [0, 1, 2, 2, 3, 0, 4, 2]
    k = Solution().removeElement(nums, 2)
    assert k == 5
    assert nums[:k] == [0, 1, 3, 0, 4]
