# LC 121 Best Time to Buy and Sell Stock (Easy)
# One pass: track min price so far, best profit = price - min.
def max_profit(prices: list[int]) -> int:
    best = 0
    min_price = float("inf")
    for p in prices:
        if p < min_price:
            min_price = p
        elif p - min_price > best:
            best = p - min_price
    return best
