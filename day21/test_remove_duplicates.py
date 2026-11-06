from remove_duplicates import Solution


def test_basic():
    nums = [0, 0, 1, 1, 1, 2, 2]
    k = Solution().removeDuplicates(nums)
    assert k == 3 and nums[:k] == [0, 1, 2]


def test_single():
    nums = [7]
    k = Solution().removeDuplicates(nums)
    assert k == 1 and nums[:k] == [7]


def test_empty():
    assert Solution().removeDuplicates([]) == 0


def test_no_duplicates():
    nums = [1, 2, 3]
    k = Solution().removeDuplicates(nums)
    assert k == 3 and nums[:k] == [1, 2, 3]


def test_all_same():
    nums = [5, 5, 5, 5]
    k = Solution().removeDuplicates(nums)
    assert k == 1 and nums[:k] == [5]
