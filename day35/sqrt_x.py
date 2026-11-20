"""LC 69 Sqrt(x) - Easy - integer binary search on the answer."""

import math


class Solution:
    def mySqrt(self, x: int) -> int:
        lo, hi = 0, x
        while lo <= hi:
            mid = (lo + hi) // 2
            sq = mid * mid
            if sq == x:
                return mid
            if sq < x:
                lo = mid + 1
            else:
                hi = mid - 1
        return hi
