"""LC 455 Assign Cookies: sort both sides, greedy smallest-fit first."""
from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        child = 0
        for size in s:
            if child < len(g) and g[child] <= size:
                child += 1
        return child
