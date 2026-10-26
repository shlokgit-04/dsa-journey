"""LC 27: Remove Element (Easy) - two pointers, write index."""
from typing import List


def remove_element(nums: List[int], val: int) -> int:
    """Move all != val to the front; return k. Elements after k don't matter."""
    write = 0
    for x in nums:
        if x != val:
            nums[write] = x
            write += 1
    return write
