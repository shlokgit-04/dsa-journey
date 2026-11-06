# 27. Remove Element
# https://leetcode.com/problems/remove-element/
# Easy | Array, Two Pointers

from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for x in nums:
            if x != val:
                nums[k] = x
                k += 1
        return k


if __name__ == "__main__":
    nums = [3, 2, 2, 3]
    k = Solution().removeElement(nums, 3)
    assert k == 2 and sorted(nums[:k]) == [2, 2]
    print("ok")
