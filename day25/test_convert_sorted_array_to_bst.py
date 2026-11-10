from convert_sorted_array_to_bst import Solution, TreeNode


def inorder(node):
    if not node:
        return []
    return inorder(node.left) + [node.val] + inorder(node.right)


def test_leetcode_example():
    root = Solution().sortedArrayToBST([-10, -3, 0, 5, 9])
    assert inorder(root) == [-10, -3, 0, 5, 9]
    assert root.val == 0


def test_two_elements():
    root = Solution().sortedArrayToBST([1, 3])
    assert inorder(root) == [1, 3]
    assert root.val in (1, 3)


def test_single_element():
    root = Solution().sortedArrayToBST([1])
    assert root.val == 1
    assert root.left is None and root.right is None


def test_seven_elements_balanced():
    root = Solution().sortedArrayToBST([-5, -3, -1, 0, 2, 4, 6])
    assert root.val == 0
    assert inorder(root) == [-5, -3, -1, 0, 2, 4, 6]
    assert root.left.val == -3 and root.right.val == 4


def test_empty_returns_none():
    assert Solution().sortedArrayToBST([]) is None
