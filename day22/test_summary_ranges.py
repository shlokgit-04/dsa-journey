from summary_ranges import Solution


def test_basic():
    assert Solution().summaryRanges([0, 1, 2, 4, 5, 7]) == ["0->2", "4->5", "7"]


def test_empty():
    assert Solution().summaryRanges([]) == []


def test_single():
    assert Solution().summaryRanges([5]) == ["5"]


def test_negative():
    assert Solution().summaryRanges([-1, 0, 3]) == ["-1->0", "3"]


def test_all_one_range():
    assert Solution().summaryRanges([1, 2, 3, 4]) == ["1->4"]
