"""LC 121 Best Time to Buy and Sell Stock (one pass, min price tracking)."""


def max_profit(prices):
    min_price = None
    best = 0
    for p in prices:
        if min_price is None or p < min_price:
            min_price = p
        elif p - min_price > best:
            best = p - min_price
    return best


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        return max_profit(prices)
