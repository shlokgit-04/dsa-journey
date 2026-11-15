# 682. Baseball Game
# https://leetcode.com/problems/baseball-game/
# Easy | Array, Stack


class Solution:
    def calPoints(self, operations: list[str]) -> int:
        stack = []
        for op in operations:
            if op == "+":
                stack.append(stack[-1] + stack[-2])
            elif op == "D":
                stack.append(2 * stack[-1])
            elif op == "C":
                stack.pop()
            else:
                stack.append(int(op))
        return sum(stack)


if __name__ == "__main__":
    assert Solution().calPoints(["5", "2", "C", "D", "+"]) == 30
    assert Solution().calPoints(["5", "-2", "4", "C", "D", "9", "+", "+"]) == 27
    assert Solution().calPoints(["1", "C"]) == 0
    print("ok")
