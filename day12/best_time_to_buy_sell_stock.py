"""Best Time to Buy and Sell Stock (LeetCode 121, Easy).

Single pass: track the minimum price seen so far and the best profit
made selling after it. O(n) time, O(1) space.
"""
from typing import List


def max_profit(prices: List[int]) -> int:
    if not prices:
        return 0
    best = 0
    min_price = prices[0]
    for price in prices[1:]:
        if price < min_price:
            min_price = price
        else:
            best = max(best, price - min_price)
    return best


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        return max_profit(prices)
