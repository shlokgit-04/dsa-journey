"""LC 101 Symmetric Tree (Easy, Tree/DFS).

A tree is symmetric when its left and right subtrees are mirrors of
each other. Recurse in mirrored pairs: (a.left, b.right) and (a.right, b.left).
"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        def mirror(a: Optional[TreeNode], b: Optional[TreeNode]) -> bool:
            if a is None and b is None:
                return True
            if a is None or b is None or a.val != b.val:
                return False
            return mirror(a.left, b.right) and mirror(a.right, b.left)

        return mirror(root.left, root.right)
