from top_k_frequent import Solution


def test_leetcode_example():
    assert sorted(Solution().topKFrequent([1, 1, 1, 2, 2, 3], 2)) == [1, 2]


def test_single_element():
    assert Solution().topKFrequent([5], 1) == [5]


def test_k_equals_unique():
    got = sorted(Solution().topKFrequent([1, 2, 3, 4], 4))
    assert got == [1, 2, 3, 4]


def test_negatives():
    assert sorted(Solution().topKFrequent([-1, -1, 2], 1)) == [-1]


def test_ties_return_k_items():
    got = Solution().topKFrequent([1, 2], 2)
    assert sorted(got) == [1, 2]
