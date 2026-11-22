"""LC 70 Climbing Stairs (Easy) - DP.

Fibonacci in disguise: ways(n) = ways(n-1) + ways(n-2).
Iterative two-variable version, O(n) time, O(1) space.
"""


class Solution:
    def climbStairs(self, n):
        a = b = 1
        for _ in range(n - 1):
            a, b = b, a + b
        return b


if __name__ == "__main__":
    assert Solution().climbStairs(1) == 1
    assert Solution().climbStairs(2) == 2
    assert Solution().climbStairs(3) == 3
    assert Solution().climbStairs(10) == 89
    print("ok")
