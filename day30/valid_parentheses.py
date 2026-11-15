# 20. Valid Parentheses
# https://leetcode.com/problems/valid-parentheses/
# Easy | String, Stack


class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {")": "(", "]": "[", "}": "{"}
        stack = []
        for ch in s:
            if ch in "([{":
                stack.append(ch)
            elif not stack or stack.pop() != pairs[ch]:
                return False
        return not stack


if __name__ == "__main__":
    assert Solution().isValid("()[]{}") is True
    assert Solution().isValid("(]") is False
    assert Solution().isValid("([)]") is False
    assert Solution().isValid("{[]}") is True
    assert Solution().isValid("") is True
    print("ok")
