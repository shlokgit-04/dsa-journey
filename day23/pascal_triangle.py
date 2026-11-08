# 118. Pascal's Triangle
# https://leetcode.com/problems/pascals-triangle/
# Easy | Array, DP

from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        rows = []
        for i in range(numRows):
            row = [1] * (i + 1)
            for j in range(1, i):
                row[j] = rows[i - 1][j - 1] + rows[i - 1][j]
            rows.append(row)
        return rows


if __name__ == "__main__":
    assert Solution().generate(5) == [
        [1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]
    ]
    print("ok")
