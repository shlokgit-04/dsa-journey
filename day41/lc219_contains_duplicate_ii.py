"""LC 219 Contains Duplicate II: value -> last index, gap check under k."""
from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        last_seen = {}
        for i, x in enumerate(nums):
            if x in last_seen and i - last_seen[x] <= k:
                return True
            last_seen[x] = i
        return False
