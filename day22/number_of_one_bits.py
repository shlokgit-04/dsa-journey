# 191. Number of 1 Bits
# https://leetcode.com/problems/number-of-1-bits/
# Easy | Bit Manipulation


class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            n &= n - 1  # clears the lowest set bit
            count += 1
        return count


if __name__ == "__main__":
    assert Solution().hammingWeight(11) == 3
    assert Solution().hammingWeight(0) == 0
    print("ok")
