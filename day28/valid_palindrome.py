# 125. Valid Palindrome
# https://leetcode.com/problems/valid-palindrome/
# Easy | Two Pointers, String

class Solution:
    def isPalindrome(self, s: str) -> bool:
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
    assert Solution().isPalindrome("A man, a plan, a canal: Panama") is True
    assert Solution().isPalindrome("race a car") is False
    assert Solution().isPalindrome(" ") is True
    print("ok")
