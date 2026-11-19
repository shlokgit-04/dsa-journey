"""LC 169 Majority Element (Easy, Hashing/Counting).

Two takes: a Counter pass (O(n) time, O(n) space) and Boyer-Moore voting
(O(n) time, O(1) space): keep a candidate and a counter, replace the
candidate when the counter hits 0, and the true majority element always
survives because it outnumbers everything else combined.
"""
from collections import Counter
from typing import List


def majority_element_counter(nums: List[int]) -> int:
    counts = Counter(nums)
    return max(counts, key=counts.get)


def majority_element_boyer_moore(nums: List[int]) -> int:
    candidate, votes = None, 0
    for num in nums:
        if votes == 0:
            candidate = num
        votes += 1 if num == candidate else -1
    return candidate


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return majority_element_boyer_moore(nums)
