import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from day33.three_sum import Solution as TS
from day33.product_except_self import Solution as PS
from day33.backspace_compare import Solution as BS


def test_three_sum_basic():
    assert TS().threeSum([-1, 0, 1, 2, -1, -4]) == [[-1, -1, 2], [-1, 0, 1]]


def test_three_sum_no_triple():
    assert TS().threeSum([0, 1, 1]) == []


def test_three_sum_all_zero():
    assert TS().threeSum([0, 0, 0, 0]) == [[0, 0, 0]]


def test_three_sum_empty():
    assert TS().threeSum([]) == []


def test_three_sum_skips_duplicate_anchors():
    assert TS().threeSum([-2, 0, 0, 2, 2]) == [[-2, 0, 2]]


def test_product_except_self_basic():
    assert PS().productExceptSelf([1, 2, 3, 4]) == [24, 12, 8, 6]


def test_product_except_self_with_zero():
    assert PS().productExceptSelf([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]


def test_product_except_self_two():
    assert PS().productExceptSelf([2, 3]) == [3, 2]


def test_backspace_compare_equal():
    assert BS().backspaceCompare("ab#c", "ad#c") is True


def test_backspace_compare_unequal():
    assert BS().backspaceCompare("ab##", "c#d#") is True


def test_backspace_compare_both_empty():
    assert BS().backspaceCompare("a#c", "b") is False


def test_backspace_compare_trailing_hashes():
    assert BS().backspaceCompare("bxj##tw", "bxo#j##tw") is True
