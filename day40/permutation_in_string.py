"""LC 567: Permutation in String (medium, sliding window + counts).

Fixed window of len(s1) sliding over s2 with a running count array; the
window is a permutation exactly when its counts equal s1's counts. Keep a
single 26-slot delta counter instead of two arrays to compare fast.
Time O(n), space O(1) (26 slots).
"""


def check_inclusion(s1: str, s2: str) -> bool:
    n, m = len(s1), len(s2)
    if n > m:
        return False
    need = [0] * 26
    for ch in s1:
        need[ord(ch) - 97] += 1

    window = [0] * 26
    for i, ch in enumerate(s2):
        window[ord(ch) - 97] += 1
        if i >= n:
            window[ord(s2[i - n]) - 97] -= 1
        if i >= n - 1 and window == need:
            return True
    return False
