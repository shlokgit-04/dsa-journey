"""LC 268 Missing Number (Easy, math / hashing).

Gauss sum: the sum of 0..n minus the array sum is the missing value.
No overflow risk in Python, so the closed form is the clean pick.
"""
from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        return n * (n + 1) // 2 - sum(nums)
