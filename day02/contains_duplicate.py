"""LeetCode 217. Contains Duplicate (Easy)

Solved live on LeetCode 2026-10-18: Accepted, 79/79 testcases, 0 ms.
Idea: a value repeats iff the set shrinks the array.
"""
from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)


def test_duplicate_present():
    assert Solution().containsDuplicate([1, 2, 3, 1]) is True


def test_all_distinct():
    assert Solution().containsDuplicate([1, 2, 3, 4]) is False


def test_many_repeats():
    assert Solution().containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]) is True


def test_single_element():
    assert Solution().containsDuplicate([7]) is False
