from day27.majority_element import majority_element

def test_basic():
    assert majority_element([3,2,3]) == 3

def test_half_plus():
    assert majority_element([2,2,1,1,1,2,2]) == 2

def test_single():
    assert majority_element([1]) == 1

def test_all_same():
    assert majority_element([7,7,7,7]) == 7

def test_pair():
    assert majority_element([9,9]) == 9
