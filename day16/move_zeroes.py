"""LC 283 Move Zeroes (two pointers, in-place)."""
from typing import List


def move_zeroes(nums: List[int]) -> List[int]:
    """Shift every 0 to the end in place, keeping non-zero order.

    Slow pointer marks where the next non-zero lands; fast pointer scans.
    """
    slow = 0
    for fast in range(len(nums)):
        if nums[fast] != 0:
            nums[slow], nums[fast] = nums[fast], nums[slow]
            slow += 1
    return nums
