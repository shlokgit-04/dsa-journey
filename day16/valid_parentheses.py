"""LC 20 Valid Parentheses (stack)."""


def is_valid(s: str) -> bool:
    """Return True if every bracket closes in the right order."""
    pairs = {')': '(', ']': '[', '}': '{'}
    stack = []
    for ch in s:
        if ch in pairs:
            if not stack or stack.pop() != pairs[ch]:
                return False
        else:
            stack.append(ch)
    return not stack
