# 680. Valid Palindrome II
# https://leetcode.com/problems/valid-palindrome-ii/
# Easy | Two Pointers, String, Greedy


class Solution:
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                skip_left = s[left + 1 : right + 1]
                skip_right = s[left:right]
                return (
                    skip_left == skip_left[::-1]
                    or skip_right == skip_right[::-1]
                )
            left += 1
            right -= 1
        return True


if __name__ == "__main__":
    assert Solution().validPalindrome("aba") is True
    assert Solution().validPalindrome("abca") is True
    assert Solution().validPalindrome("abc") is False
    print("ok")
