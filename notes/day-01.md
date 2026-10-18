# Day 1 - Two Sum

The obvious answer is two nested loops, O(n^2). The trick is to trade
memory for time: as we walk the list we remember each value and its index
in a dict. For the current value n, the partner we need is target - n.
If we have already seen that partner, we are done.

Complexity: O(n) time, O(n) space.

Edge cases handled: same value twice (nums = [3,3]), no valid pair.
