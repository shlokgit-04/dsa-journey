"""LeetCode 70. Climbing Stairs (Easy, DP)

You are climbing a staircase with n steps; each move is 1 or 2 steps.
Ways(n) = Ways(n-1) + Ways(n-2): the classic Fibonacci recurrence.
Two rolling variables keep it O(n) time, O(1) space.

Interview relevance: the canonical intro to dynamic programming --
recognise overlapping subproblems before reaching for memoization.
"""


def climb_stairs(n: int) -> int:
    if n <= 2:
        return n
    prev, curr = 1, 2
    for _ in range(3, n + 1):
        prev, curr = curr, prev + curr
    return curr


class Solution:
    def climbStairs(self, n: int) -> int:
        return climb_stairs(n)
