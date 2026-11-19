"""LC 118 Pascal's Triangle (Easy, Arrays/DP).

Row i is built from row i-1: every interior entry is the sum of the two
entries above it. Row 0 is [1].
"""
from typing import List


def generate(num_rows: int) -> List[List[int]]:
    rows: List[List[int]] = []
    for i in range(num_rows):
        if i == 0:
            rows.append([1])
            continue
        prev = rows[-1]
        row = [1] + [prev[j - 1] + prev[j] for j in range(1, i)] + [1]
        rows.append(row)
    return rows


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        return generate(numRows)
