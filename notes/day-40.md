# Day 40 - Wed Nov 25, 2026 (two pointers + sliding window + hashing + trees + DP)

Six problems across the pointer/window/tree/DP families. The running theme:
ordered structure is free information, and a queue or a count array is
usually a smaller idea than the "real" algorithm looks.

## LC 75 - Sort Colors
Dutch national flag in one pass. Three regions: low owns 0s, high owns 2s,
mid scans. The subtle part is NOT advancing mid after swapping a 2 inward -
the swapped-in value from the back still needs checking, while a 0 from the
front is already handled.

## LC 392 - Is Subsequence
Greedy pointer walk is optimal when s is fixed. Early exit the moment the
subsequence pointer reaches len(s), so a long tail of t costs nothing.

## LC 567 - Permutation in String
Fixed window = sliding window with a constant length, the easy variant.
One 26-slot count array for the target, one for the current window, compare
only when the window is exactly len(s1) wide. "adc" in "dcda" is the trap:
the permutation hides in the middle, not at either end.

## LC 349 - Intersection of Two Arrays
Set the bigger array, dedupe hits from the other with a set comprehension.
Order does not matter per the problem, so returning a list of a set is fine.

## LC 102 - Level Order Traversal
BFS with a size snapshot: len(q) each round is exactly one level. Children
pushed during the drain join the NEXT level, never the current one.

## LC 62 - Unique Paths
The cell value only depends on top + left, so one rolling row over n
columns is enough. First row stays 1 forever - single path along the edge.

Test count: 26 assertions across 4 pytest files, all passing locally.
