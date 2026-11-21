"""LC 49: Group Anagrams (medium, hashing) - Day 36, Sat Nov 21 2026."""
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs):
        buckets = defaultdict(list)
        for s in strs:
            buckets["".join(sorted(s))].append(s)
        return list(buckets.values())


def test():
    out = sorted(Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]), key=sorted)
    assert sorted(map(sorted, out)) == [["ate", "eat", "tea"], ["bat"], ["nat", "tan"]]
    assert Solution().groupAnagrams([""]) == [[""]]
    assert Solution().groupAnagrams(["a"]) == [["a"]]
    return "ok"
