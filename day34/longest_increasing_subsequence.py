"""LC 300 Longest Increasing Subsequence (Medium, DP).

dp[i] = length of the best increasing subsequence ending at i: scan the
smaller left indices, extend when nums[j] < nums[i]. The patience
sorting variant keeps tails sorted and binary-searches for the swap
point, giving O(n log n).
"""
from bisect import bisect_left
from typing import List


def length_of_lis_dp(nums: List[int]) -> int:
    if not nums:
        return 0
    dp = [1] * len(nums)
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)


def length_of_lis(nums: List[int]) -> int:
    tails: List[int] = []
    for num in nums:
        i = bisect_left(tails, num)
        if i == len(tails):
            tails.append(num)
        else:
            tails[i] = num
    return len(tails)


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        return length_of_lis(nums)
