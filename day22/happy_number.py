# 202. Happy Number
# https://leetcode.com/problems/happy-number/
# Easy | Hash Set, Two Pointers (cycle detection)

def digit_square_sum(n: int) -> int:
    total = 0
    while n:
        d = n % 10
        total += d * d
        n //= 10
    return total


class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = digit_square_sum(n)
        return n == 1


if __name__ == "__main__":
    assert Solution().isHappy(19) is True
    assert Solution().isHappy(2) is False
    print("ok")
