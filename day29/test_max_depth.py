import os
import sys

sys.path.insert(0, os.path.dirname(__file__))

from tree_utils import TreeNode, build_tree
from max_depth import Solution


def t(vals):
    return build_tree(vals)


def test_none_root():
    assert Solution().maxDepth(None) == 0


def test_single_node():
    assert Solution().maxDepth(t([1])) == 1


def test_three_levels():
    assert Solution().maxDepth(t([3, 9, 20, None, None, 15, 7])) == 3


def test_skewed_left_chain():
    assert Solution().maxDepth(t([1, 2, None, 3, None, 4])) == 4


def test_two_nodes():
    assert Solution().maxDepth(t([1, 2])) == 2
