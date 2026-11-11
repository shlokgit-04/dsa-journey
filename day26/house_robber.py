

class Solution:
    def rob(self, nums: list[int]) -> int:
        """LC 198. House Robber - rolling DP, O(n) time O(1) space."""
        prev, curr = 0, 0
        for x in nums:
            prev, curr = curr, max(curr, prev + x)
        return curr
