import os
import sys

sys.path.insert(0, os.path.dirname(__file__))

from tree_utils import TreeNode, build_tree
from invert_tree import Solution


def preorder(root):
    if root is None:
        return []
    out = [root.val]
    out += preorder(root.left)
    out += preorder(root.right)
    return out


def test_none():
    assert Solution().invertTree(None) is None


def test_single():
    assert preorder(Solution().invertTree(build_tree([1]))) == [1]


def test_three_levels():
    root = Solution().invertTree(build_tree([4, 2, 7, 1, 3, 6, 9]))
    assert preorder(root) == [4, 7, 9, 6, 2, 3, 1]


def test_skewed_becomes_other_side():
    root = Solution().invertTree(build_tree([1, 2, None, 3, None, 4]))
    assert preorder(root) == [1, 2, 3, 4]


def test_two_nodes():
    root = Solution().invertTree(build_tree([1, 2]))
    assert root.left is None and root.right.val == 2
