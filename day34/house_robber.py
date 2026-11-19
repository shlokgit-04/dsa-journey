"""LC 198 House Robber (Medium, DP).

dp[i] = max money robbing the first i houses. Either skip house i
(dp[i-1]) or rob it (dp[i-2] + nums[i-1]); adjacent houses can't both
be robbed. Rolling two variables keep it O(1) space.
"""
from typing import List


def rob(nums: List[int]) -> int:
    prev, curr = 0, 0
    for num in nums:
        prev, curr = curr, max(curr, prev + num)
    return curr


class Solution:
    def rob(self, nums: List[int]) -> int:
        return rob(nums)
