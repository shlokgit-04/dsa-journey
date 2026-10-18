from day03.best_time_to_buy_and_sell_stock import max_profit


def test_examples():
    assert max_profit([7, 1, 5, 3, 6, 4]) == 5
    assert max_profit([7, 6, 4, 3, 1]) == 0


def test_edges():
    assert max_profit([1]) == 0
    assert max_profit([]) == 0
    assert max_profit([2, 4, 1]) == 2
    assert max_profit([1, 2]) == 1
    assert max_profit([3, 2, 6, 5, 0, 3]) == 4
