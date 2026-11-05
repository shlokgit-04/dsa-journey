from search_insert_position import Solution

s = Solution()


def test_middle():
    assert s.searchInsert([1, 3, 5, 6], 2) == 1


def test_end():
    assert s.searchInsert([1, 3, 5, 6], 7) == 4


def test_front():
    assert s.searchInsert([1, 3, 5, 6], 0) == 0


def test_exact():
    assert s.searchInsert([1, 3, 5, 6], 5) == 2


def test_single_low():
    assert s.searchInsert([1], 0) == 0


def test_single_high():
    assert s.searchInsert([1], 2) == 1
