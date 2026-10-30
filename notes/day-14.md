# Day 14 (Oct 30): Strings, Linked Lists, DP

## Longest Common Prefix (LC 14)
Horizontal scan: keep the first string as the prefix candidate, then for every
other string shrink it to the length of the matching head. Early exit when the
prefix collapses to empty. O(S) over all characters.

## Linked List Cycle (LC 141)
Floyd's tortoise and hare. Slow moves one step, fast two; if they ever meet
there is a cycle. A fast pointer that reaches None means no cycle. O(n) time,
O(1) space.

## House Robber (LC 198)
Two rolling values: best if we take this house, best if we skip it. Taking
means skip + value; skipping means max of the previous two. O(n) time, O(1)
space.
