# Day 6 - First Unique Character in a String

Two passes over the string: the first builds a character frequency
table, the second walks the string in order and returns the first index
whose count is 1. The in-order second pass is what guarantees FIRST
unique; a hash table alone has no order.

Complexity: O(n) time, O(1) space (at most 26 lowercase letters).

Edge cases handled: no unique character returns -1, single character
returns 0, unique at the end still found by the ordered scan.
