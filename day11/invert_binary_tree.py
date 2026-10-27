class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root

def tree_to_list(root):
    """Level-order serialization with None holes, trailing Nones trimmed."""
    out, queue = [], [root]
    while queue:
        node = queue.pop(0)
        if node:
            out.append(node.val)
            queue.extend([node.left, node.right])
        else:
            out.append(None)
    while out and out[-1] is None:
        out.pop()
    return out

def list_to_tree(vals):
    if not vals:
        return None
    root = TreeNode(vals[0])
    queue, i = [root], 1
    while queue and i < len(vals):
        node = queue.pop(0)
        if i < len(vals):
            node.left = TreeNode(vals[i]) if vals[i] is not None else None
            if node.left:
                queue.append(node.left)
            i += 1
        if i < len(vals):
            node.right = TreeNode(vals[i]) if vals[i] is not None else None
            if node.right:
                queue.append(node.right)
            i += 1
    return root
