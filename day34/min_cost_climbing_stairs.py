"""LC 746 Min Cost Climbing Stairs (Easy, DP).

You may start at step 0 or 1 and climb one or two steps; each step i
costs cost[i]. Cheapest way to reach the top is the min of the last two
running totals: one or two steps back, plus that step's cost.
"""
from typing import List


def min_cost_climbing_stairs(cost: List[int]) -> int:
    a, b = 0, 0
    for c in cost:
        a, b = b, min(a, b) + c
    return min(a, b)


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        return min_cost_climbing_stairs(cost)
