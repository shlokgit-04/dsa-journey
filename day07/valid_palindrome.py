"""LeetCode 125. Valid Palindrome (Easy, two pointers / strings)

A phrase is a palindrome if, after converting all uppercase letters into
lowercase letters and removing all non-alphanumeric characters, it reads
the same forward and backward.

Approach: two pointers walking inward, skipping non-alphanumeric
characters. O(n) time, O(1) extra space.
"""

def is_palindrome(s: str) -> bool:
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

class Solution:
    def isPalindrome(self, s: str) -> bool:
        return is_palindrome(s)
