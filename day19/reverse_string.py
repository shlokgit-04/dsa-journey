"""LC 344 Reverse String (Easy, Two Pointers).

Reverse the char list in place with O(1) extra memory:
swap the ends and walk the pointers inward until they meet.
"""
from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
