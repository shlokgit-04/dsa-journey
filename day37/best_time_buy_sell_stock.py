"""LC 121 Best Time to Buy and Sell Stock (Easy) - arrays/DP.

Track the cheapest price seen so far; each day the best profit is
price - min_so_far. One pass, O(n) time, O(1) space.
"""


class Solution:
    def maxProfit(self, prices):
        buy = float("inf")
        best = 0
        for p in prices:
            best = max(best, p - buy)
            buy = min(buy, p)
        return best


if __name__ == "__main__":
    assert Solution().maxProfit([7, 1, 5, 3, 6, 4]) == 5
    assert Solution().maxProfit([7, 6, 4, 3, 1]) == 0
    assert Solution().maxProfit([2, 4, 1]) == 2
    print("ok")
