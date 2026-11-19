"""LC 119 Pascal's Triangle II (Easy, Arrays/DP).

Only row rowIndex is needed, so keep a single rolling row and extend it
in place: update from right to left so each add uses the previous row's
values before they are overwritten.
"""
from typing import List


def get_row(row_index: int) -> List[int]:
    row = [1] * (row_index + 1)
    for build in range(2, row_index + 1):
        for j in range(build - 1, 0, -1):
            row[j] += row[j - 1]
    return row


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        return get_row(rowIndex)
