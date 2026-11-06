from intersection_two_arrays import Solution


def test_basic():
    assert Solution().intersect([1, 2, 2, 1], [2, 2]) == [2, 2]


def test_multiple_overlap():
    assert sorted(Solution().intersect([4, 9, 5], [9, 4, 9, 8, 4])) == [4, 9]


def test_no_overlap():
    assert Solution().intersect([1, 2], [3, 4]) == []


def test_empty_one():
    assert Solution().intersect([], [1, 2]) == []


def test_respects_multiplicity():
    assert sorted(Solution().intersect([2, 2, 2], [2, 2])) == [2, 2]
