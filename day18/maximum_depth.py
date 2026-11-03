"""LC 104 Maximum Depth of Binary Tree - bottom-up DFS.

Depth of a node = 1 + max(depth of children); empty tree is 0.
O(n) time, O(h) recursion stack.
"""
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def max_depth(root: TreeNode | None) -> int:
    if root is None:
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))


def to_tree(values):
    """Build a tree from a LeetCode-style level-order list with None holes."""
    if not values:
        return None
    nodes = [TreeNode(v) if v is not None else None for v in values]
    kids = iter(nodes[1:])
    for node in nodes:
        if node is None:
            continue
        for attr in ("left", "right"):
            child = next(kids, None)
            if child is not None:
                setattr(node, attr, child)
    return nodes[0]
