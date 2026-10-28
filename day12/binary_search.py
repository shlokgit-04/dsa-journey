"""Binary Search (LeetCode 704, Easy).

Classic closed-interval binary search. O(log n) time, O(1) space.
"""
from typing import List


def search(nums: List[int], target: int) -> int:
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return search(nums, target)
