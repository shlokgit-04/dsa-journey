# 560. Subarray Sum Equals K (Medium) - Day 32
# Prefix sums + hash map of counts. s - k seen before means a subarray sums to k.
from collections import defaultdict

class Solution:
    def subarraySum(self, nums, k):
        count = defaultdict(int)
        count[0] = 1
        s = res = 0
        for n in nums:
            s += n
            res += count[s - k]
            count[s] += 1
        return res
