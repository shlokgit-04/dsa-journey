# 205. Isomorphic Strings (Easy) - Day 32
# Two-way character mapping; a fresh letter must map consistently both ways.
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s2t, t2s = {}, {}
        for a, b in zip(s, t):
            if s2t.setdefault(a, b) != b or t2s.setdefault(b, a) != a:
                return False
        return True
