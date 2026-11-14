# 226. Invert Binary Tree
# https://leetcode.com/problems/invert-binary-tree/
# Easy | Tree, DFS

from typing import Optional


class Solution:
    def invertTree(self, root: Optional["TreeNode"]) -> Optional["TreeNode"]:
        if root is None:
            return None
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root
