# Day 5 - Move Zeroes

Two pointers, one pass to compact non-zeros, one pass to zero the tail.
The read pointer scans; the write pointer marks where the next non-zero
belongs. Order of non-zeros is preserved because reads overtake writes.

Complexity: O(n) time, O(1) extra space, in-place.

Edge cases handled: all zeros, no zeros, and an empty array.
