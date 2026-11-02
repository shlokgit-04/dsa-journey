# Day 17 - Nov 2, 2026 (Monday, regular day)

| Problem | Difficulty | Topic | Approach | Time | Space |
|---|---|---|---|---|---|
| LC 268 Missing Number | Easy | Array / XOR | XOR all indices (0..n-1) with all values and n; pairs cancel, missing value survives | O(n) | O(1) |

Key idea: index n is never a value, so seed the accumulator with n, then
`missing ^= i ^ val` for each slot. Every number in [0, n] except the missing
one appears exactly twice across the index/value stream, so XOR leaves only it.

5 pytest tests green.
