"""LC 3: Longest Substring Without Repeating Characters (medium, sliding window) - Day 36, Sat Nov 21 2026."""
class Solution:
    def lengthOfLongestSubstring(self, s):
        last = {}
        best = start = 0
        for i, c in enumerate(s):
            if c in last and last[c] >= start:
                start = last[c] + 1
            last[c] = i
            best = max(best, i - start + 1)
        return best


def test():
    assert Solution().lengthOfLongestSubstring("abcabcbb") == 3
    assert Solution().lengthOfLongestSubstring("bbbbb") == 1
    assert Solution().lengthOfLongestSubstring("pwwkew") == 3
    assert Solution().lengthOfLongestSubstring("") == 0
    assert Solution().lengthOfLongestSubstring(" ") == 1
    assert Solution().lengthOfLongestSubstring("abba") == 2
    return "ok"
