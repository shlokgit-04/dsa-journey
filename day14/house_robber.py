from typing import List


def rob(nums: List[int]) -> int:
    """LC 198 House Robber: DP over houses, max of skipping or taking each."""
    take, skip = 0, 0
    for value in nums:
        take, skip = skip + value, max(take, skip)
    return max(take, skip)


class Solution:
    def rob(self, nums: List[int]) -> int:
        return rob(nums)
