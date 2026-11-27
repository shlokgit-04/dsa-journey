"""LC 1207 Unique Number of Occurrences (hashing).

Count each distinct value's frequency; the answer is true exactly when
the frequency list itself contains no duplicates.
"""


class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        counts = {}
        for x in arr:
            counts[x] = counts.get(x, 0) + 1
        seen = set()
        for c in counts.values():
            if c in seen:
                return False
            seen.add(c)
        return True
