from typing import List


def contains_duplicate(nums: List[int]) -> bool:
    """LC 217 Contains Duplicate (Easy).

    Hash set membership scan: add each value to a seen-set; the first
    repeat proves a duplicate. O(n) time, O(n) space.
    """
    seen = set()
    for value in nums:
        if value in seen:
            return True
        seen.add(value)
    return False
