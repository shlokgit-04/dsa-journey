from contains_duplicate import contains_duplicate


def test_example_true():
    assert contains_duplicate([1, 2, 3, 1]) is True


def test_example_false():
    assert contains_duplicate([1, 2, 3, 4]) is False


def test_large_true():
    assert contains_duplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]) is True


def test_single():
    assert contains_duplicate([7]) is False


def test_empty():
    assert contains_duplicate([]) is False
