from day08.missing_number import missing_number

def test_basic():
    assert missing_number([3, 0, 1]) == 2

def test_missing_zero():
    assert missing_number([1, 2, 3]) == 0

def test_missing_last():
    assert missing_number([0, 1]) == 2
