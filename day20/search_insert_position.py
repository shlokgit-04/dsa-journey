"""LC 35 Search Insert Position (lower-bound binary search)."""


def search_insert(nums, target):
    lo, hi = 0, len(nums)
    while lo < hi:
        mid = (lo + hi) // 2
        if nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid
    return lo


class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        return search_insert(nums, target)
