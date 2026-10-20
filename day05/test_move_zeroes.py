from day05.move_zeroes import move_zeroes


def test_examples():
    assert move_zeroes([0, 1, 0, 3, 12]) == [1, 3, 12, 0, 0]
    assert move_zeroes([0]) == [0]


def test_no_zeros():
    assert move_zeroes([1, 2, 3]) == [1, 2, 3]


def test_all_zeros_and_empty():
    assert move_zeroes([0, 0, 0]) == [0, 0, 0]
    assert move_zeroes([]) == []
