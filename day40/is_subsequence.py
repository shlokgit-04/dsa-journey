"""LC 392: Is Subsequence (easy, two pointers).

Walk both strings; every time chars match, advance the subsequence pointer.
Matching the whole of s means it is a subsequence of t.
Time O(len(t)), space O(1).
"""


def is_subsequence(s: str, t: str) -> bool:
    if not s:
        return True
    i = 0
    for ch in t:
        if ch == s[i]:
            i += 1
            if i == len(s):
                return True
    return False
