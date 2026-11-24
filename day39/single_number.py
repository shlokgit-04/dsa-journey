"""LC 136 Single Number (Easy, bit manipulation).

XOR is associative and a ^ a = 0, so xoring every number leaves only
the one that never got a pair. O(n) time, O(1) space.
"""
from functools import reduce
from operator import xor
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return reduce(xor, nums, 0)
