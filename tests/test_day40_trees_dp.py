import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "day40"))

from level_order import TreeNode, level_order
from unique_paths import unique_paths


def test_level_order_examples():
    #      3
    #     / \
    #    9  20
    #       / \
    #      15  7
    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    assert level_order(root) == [[3], [9, 20], [15, 7]]


def test_level_order_edges():
    assert level_order(None) == []
    assert level_order(TreeNode(1)) == [[1]]


def test_unique_paths_examples():
    assert unique_paths(3, 7) == 28
    assert unique_paths(3, 2) == 3


def test_unique_paths_edges():
    assert unique_paths(1, 1) == 1
    assert unique_paths(2, 2) == 2
