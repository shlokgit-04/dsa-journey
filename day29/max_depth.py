# 104. Maximum Depth of Binary Tree
# https://leetcode.com/problems/maximum-depth-of-binary-tree/
# Easy | Tree, DFS

from typing import Optional


class Solution:
    def maxDepth(self, root: Optional["TreeNode"]) -> int:
        if root is None:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
