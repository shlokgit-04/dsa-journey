# 739. Daily Temperatures
# https://leetcode.com/problems/daily-temperatures/
# Medium | Array, Stack, Monotonic Stack


class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        answer = [0] * len(temperatures)
        stack = []  # indices with decreasing temperatures
        for i, temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                j = stack.pop()
                answer[j] = i - j
            stack.append(i)
        return answer


if __name__ == "__main__":
    assert Solution().dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]) == [1, 1, 4, 2, 1, 1, 0, 0]
    assert Solution().dailyTemperatures([30, 40, 50, 60]) == [1, 1, 1, 0]
    assert Solution().dailyTemperatures([30, 60, 90]) == [1, 1, 0]
    print("ok")
