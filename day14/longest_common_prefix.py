from typing import List


def longest_common_prefix(strs: List[str]) -> str:
    """LC 14 Longest Common Prefix: horizontal scan, shrink as mismatches appear."""
    if not strs:
        return ""
    prefix = strs[0]
    for s in strs[1:]:
        i = 0
        while i < len(prefix) and i < len(s) and prefix[i] == s[i]:
            i += 1
        prefix = prefix[:i]
        if not prefix:
            return ""
    return prefix


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        return longest_common_prefix(strs)
