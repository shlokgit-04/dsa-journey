"""LeetCode 121. Best Time to Buy and Sell Stock (Easy)

One pass: track the minimum price so far; each day, the best sell
profit from that price is price - min_so_far.
"""

from typing import List


def max_profit(prices: List[int]) -> int:
    min_price = float("inf")
    profit = 0
    for p in prices:
        if p < min_price:
            min_price = p
        elif p - min_price > profit:
            profit = p - min_price
    return profit


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        return max_profit(prices)
