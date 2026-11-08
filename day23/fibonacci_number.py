# 509. Fibonacci Number
# https://leetcode.com/problems/fibonacci-number/
# Easy | DP, Iterative


class Solution:
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b


if __name__ == "__main__":
    assert [Solution().fib(i) for i in range(7)] == [0, 1, 1, 2, 3, 5, 8]
    print("ok")
