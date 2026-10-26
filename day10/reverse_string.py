"""LC 344: Reverse String (Easy) - two pointers, in place."""
from typing import List


def reverse_string(s: List[str]) -> List[str]:
    """Reverse the char list in place; return it (LC returns None, we return for testing)."""
    left, right = 0, len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
    return s
