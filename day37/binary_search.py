"""LC 704 Binary Search (Easy) - binary search.

Classic closed-interval [lo, hi] search on a sorted array.
O(log n) time, O(1) space.
"""


class Solution:
    def search(self, nums, target):
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


if __name__ == "__main__":
    assert Solution().search([-1, 0, 3, 5, 9, 12], 9) == 4
    assert Solution().search([-1, 0, 3, 5, 9, 12], 2) == -1
    assert Solution().search([5], 5) == 0
    assert Solution().search([5], -5) == -1
    print("ok")
