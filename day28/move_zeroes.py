# 283. Move Zeroes
# https://leetcode.com/problems/move-zeroes/
# Easy | Two Pointers

from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        w = 0
        for r in range(len(nums)):
            if nums[r] != 0:
                nums[w], nums[r] = nums[r], nums[w]
                w += 1


if __name__ == "__main__":
    a = [0, 1, 0, 3, 12]
    Solution().moveZeroes(a)
    assert a == [1, 3, 12, 0, 0]
    b = [0]
    Solution().moveZeroes(b)
    assert b == [0]
    print("ok")
