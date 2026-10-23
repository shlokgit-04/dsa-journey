from day08.ransom_note import can_construct

def test_false():
    assert can_construct("a", "b") is False

def test_true():
    assert can_construct("aa", "aab") is True

def test_exact():
    assert can_construct("abc", "cba") is True
