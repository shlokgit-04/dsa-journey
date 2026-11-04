from day19.invert_binary_tree import Solution, to_tree, level_order


def test_example():
    # [4,2,7,1,3,6,9] -> [4,7,2,9,6,3,1]
    root = to_tree([4, 2, 7, 1, 3, 6, 9])
    out = Solution().invertTree(root)
    assert level_order(out) == [4, 7, 2, 9, 6, 3, 1]


def test_single():
    root = to_tree([1])
    out = Solution().invertTree(root)
    assert level_order(out) == [1]


def test_empty():
    assert Solution().invertTree(None) is None


def test_two_levels():
    # [1,2] -> [1,None,2]
    root = to_tree([1, 2])
    out = Solution().invertTree(root)
    assert level_order(out) == [1, None, 2]
