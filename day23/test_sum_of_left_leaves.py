from sum_of_left_leaves import TreeNode, Solution


def tree(vals):
    if not vals:
        return None
    nodes = [None] + [TreeNode(v) if v is not None else None for v in vals]
    for i in range(1, len(vals) // 2 + 1):
        node = nodes[i]
        if node:
            node.left = nodes[2 * i] if 2 * i <= len(vals) else None
            node.right = nodes[2 * i + 1] if 2 * i + 1 <= len(vals) else None
    return nodes[1]


def test_leetcode_example():
    root = tree([3, 9, 20, None, None, 15, 7])
    assert Solution().sumOfLeftLeaves(root) == 24


def test_single_node():
    assert Solution().sumOfLeftLeaves(TreeNode(1)) == 0


def test_only_right_chain():
    root = TreeNode(1, None, TreeNode(2, None, TreeNode(3)))
    assert Solution().sumOfLeftLeaves(root) == 0


def test_deep_left_leaf():
    root = TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4))))
    assert Solution().sumOfLeftLeaves(root) == 4


def test_mixed():
    root = tree([1, 2, 3, 4, 5])
    assert Solution().sumOfLeftLeaves(root) == 4
