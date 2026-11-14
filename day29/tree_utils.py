# Shared tree helpers for day 29 (binary tree problems)

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(values: List[Optional[int]]) -> Optional[TreeNode]:
    """Build a level-order binary tree from a list (None = missing node)."""
    if not values:
        return None
    nodes = [None if v is None else TreeNode(v) for v in values]
    kids = nodes[1:]
    root = nodes[0]
    queue = [root]
    i = 0
    while queue and i < len(kids):
        node = queue.pop(0)
        if node is None:
            continue
        if i < len(kids):
            node.left = kids[i]
            i += 1
        if i < len(kids):
            node.right = kids[i]
            i += 1
        queue.append(node.left)
        queue.append(node.right)
    return root
