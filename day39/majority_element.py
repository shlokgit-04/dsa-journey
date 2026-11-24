"""LC 169 Majority Element (Easy, hashing).

Boyer-Moore voting: keep a candidate and a counter; a true majority
element survives because every non-majority pair cancels one vote.
O(n) time, O(1) space.
"""
from collections import Counter
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate, votes = None, 0
        for num in nums:
            if votes == 0:
                candidate = num
            votes += 1 if num == candidate else -1
        return candidate


def majority_element_counter(nums: List[int]) -> int:
    """Straightforward alternative: Counter + max by count."""
    return max(Counter(nums), key=Counter(nums).get)
