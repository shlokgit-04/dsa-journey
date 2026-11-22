from day37.best_time_buy_sell_stock import Solution as BuyStock
from day37.maximum_subarray import Solution as MaxSub


def test_lc121_basic():
    assert BuyStock().maxProfit([7, 1, 5, 3, 6, 4]) == 5


def test_lc121_no_profit():
    assert BuyStock().maxProfit([7, 6, 4, 3, 1]) == 0


def test_lc121_late_dip():
    assert BuyStock().maxProfit([2, 4, 1]) == 2


def test_lc53_classic():
    assert MaxSub().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6


def test_lc53_single():
    assert MaxSub().maxSubArray([1]) == 1


def test_lc53_all_positive():
    assert MaxSub().maxSubArray([5, 4, -1, 7, 8]) == 23
