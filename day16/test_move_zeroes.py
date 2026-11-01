from day16.move_zeroes import move_zeroes


def test_basic():
    assert move_zeroes([0, 1, 0, 3, 12]) == [1, 3, 12, 0, 0]


def test_all_zero():
    assert move_zeroes([0, 0]) == [0, 0]


def test_no_zero():
    assert move_zeroes([1, 2, 3]) == [1, 2, 3]


def test_leading_zero():
    assert move_zeroes([0]) == [0]


def test_mixed_tail():
    assert move_zeroes([2, 0, 1, 0, 5]) == [2, 1, 5, 0, 0]
