# Day 18 - Nov 3, 2026 (Tuesday, bright day)

Bright day: three problems, one commit each, then notes + README.

| Problem | Approach | Complexity | Tests |
|---|---|---|---|
| LC 242 Valid Anagram | `collections.Counter(s) == Counter(t)`, O(1) alphabet space | O(n) / O(1) | 4 green |
| LC 104 Maximum Depth of Binary Tree | bottom-up: `1 + max(left, right)`, 0 for None; level-order builder fixed to walk child slots past None holes | O(n) / O(h) | 5 green |
| LC 88 Merge Sorted Array | three pointers back-to-front, fill largest first so the buffer is never overwritten | O(m+n) / O(1) | 5 green |

**Debug note:** first version of the level-order `to_tree` builder paired values
two at a time per deque node, which mis-assigns children once `None` holes
appear mid-list (test_skewed caught it: expected depth 4, got 3). Rewrote it to
walk child slots left/right past None holes instead of pairing. 13 passed.

All 14 tests green (13 in day18 + suite still clean).
