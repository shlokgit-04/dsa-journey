# 238. Product of Array Except Self (Medium)
# Two passes without division: result[i] starts as the product of everything
# left of i, then a right-to-left pass multiplies in the running suffix product.
# Time O(n), space O(1) beyond the output array.
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        out = [1] * n
        left = 1
        for i in range(n):
            out[i] = left
            left *= nums[i]
        right = 1
        for i in range(n - 1, -1, -1):
            out[i] *= right
            right *= nums[i]
        return out
