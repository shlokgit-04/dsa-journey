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


from day37.climbing_stairs import Solution as Climb
from day37.binary_search import Solution as BinSearch


def test_lc70_base():
    assert Climb().climbStairs(1) == 1
    assert Climb().climbStairs(2) == 2


def test_lc70_known_values():
    assert Climb().climbStairs(3) == 3
    assert Climb().climbStairs(10) == 89


def test_lc704_found():
    assert BinSearch().search([-1, 0, 3, 5, 9, 12], 9) == 4
    assert BinSearch().search([5], 5) == 0


def test_lc704_missing():
    assert BinSearch().search([-1, 0, 3, 5, 9, 12], 2) == -1
    assert BinSearch().search([5], -5) == -1
