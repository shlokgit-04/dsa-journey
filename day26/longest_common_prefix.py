

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        """LC 14. Longest Common Prefix - shrink candidate, O(S)."""
        prefix = strs[0]
        for s in strs[1:]:
            while not s.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        return prefix
