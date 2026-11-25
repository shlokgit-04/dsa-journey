"""LC 349: Intersection of Two Arrays (easy, hashing).

Set one array, scan the other, dedupe the hits. The set-membership check is
what keeps the scan linear.
Time O(n + m), space O(min(n, m)).
"""
from typing import List


def intersection(nums1: List[int], nums2: List[int]) -> List[int]:
    inside = set(nums1)
    hits = {n for n in nums2 if n in inside}
    return list(hits)
