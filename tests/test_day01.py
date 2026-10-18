from day01.two_sum import two_sum


def test_basic_case():
    i, j = two_sum([2, 7, 11, 15], 9)
    assert sorted([i, j]) == [0, 1]


def test_later_indices():
    i, j = two_sum([3, 2, 4], 6)
    assert sorted([i, j]) == [1, 2]


def test_duplicates():
    i, j = two_sum([3, 3], 6)
    assert sorted([i, j]) == [0, 1]


def test_no_answer():
    assert two_sum([1, 2], 99) == []
