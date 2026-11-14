import os
import sys

sys.path.insert(0, os.path.dirname(__file__))

from tree_utils import build_tree
from same_tree import Solution


def test_both_empty():
    assert Solution().isSameTree(None, None) is True


def test_one_empty():
    assert Solution().isSameTree(build_tree([1]), None) is False


def test_identical():
    assert (
        Solution().isSameTree(build_tree([1, 2, 3]), build_tree([1, 2, 3])) is True
    )


def test_different_values():
    assert (
        Solution().isSameTree(build_tree([1, 2]), build_tree([1, 3])) is False
    )


def test_different_shape():
    assert (
        Solution().isSameTree(build_tree([1, 2]), build_tree([1, None, 2])) is False
    )
