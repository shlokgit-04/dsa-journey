# 326. Power of Three
# https://leetcode.com/problems/power-of-three/
# Easy | Math


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n < 1:
            return False
        while n % 3 == 0:
            n //= 3
        return n == 1


if __name__ == "__main__":
    assert Solution().isPowerOfThree(27) is True
    assert Solution().isPowerOfThree(0) is False
    print("ok")
