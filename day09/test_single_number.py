from single_number import single_number

def test_basic():
    assert single_number([2, 2, 1]) == 1

def test_second_position():
    assert single_number([4, 1, 2, 1, 2]) == 4

def test_single_element():
    assert single_number([1]) == 1
