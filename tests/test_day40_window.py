import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "day40"))

from permutation_in_string import check_inclusion


def test_examples():
    assert check_inclusion("ab", "eidbaooo") is True
    assert check_inclusion("ab", "eidboaoo") is False


def test_edges():
    assert check_inclusion("a", "a") is True
    assert check_inclusion("adc", "dcda") is True
    assert check_inclusion("hello", "ooolleoooleh") is False
    assert check_inclusion("abc", "ab") is False
