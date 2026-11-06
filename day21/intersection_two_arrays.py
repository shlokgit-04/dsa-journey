# 350. Intersection of Two Arrays II
# https://leetcode.com/problems/intersection-of-two-arrays-ii/
# Easy | Hash Table, Two Pointers

from collections import Counter
from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        counts = Counter(nums1)
        out = []
        for x in nums2:
            if counts[x] > 0:
                out.append(x)
                counts[x] -= 1
        return out


if __name__ == "__main__":
    assert Solution().intersect([1, 2, 2, 1], [2, 2]) == [2, 2]
    assert Solution().intersect([4, 9, 5], [9, 4, 9, 8, 4]) in ([4, 9], [9, 4])
    print("ok")
