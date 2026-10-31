from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    """LC 1 Two Sum (Easy).

    One-pass complement map: for each value, check whether target - value
    was already seen; the map stores value -> index. O(n) time, O(n) space.
    """
    complement_index = {}
    for i, value in enumerate(nums):
        need = target - value
        if need in complement_index:
            return [complement_index[need], i]
        complement_index[value] = i
    return []
