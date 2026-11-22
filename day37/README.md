# Day 37 - Sunday dark day (Nov 22, 2026)

DP + binary search + trees. Six problems solved and committed one by one:

| # | Problem | Difficulty | Idea | File |
|---|---------|-----------|------|------|
| 1 | LC 121 Best Time to Buy and Sell Stock | Easy | track min price so far, profit = price - min | [best_time_buy_sell_stock.py](best_time_buy_sell_stock.py) |
| 2 | LC 53 Maximum Subarray | Medium | Kadane: extend or restart the running subarray | [maximum_subarray.py](maximum_subarray.py) |
| 3 | LC 70 Climbing Stairs | Easy | Fibonacci recurrence, two variables | [climbing_stairs.py](climbing_stairs.py) |
| 4 | LC 704 Binary Search | Easy | closed-interval [lo, hi] search | [binary_search.py](binary_search.py) |
| 5 | LC 226 Invert Binary Tree | Easy | swap left/right, recurse | [invert_binary_tree.py](invert_binary_tree.py) |
| 6 | LC 100 Same Tree | Easy | recurse down both trees together | [same_tree.py](same_tree.py) |

Run the suite: `python3 -m pytest tests/test_day37.py -q` (14 cases).
