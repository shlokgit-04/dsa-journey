import os
import sys

sys.path.insert(0, os.path.dirname(__file__))

from tree_utils import build_tree
from diameter_of_binary_tree import Solution


def test_none():
    assert Solution().diameterOfBinaryTree(None) == 0


def test_single():
    assert Solution().diameterOfBinaryTree(build_tree([1])) == 0


def test_three_levels():
    assert Solution().diameterOfBinaryTree(build_tree([1, 2, 3, 4, 5])) == 3


def test_long_chain():
    assert Solution().diameterOfBinaryTree(build_tree([1, 2, None, 3, None, 4])) == 3


def test_unbalanced():
    assert Solution().diameterOfBinaryTree(build_tree([1, 2, 3, 4, None, None, 5, 6])) == 5
