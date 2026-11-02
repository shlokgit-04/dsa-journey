# Day 16 - Nov 1, 2026 (Sunday)

## Problems
- LC 283 Move Zeroes - two pointers, in-place partition
- LC 20 Valid Parentheses - stack with a closing-bracket table
- LC 110 Balanced Binary Tree - bottom-up height DFS with a -1 prune

## Approach notes
- Move Zeroes: slow pointer marks where the next non-zero lands, fast
  pointer scans. One swap per non-zero keeps original order. O(n) time,
  O(1) space, single pass.
- Valid Parentheses: push openers, on a closer pop and compare against
  the expected opener. Empty stack at the end means valid. Gotcha: a
  closer on an empty stack is invalid, and leftovers are invalid too.
- Balanced Binary Tree: naive top-down recounting is O(n^2). Bottom-up
  DFS returns height, or -1 the moment any subtree is unbalanced, which
  short-circuits the whole check. O(n) time, O(h) stack.

## Complexity summary
| Problem | Time | Space |
| --- | --- | --- |
| Move Zeroes | O(n) | O(1) |
| Valid Parentheses | O(n) | O(n) |
| Balanced Binary Tree | O(n) | O(h) |

15 pytest tests green.
