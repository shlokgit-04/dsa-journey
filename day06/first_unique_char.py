"""LeetCode 387. First Unique Character in a String (Easy, Hashing)

Find the index of the first character that appears exactly once.
One pass counts frequencies; a second pass scans in order and returns
the first index whose count is 1. Scanning in input order is what makes
the second pass return the FIRST unique, not any unique.

Interview relevance: frequency-count hashing, the base pattern behind
anagram checks, top-k, and dedup problems.
"""


def first_unique_char(s: str) -> int:
    counts = {}
    for ch in s:
        counts[ch] = counts.get(ch, 0) + 1
    for i, ch in enumerate(s):
        if counts[ch] == 1:
            return i
    return -1


class Solution:
    def firstUniqChar(self, s: str) -> int:
        return first_unique_char(s)
