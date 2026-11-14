# 543. Diameter of Binary Tree
# https://leetcode.com/problems/diameter-of-binary-tree/
# Easy | Tree, DFS

from typing import Optional


class Solution:
    def diameterOfBinaryTree(self, root: Optional["TreeNode"]) -> int:
        self.best = 0

        def depth(node):
            if node is None:
                return 0
            left = depth(node.left)
            right = depth(node.right)
            self.best = max(self.best, left + right)
            return 1 + max(left, right)

        depth(root)
        return self.best
