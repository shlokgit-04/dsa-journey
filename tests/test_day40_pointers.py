import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "day40"))

from sort_colors import sort_colors
from is_subsequence import is_subsequence


def test_sort_colors_examples():
    a = [2, 0, 2, 1, 1, 0]
    sort_colors(a)
    assert a == [0, 0, 1, 1, 2, 2]
    b = [2, 0, 1]
    sort_colors(b)
    assert b == [0, 1, 2]


def test_sort_colors_edges():
    a = [0]
    sort_colors(a)
    assert a == [0]
    b = [1, 1, 1]
    sort_colors(b)
    assert b == [1, 1, 1]
    c = [2, 2, 0, 0]
    sort_colors(c)
    assert c == [0, 0, 2, 2]


def test_is_subsequence_examples():
    assert is_subsequence("abc", "ahbgdc") is True
    assert is_subsequence("axc", "ahbgdc") is False


def test_is_subsequence_edges():
    assert is_subsequence("", "ahbgdc") is True
    assert is_subsequence("a", "") is False
    assert is_subsequence("acb", "ahbgdc") is False
