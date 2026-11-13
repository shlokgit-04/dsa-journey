# 412. Fizz Buzz
# https://leetcode.com/problems/fizz-buzz/
# Easy | String, Math

from typing import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        out = []
        for i in range(1, n + 1):
            if i % 15 == 0:
                out.append("FizzBuzz")
            elif i % 3 == 0:
                out.append("Fizz")
            elif i % 5 == 0:
                out.append("Buzz")
            else:
                out.append(str(i))
        return out


if __name__ == "__main__":
    assert Solution().fizzBuzz(3) == ["1", "2", "Fizz"]
    assert Solution().fizzBuzz(5) == ["1", "2", "Fizz", "4", "Buzz"]
    assert Solution().fizzBuzz(15)[14] == "FizzBuzz"
    print("ok")
