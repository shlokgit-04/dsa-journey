from day18.valid_anagram import is_anagram


def test_examples():
    assert is_anagram("anagram", "nagaram") is True
    assert is_anagram("rat", "car") is False


def test_lengths_differ():
    assert is_anagram("a", "ab") is False
    assert is_anagram("ab", "a") is False


def test_same_string():
    assert is_anagram("abc", "abc") is True


def test_repeats():
    assert is_anagram("aacc", "ccac") is False
    assert is_anagram("aacc", "ccaa") is True
