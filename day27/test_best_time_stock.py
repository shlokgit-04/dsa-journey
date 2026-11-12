from day27.best_time_stock import max_profit

def test_profit_basic():
    assert max_profit([7,1,5,3,6,4]) == 5

def test_no_profit():
    assert max_profit([7,6,4,3,1]) == 0

def test_single_price():
    assert max_profit([5]) == 0

def test_rising():
    assert max_profit([1,2,3,4,5]) == 4

def test_two_prices():
    assert max_profit([2,4]) == 2
