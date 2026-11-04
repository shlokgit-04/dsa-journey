from day19.symmetric_tree import Solution, TreeNode


def tree(vals):
    nodes = [TreeNode(v) if v is not None else None for v in vals]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node is not None:
            if kids:
                node.left = kids.pop()
            if kids:
                node.right = kids.pop()
    return root


def test_example():
    assert Solution().isSymmetric(tree([1, 2, 2, 3, 4, 4, 3])) is True


def test_not_symmetric():
    assert Solution().isSymmetric(tree([1, 2, 2, None, 3, None, 3])) is False


def test_single():
    assert Solution().isSymmetric(TreeNode(1)) is True


def test_empty():
    assert Solution().isSymmetric(None) is True
