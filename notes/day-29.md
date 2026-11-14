# Day 29 - Sat, 14 Nov 2026

Set: binary tree DFS (LC 104, 226, 543, 100, 112) + 25 pytest cases in day29/.

- LC 104 Maximum Depth: classic recursion, `1 + max(left, right)`.
- LC 226 Invert Binary Tree: swap children recursively.
- LC 543 Diameter of Binary Tree: DFS returns height, tracks `left + right` best in an attribute.
- LC 100 Same Tree: compare value + both subtrees; short-circuit left/right into locals to keep lines readable.
- LC 112 Path Sum: subtract on the way down; leaf check is `left is None and right is None`.

Note: diameter/edge-count and invert preorder expectations had to be corrected in the tests
(solutions were right); the level-order builder treats None slots as real children positions.
