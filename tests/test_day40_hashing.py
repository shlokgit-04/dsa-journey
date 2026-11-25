import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "day40"))

from intersection_two_arrays import intersection


def test_examples():
    assert sorted(intersection([1, 2, 2, 1], [2, 2])) == [2]
    assert sorted(intersection([4, 9, 5], [9, 4, 9, 8, 4])) == [4, 9]


def test_edges():
    assert intersection([1, 2, 3], [4, 5, 6]) == []
    assert intersection([], [1]) == []
