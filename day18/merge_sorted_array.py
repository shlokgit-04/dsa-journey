"""LC 88 Merge Sorted Array - merge back-to-front.

nums1 has trailing zeros for the merge buffer. Fill from the largest end so
writes never overwrite unread values. O(m+n) time, O(1) space.
"""
from typing import List


def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    i, j, k = m - 1, n - 1, m + n - 1
    while j >= 0:
        if i >= 0 and nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1
