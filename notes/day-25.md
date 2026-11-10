# Day 25 - Nov 10, 2026 (Tuesday)

## LC 387 First Unique Character in a String (Easy, strings/hashing)
Two passes over the string. First pass counts every character in a dict,
second pass walks the string and returns the first index whose count is 1.
O(n) time, O(1) extra space (26 lowercase letters max).

## LC 703 Kth Largest Element in a Stream (Easy, heap/design)
Keep a min-heap of size k: the root is always the kth largest. Heapify the
initial list, pop down to size k. Every add pushes then pops back to size k.
Answer is heap[0]. O(log k) per add.

## LC 108 Convert Sorted Array to BST (Easy, trees)
Sorted array -> height-balanced BST: pick the middle element as the root,
recursively build left half and right half. Mid = len // 2 gives the left
side the extra element when length is even (LeetCode accepts either).
