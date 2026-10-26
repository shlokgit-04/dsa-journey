from day10.reverse_string import reverse_string


def test_basic():
    s = ["h", "e", "l", "l", "o"]
    assert reverse_string(s) == ["o", "l", "l", "e", "h"]


def test_even_len():
    assert reverse_string(["a", "b"]) == ["b", "a"]


def test_single():
    assert reverse_string(["z"]) == ["z"]
