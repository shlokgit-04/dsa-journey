"""Two Sum: return indices of the two numbers that add up to target.

One pass with a hash map: for each value, check if its complement
(target - value) has already been seen. O(n) time, O(n) space.
"""
from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    seen = {}
    for i, n in enumerate(nums):
        need = target - n
        if need in seen:
            return [seen[need], i]
        seen[n] = i
    return []
