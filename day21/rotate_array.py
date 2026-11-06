# 189. Rotate Array
# https://leetcode.com/problems/rotate-array/
# Medium | Array, Two Pointers (in-place reversal)

from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n

        def rev(lo: int, hi: int) -> None:
            while lo < hi:
                nums[lo], nums[hi] = nums[hi], nums[lo]
                lo += 1
                hi -= 1

        rev(0, n - 1)
        rev(0, k - 1)
        rev(k, n - 1)


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 6, 7]
    Solution().rotate(nums, 3)
    assert nums == [5, 6, 7, 1, 2, 3, 4]
    print("ok")
