# 344. Reverse String
# https://leetcode.com/problems/reverse-string/
# Easy | Two Pointers

from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        lo, hi = 0, len(s) - 1
        while lo < hi:
            s[lo], s[hi] = s[hi], s[lo]
            lo += 1
            hi -= 1


if __name__ == "__main__":
    a = ["h", "e", "l", "l", "o"]
    Solution().reverseString(a)
    assert a == ["o", "l", "l", "e", "h"]
    b = ["H", "a", "n", "n", "a", "h"]
    Solution().reverseString(b)
    assert b == ["h", "a", "n", "n", "a", "H"]
    print("ok")
