# 26. Remove Duplicates from Sorted Array
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/
# Easy | Array, Two Pointers

from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        for i, x in enumerate(nums):
            if i == 0 or x != nums[k - 1]:
                nums[k] = x
                k += 1
        return k


if __name__ == "__main__":
    nums = [0, 0, 1, 1, 1, 2, 2]
    k = Solution().removeDuplicates(nums)
    assert k == 3 and nums[:k] == [0, 1, 2]
    print("ok")
