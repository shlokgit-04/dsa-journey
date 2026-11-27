"""LC 977 Squares of a Sorted Array (two pointers, O(n)).

nums is non-decreasing, so the largest squares sit at either end.
Fill the result from the back: compare |nums[l]| vs |nums[r]| and place
the bigger square at the current tail, moving the winning pointer inward.
"""


class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        n = len(nums)
        res = [0] * n
        l, r = 0, n - 1
        for i in range(n - 1, -1, -1):
            if abs(nums[l]) > abs(nums[r]):
                res[i] = nums[l] * nums[l]
                l += 1
            else:
                res[i] = nums[r] * nums[r]
                r -= 1
        return res
