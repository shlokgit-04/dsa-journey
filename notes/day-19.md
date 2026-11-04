# Day 19 - Nov 4, 2026 (Wednesday dark day)

Six problems, one commit each plus a test-file commit each. 22 tests green.

| LC | Problem | Topic | Approach |
|----|---------|-------|----------|
| 226 | Invert Binary Tree | Tree/DFS | recursive subtree swap |
| 101 | Symmetric Tree | Tree/DFS | mirrored-pair DFS (a.left vs b.right) |
| 70 | Climbing Stairs | DP | rolling Fibonacci, two variables |
| 344 | Reverse String | Two Pointers | in-place end swap, pointers meet |
| 125 | Valid Palindrome | Two Pointers | skip non-alnum, compare lowercased ends |
| 13 | Roman to Integer | Hash Table | symbol map, subtract when smaller precedes larger |

## Takeaways
- Symmetric tree is just invert-check done pairwise; mirror(a, b) compares
  crossed children, which also covers the None-vs-value mismatch case.
- Roman numerals: subtracting the current symbol when the next one is
  bigger avoids enumerating the six special pairs.
- In-place reverse keeps O(1) memory; the LeetCode version mutates the
  list and returns nothing.
