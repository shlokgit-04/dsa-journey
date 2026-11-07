# 228. Summary Ranges
# https://leetcode.com/problems/summary-ranges/
# Easy | Array

from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        out = []
        i = 0
        while i < len(nums):
            start = nums[i]
            while i + 1 < len(nums) and nums[i + 1] == nums[i] + 1:
                i += 1
            out.append(f"{start}->{nums[i]}" if nums[i] != start else str(start))
            i += 1
        return out


if __name__ == "__main__":
    assert Solution().summaryRanges([0, 1, 2, 4, 5, 7]) == ["0->2", "4->5", "7"]
    assert Solution().summaryRanges([]) == []
    print("ok")
