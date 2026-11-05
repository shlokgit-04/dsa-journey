"""LC 9 Palindrome Number (reverse half of the digits)."""


def is_palindrome(x):
    if x < 0 or (x % 10 == 0 and x != 0):
        return False
    rev = 0
    while x > rev:
        rev = rev * 10 + x % 10
        x //= 10
    return x == rev or x == rev // 10


class Solution:
    def isPalindrome(self, x: int) -> bool:
        return is_palindrome(x)
