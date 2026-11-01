from day16.balanced_binary_tree import is_balanced, to_tree


def test_empty():
    assert is_balanced(to_tree([])) is True


def test_single():
    assert is_balanced(to_tree([1])) is True


def test_balanced_two_levels():
    assert is_balanced(to_tree([3, 9, 20])) is True


def test_balanced_three_levels():
    assert is_balanced(to_tree([3, 9, 20, None, None, 15, 7])) is True


def test_unbalanced_chain():
    assert is_balanced(to_tree([1, 2, 2, 3, 3, None, None, 4, 4])) is False
