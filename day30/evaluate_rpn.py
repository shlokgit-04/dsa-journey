# 150. Evaluate Reverse Polish Notation
# https://leetcode.com/problems/evaluate-reverse-polish-notation/
# Medium | Array, Math, Stack


class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        ops = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: int(a / b),  # truncates toward zero
        }
        for token in tokens:
            if token in ops:
                b = stack.pop()
                a = stack.pop()
                stack.append(ops[token](a, b))
            else:
                stack.append(int(token))
        return stack[0]


if __name__ == "__main__":
    assert Solution().evalRPN(["2", "1", "+", "3", "*"]) == 9
    assert Solution().evalRPN(["4", "13", "5", "/", "+"]) == 6
    assert Solution().evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]) == 22
    print("ok")
