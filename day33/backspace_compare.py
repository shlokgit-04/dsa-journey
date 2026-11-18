# 844. Backspace String Compare (Easy)
# Walk both strings from the end: skip over '#'s, dropping one real char
# per pending backspace, then compare the surviving characters one by one.
# Time O(m + n), space O(1).
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def skip(i, x):
            b = 0
            while i >= 0:
                if x[i] == '#':
                    b += 1
                elif b:
                    b -= 1
                else:
                    return i - 1
                i -= 1
            return i

        i, j = len(s) - 1, len(t) - 1
        while i >= 0 or j >= 0:
            i = skip(i, s)
            j = skip(j, t)
            if i >= 0 and j >= 0 and s[i] != t[j]:
                return False
            if (i >= 0) != (j >= 0):
                return False
            i -= 1
            j -= 1
        return True
