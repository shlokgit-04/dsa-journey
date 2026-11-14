# 100. Same Tree
# https://leetcode.com/problems/same-tree/
# Easy | Tree, DFS

from typing import Optional


class Solution:
    def isSameTree(self, p: Optional["TreeNode"], q: Optional["TreeNode"]) -> bool:
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        same_left = self.isSameTree(p.left, q.left)
        same_right = self.isSameTree(p.right, q.right)
        return p.val == q.val and same_left and same_right
