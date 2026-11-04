"""LC 70 Climbing Stairs (Easy, DP).

n stairs, 1 or 2 steps at a time: the count is the Fibonacci sequence.
ways(n) = ways(n-1) + ways(n-2); iterate with two rolling variables.
"""
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        prev, curr = 1, 2
        for _ in range(3, n + 1):
            prev, curr = curr, prev + curr
        return curr
