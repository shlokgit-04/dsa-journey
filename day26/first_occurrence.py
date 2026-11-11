

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        """LC 28. Find the Index of the First Occurrence - sliding window."""
        n, m = len(haystack), len(needle)
        for i in range(n - m + 1):
            if haystack[i:i + m] == needle:
                return i
        return -1
