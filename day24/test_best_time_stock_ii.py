from best_time_stock_ii import Solution


def test_leetcode_example():
    assert Solution().maxProfit([7, 1, 5, 3, 6, 4]) == 7


def test_strictly_rising():
    assert Solution().maxProfit([1, 2, 3, 4, 5]) == 4


def test_strictly_falling():
    assert Solution().maxProfit([7, 6, 4, 3, 1]) == 0


def test_single():
    assert Solution().maxProfit([5]) == 0


def test_flat():
    assert Solution().maxProfit([3, 3, 3]) == 0
