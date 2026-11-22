"""LC 53 Maximum Subarray (Medium) - DP (Kadane's algorithm).

Keep a running best subarray ending here; extend it or restart at the
current element, whichever is bigger. O(n) time, O(1) space.
"""


class Solution:
    def maxSubArray(self, nums):
        cur = best = nums[0]
        for x in nums[1:]:
            cur = max(x, cur + x)
            best = max(best, cur)
        return best


if __name__ == "__main__":
    assert Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
    assert Solution().maxSubArray([1]) == 1
    assert Solution().maxSubArray([5, 4, -1, 7, 8]) == 23
    assert Solution().maxSubArray([-1]) == -1
    print("ok")
