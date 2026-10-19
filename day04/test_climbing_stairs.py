from day04.climbing_stairs import climb_stairs


def test_base_cases():
    assert climb_stairs(1) == 1
    assert climb_stairs(2) == 2


def test_examples():
    assert climb_stairs(3) == 3
    assert climb_stairs(4) == 5


def test_large_n():
    assert climb_stairs(10) == 89
    assert climb_stairs(35) == 14930352
