"""LC 11 Container With Most Water - Medium - two pointers (O(n) time, O(1) space)."""


class Solution:
    def maxArea(self, height: list[int]) -> int:
        best = 0
        left, right = 0, len(height) - 1
        while left < right:
            area = min(height[left], height[right]) * (right - left)
            best = max(best, area)
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        return best
