from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """LC 242. Valid Anagram - Counter equality, O(n)."""
        return Counter(s) == Counter(t)
