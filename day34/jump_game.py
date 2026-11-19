"""LC 55 Jump Game (Medium, Greedy).

Walk the array keeping the farthest reachable index; a position past
that reach is unreachable, so return False early. Greedy reach update
needs one pass, no DP table.
"""
from typing import List


def can_jump(nums: List[int]) -> bool:
    reach = 0
    for i, jump in enumerate(nums):
        if i > reach:
            return False
        reach = max(reach, i + jump)
        if reach >= len(nums) - 1:
            return True
    return True


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        return can_jump(nums)
