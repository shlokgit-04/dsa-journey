"""LC 169 Majority Element (Boyer-Moore vote)."""


def majority_element(nums):
    count = 0
    cand = None
    for n in nums:
        if count == 0:
            cand = n
            count = 1
        elif n == cand:
            count += 1
        else:
            count -= 1
    return cand


class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        return majority_element(nums)
