# 125. Valid Palindrome
# https://leetcode.com/problems/valid-palindrome/
# Easy | Two Pointers, String


class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True


if __name__ == "__main__":
    assert Solution().isPalindrome("A man, a plan, a canal: Panama") is True
    assert Solution().isPalindrome("race a car") is False
    assert Solution().isPalindrome(" ") is True
    assert Solution().isPalindrome("0P") is False
    print("ok")
