"""LC 75: Sort Colors (medium, two pointers, Dutch national flag).

Three regions in one pass: low tracks the 0 boundary, high tracks the 2
boundary. Swap a 0 to the front and a 2 to the back as the scan pointer
crosses them; 1s settle in the middle on their own.
Time O(n), space O(1).
"""
from typing import List


def sort_colors(nums: List[int]) -> None:
    low, mid, high = 0, 0, len(nums) - 1
    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 2:
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1
        else:
            mid += 1
