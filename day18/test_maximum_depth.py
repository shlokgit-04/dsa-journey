from day18.maximum_depth import max_depth, to_tree


def test_examples():
    assert max_depth(to_tree([3, 9, 20, None, None, 15, 7])) == 3
    assert max_depth(to_tree([1, None, 2])) == 2


def test_empty():
    assert max_depth(None) == 0


def test_single_node():
    assert max_depth(to_tree([0])) == 1


def test_skewed():
    assert max_depth(to_tree([1, 2, None, 3, None, 4])) == 4
    assert max_depth(to_tree([1, None, 2, None, 3])) == 3
