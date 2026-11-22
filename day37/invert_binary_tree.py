"""LC 226 Invert Binary Tree (Easy) - trees.

Swap every node's left and right child, recursively.
O(n) time (every node visited once), O(h) recursion stack.
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root):
        if not root:
            return None
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root


if __name__ == "__main__":
    #      4              4
    #     / \            / \
    #    2   7   ->     7   2
    #   / \ / \        / \ / \
    #  1  3 6  9      9  6 3  1
    root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7, TreeNode(6), TreeNode(9)))
    out = Solution().invertTree(root)
    assert out.val == 4 and out.left.val == 7 and out.right.val == 2
    assert out.left.left.val == 9 and out.left.right.val == 6
    assert Solution().invertTree(None) is None
    print("ok")
