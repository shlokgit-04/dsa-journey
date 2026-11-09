# 122. Best Time to Buy and Sell Stock II
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
# Medium | Array, Greedy

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]
        return profit


if __name__ == "__main__":
    assert Solution().maxProfit([7, 1, 5, 3, 6, 4]) == 7
    assert Solution().maxProfit([1, 2, 3, 4, 5]) == 4
    print("ok")
