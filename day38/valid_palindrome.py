"""LC 125 Valid Palindrome (Easy) - two pointers / strings.

Skip non-alphanumerics, compare lowercased chars from both ends.
O(n) time, O(1) extra space.
"""


class Solution:
    def isPalindrome(self, s):
        lo, hi = 0, len(s) - 1
        while lo < hi:
            while lo < hi and not s[lo].isalnum():
                lo += 1
            while lo < hi and not s[hi].isalnum():
                hi -= 1
            if s[lo].lower() != s[hi].lower():
                return False
            lo += 1
            hi -= 1
        return True


if __name__ == "__main__":
    assert Solution().isPalindrome("A man, a plan, a canal: Panama")
    assert not Solution().isPalindrome("race a car")
    assert Solution().isPalindrome(" ")
    assert not Solution().isPalindrome("0P")
    print("ok")
