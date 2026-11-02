"""LC 268 Missing Number (Easy, Array / Hash / Math / XOR).

Given an array nums containing n distinct numbers in [0, n], return the one
number missing from the range. XOR trick: xor all indices and values; every
present value cancels against its index, leaving the missing one.
"""

from typing import List


def missing_number(nums: List[int]) -> int:
    missing = len(nums)  # start with index n, which never appears in values
    for i, val in enumerate(nums):
        missing ^= i ^ val
    return missing
