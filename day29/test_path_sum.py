import os
import sys

sys.path.insert(0, os.path.dirname(__file__))

from tree_utils import build_tree
from path_sum import Solution


def test_empty_root():
    assert Solution().hasPathSum(None, 0) is False


def test_single_match():
    assert Solution().hasPathSum(build_tree([5]), 5) is True


def test_single_no_match():
    assert Solution().hasPathSum(build_tree([5]), 7) is False


def test_leetcode_example():
    assert Solution().hasPathSum(build_tree([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1]), 22) is True


def test_no_path_matches():
    assert Solution().hasPathSum(build_tree([1, 2, 3]), 5) is False
