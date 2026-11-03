"""LC 242 Valid Anagram - hash-count compare.

Count characters with collections.Counter and compare the two maps.
O(n) time, O(1) space (26 lowercase letters).
"""
from collections import Counter


def is_anagram(s: str, t: str) -> bool:
    return Counter(s) == Counter(t)
