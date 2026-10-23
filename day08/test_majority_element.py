from day08.majority_element import majority_element

def test_basic():
    assert majority_element([3, 2, 3]) == 3

def test_bigger():
    assert majority_element([2, 2, 1, 1, 1, 2, 2]) == 2

def test_single():
    assert majority_element([1]) == 1
