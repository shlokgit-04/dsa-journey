"""LC 100 Same Tree (Easy) - trees.

Two trees are the same when every node matches in value and in both
children. Recurse down both at once. O(n) time, O(h) stack.
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p, q):
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


if __name__ == "__main__":
    t1 = TreeNode(1, TreeNode(2), TreeNode(3))
    t2 = TreeNode(1, TreeNode(2), TreeNode(3))
    t3 = TreeNode(1, TreeNode(2), None)
    assert Solution().isSameTree(t1, t2) is True
    assert Solution().isSameTree(t1, t3) is False
    assert Solution().isSameTree(None, None) is True
    print("ok")
