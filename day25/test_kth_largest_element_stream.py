from kth_largest_element_stream import KthLargest


def test_leetcode_example():
    k = KthLargest(3, [4, 5, 8, 2])
    assert k.add(3) == 4
    assert k.add(5) == 5
    assert k.add(10) == 5
    assert k.add(9) == 8
    assert k.add(4) == 8


def test_start_empty_negative():
    k = KthLargest(1, [])
    assert k.add(-3) == -3
    assert k.add(-2) == -2
    assert k.add(-4) == -2
    assert k.add(0) == 0
    assert k.add(4) == 4


def test_duplicates():
    k = KthLargest(2, [0])
    assert k.add(-1) == -1
    assert k.add(1) == 0


def test_larger_k():
    k = KthLargest(3, [1, 2, 3, 4, 5])
    assert k.add(6) == 4


def test_negatives():
    k = KthLargest(2, [-5, -1])
    assert k.add(-3) == -3
