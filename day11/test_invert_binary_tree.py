from invert_binary_tree import Solution, list_to_tree, tree_to_list

def test_example():
    root = list_to_tree([4, 2, 7, 1, 3, 6, 9])
    assert tree_to_list(Solution().invertTree(root)) == [4, 7, 2, 9, 6, 3, 1]

def test_empty():
    assert Solution().invertTree(None) is None

def test_single():
    assert tree_to_list(Solution().invertTree(list_to_tree([1]))) == [1]

def test_unbalanced():
    root = list_to_tree([1, 2])
    assert tree_to_list(Solution().invertTree(root)) == [1, None, 2]
