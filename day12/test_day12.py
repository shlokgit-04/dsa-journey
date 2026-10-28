import pytest

from day12.best_time_to_buy_sell_stock import max_profit
from day12.binary_search import search


@pytest.mark.parametrize(
    "prices, expected",
    [
        ([7, 1, 5, 3, 6, 4], 5),
        ([7, 6, 4, 3, 1], 0),
        ([1], 0),
        ([2, 4, 1], 2),
        ([1, 2], 1),
        ([2, 1, 2, 1, 0, 1, 2], 2),
        ([], 0),
    ],
)
def test_max_profit(prices, expected):
    assert max_profit(prices) == expected


@pytest.mark.parametrize(
    "nums, target, expected",
    [
        ([-1, 0, 3, 5, 9, 12], 9, 4),
        ([-1, 0, 3, 5, 9, 12], 2, -1),
        ([5], 5, 0),
        ([5], -5, -1),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9], 1, 0),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9], 9, 8),
        ([], 0, -1),
    ],
)
def test_search(nums, target, expected):
    assert search(nums, target) == expected
