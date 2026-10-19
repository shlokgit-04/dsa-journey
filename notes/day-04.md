# Day 4 - Climbing Stairs

The naive recursion is exponential because it recomputes the same
subproblems. Once you see that ways(n) depends only on ways(n-1) and
ways(n-2), it is Fibonacci in disguise, so two rolling variables give
O(n) time and O(1) space with no memo table needed.

Complexity: O(n) time, O(1) space.

Edge cases handled: n = 1 and n = 2 are returned directly (the loop
assumes n >= 3).
