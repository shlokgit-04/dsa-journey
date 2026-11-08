# 404. Sum of Left Leaves
# https://leetcode.com/problems/sum-of-left-leaves/
# Easy | Tree, DFS

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        def dfs(node: TreeNode, is_left: bool) -> int:
            if not node:
                return 0
            if is_left and not node.left and not node.right:
                return node.val
            return dfs(node.left, True) + dfs(node.right, False)

        return dfs(root, False)


if __name__ == "__main__":
    #      3
    #     / \
    #    9  20
    #       / \
    #      15  7
    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    assert Solution().sumOfLeftLeaves(root) == 24
    print("ok")
