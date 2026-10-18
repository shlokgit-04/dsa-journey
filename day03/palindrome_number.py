"""LeetCode 9. Palindrome Number (Easy)

Day 3 of the daily grind.
"""

def is_palindrome(x: int) -> bool:
    s = str(x)
    return s == s[::-1]


class Solution:
    def isPalindrome(self, x: int) -> bool:
        return is_palindrome(x)
