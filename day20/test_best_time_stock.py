from best_time_stock import Solution

s = Solution()


def test_example():
    assert s.maxProfit([7, 1, 5, 3, 6, 4]) == 5


def test_no_profit():
    assert s.maxProfit([7, 6, 4, 3, 1]) == 0


def test_single():
    assert s.maxProfit([1]) == 0


def test_empty():
    assert s.maxProfit([]) == 0


def test_valley():
    assert s.maxProfit([2, 4, 1]) == 2


def test_late_valley():
    assert s.maxProfit([3, 2, 6, 5, 0, 3]) == 4
