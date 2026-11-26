"""LC 700 Search in a Binary Search Tree: walk down the BST, no full search."""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        node = root
        while node and node.val != val:
            node = node.left if val < node.val else node.right
        return node
