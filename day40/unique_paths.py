"""LC 62: Unique Paths (medium, DP).

Robot walks right/down on an m x n grid. First row and column have exactly
one path; every other cell sums its top and left neighbors. Roll one row to
keep space at O(n).
Time O(m * n), space O(n).
"""


def unique_paths(m: int, n: int) -> int:
    row = [1] * n
    for _ in range(1, m):
        for col in range(1, n):
            row[col] += row[col - 1]
    return row[-1]
