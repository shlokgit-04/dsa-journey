import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from day34.jump_game import can_jump
from day34.longest_increasing_subsequence import length_of_lis, length_of_lis_dp
from day34.majority_element import majority_element_boyer_moore, majority_element_counter
from day34.min_cost_climbing_stairs import min_cost_climbing_stairs
from day34.house_robber import rob
from day34.pascals_triangle import generate
from day34.pascals_triangle_ii import get_row


def test_pascal_five_rows():
    assert generate(5) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]


def test_pascal_one_row():
    assert generate(1) == [[1]]


def test_pascal_row_zero_length():
    assert generate(0) == []


def test_pascal_row_extremes():
    assert get_row(0) == [1]
    assert get_row(1) == [1, 1]


def test_pascal_row_matches_triangle():
    triangle = generate(10)
    for i, row in enumerate(triangle):
        assert get_row(i) == row


def test_majority_examples():
    nums = [3, 2, 3]
    assert majority_element_boyer_moore(nums) == 3
    assert majority_element_counter(nums) == 3
    nums = [2, 2, 1, 1, 1, 2, 2]
    assert majority_element_boyer_moore(nums) == 2
    assert majority_element_counter(nums) == 2


def test_majority_single_and_all_same():
    assert majority_element_boyer_moore([7]) == 7
    assert majority_element_boyer_moore([5, 5, 5, 5]) == 5
    assert majority_element_counter([5, 5, 5, 5]) == 5


def test_rob_examples():
    assert rob([1, 2, 3, 1]) == 4
    assert rob([2, 7, 9, 3, 1]) == 12


def test_rob_edges():
    assert rob([]) == 0
    assert rob([5]) == 5
    assert rob([2, 1]) == 2
    assert rob([2, 1, 1, 2]) == 4


def test_min_cost_examples():
    assert min_cost_climbing_stairs([10, 15, 20]) == 15
    assert min_cost_climbing_stairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]) == 6


def test_min_cost_edges():
    assert min_cost_climbing_stairs([10, 20]) == 10
    assert min_cost_climbing_stairs([1, 2, 1]) == 2


def test_jump_game_examples():
    assert can_jump([2, 3, 1, 1, 4]) is True
    assert can_jump([3, 2, 1, 0, 4]) is False


def test_jump_game_edges():
    assert can_jump([0]) is True
    assert can_jump([1, 0]) is True
    assert can_jump([1, 0, 1]) is False
    assert can_jump([2, 0, 0]) is True


def test_lis_examples():
    assert length_of_lis([10, 9, 2, 5, 3, 7, 101, 18]) == 4
    assert length_of_lis([0, 1, 0, 3, 2, 3]) == 4
    assert length_of_lis([7, 7, 7, 7]) == 1


def test_lis_dp_matches_patience():
    cases = [[10, 9, 2, 5, 3, 7, 101, 18], [0, 1, 0, 3, 2, 3], [7, 7, 7], [1, 3, 6, 7, 9, 4, 10, 5, 6]]
    for nums in cases:
        assert length_of_lis_dp(nums) == length_of_lis(nums)
