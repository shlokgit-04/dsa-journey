"""LC 53 Maximum Subarray (Medium) - Day 9

Kadane's algorithm: carry the best sum ending here, drop it when it
goes negative. Track the global best along the way.
O(n) time, O(1) space.
"""
def max_sub_array(nums: list[int]) -> int:
    best = cur = nums[0]
    for n in nums[1:]:
        cur = max(n, cur + n)
        best = max(best, cur)
    return best
