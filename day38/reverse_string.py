"""LC 344 Reverse String (Easy) - two pointers.

In-place reverse of a char list with two pointers walking inward.
O(n) time, O(1) extra space.
"""


class Solution:
    def reverseString(self, s):
        lo, hi = 0, len(s) - 1
        while lo < hi:
            s[lo], s[hi] = s[hi], s[lo]
            lo += 1
            hi -= 1
        return s


if __name__ == "__main__":
    assert Solution().reverseString(list("hello")) == list("olleh")
    assert Solution().reverseString(list("Hannah")) == list("hannaH")
    assert Solution().reverseString(list("a")) == list("a")
    assert Solution().reverseString([]) == []
    print("ok")
