"""LC 110 Balanced Binary Tree (top-down height check)."""
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_balanced(root: Optional[TreeNode]) -> bool:
    """Return True when no node's two subtree heights differ by more than 1.

    Bottom-up DFS: each node returns its height, or -1 once a subtree is
    already unbalanced, so every node is visited once.
    """
    def height(node):
        if node is None:
            return 0
        lh = height(node.left)
        if lh == -1:
            return -1
        rh = height(node.right)
        if rh == -1 or abs(lh - rh) > 1:
            return -1
        return 1 + max(lh, rh)

    return height(root) != -1


def to_tree(values):
    """Build a level-order tree, LeetCode style: nulls are skipped."""
    if not values:
        return None
    it = iter(values)
    root = TreeNode(next(it))
    q = deque([root])
    while q:
        node = q.popleft()
        try:
            v = next(it)
        except StopIteration:
            break
        if v is not None:
            node.left = TreeNode(v)
            q.append(node.left)
        try:
            v = next(it)
        except StopIteration:
            break
        if v is not None:
            node.right = TreeNode(v)
            q.append(node.right)
    return root
