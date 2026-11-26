# Day 41 (Thu Nov 26, 2026) - trees + hashing + greedy

## LC 700 Search in a Binary Search Tree
- Walk down: while node and node.val != val, go left if val < node.val else right.
- Returns the matching subtree root (or None). O(h) time, O(1) space; no recursion stack needed.

## LC 219 Contains Duplicate II
- Value -> last seen index map; a repeat at distance <= k from the PREVIOUS index means true.
- Only the last index matters: if a farther one can't fit within k, an older one can't either, so one overwrite per value is enough.

## LC 455 Assign Cookies
- Sort both greed lists; walk cookie sizes in order, hand each cookie to the smallest still-unfed child it satisfies.
- Pointers: child index only moves forward when a cookie fits; a cookie too small for the smallest remaining child is skipped forever (it fits nobody larger).
