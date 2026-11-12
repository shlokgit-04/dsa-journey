from day27.contains_duplicate import contains_duplicate

def test_has_dup():
    assert contains_duplicate([1,2,3,1]) is True

def test_no_dup():
    assert contains_duplicate([1,2,3,4]) is False

def test_empty():
    assert contains_duplicate([]) is False

def test_single():
    assert contains_duplicate([9]) is False

def test_negative_dup():
    assert contains_duplicate([-1,-1]) is True
