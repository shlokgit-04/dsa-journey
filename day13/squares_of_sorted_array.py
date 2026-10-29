"""LC 977: Squares of a Sorted Array (two pointers).

Sorted input can hold negatives, so the largest squares live at both ends.
Merge the two ends inward, writing squares from the back of the result.
"""
def sorted_squares(nums: list[int]) -> list[int]:
    n = len(nums)
    out = [0] * n
    left, right = 0, n - 1
    for pos in range(n - 1, -1, -1):
        if abs(nums[left]) > abs(nums[right]):
            out[pos] = nums[left] * nums[left]
            left += 1
        else:
            out[pos] = nums[right] * nums[right]
            right -= 1
    return out
