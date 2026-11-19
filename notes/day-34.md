# Day 34 - Thu, 19 Nov 2026, Theme: DP basics + greedy + counting

Dark day (12+ commits). Six submissions on LeetCode (118/169/198/746/55/300), all committed
individually with a 15-case pytest run in test_day34.py.

- **LC 118 Pascal's Triangle (easy)** - row i from row i-1, every interior entry sums the two above it.
- **LC 119 Pascal's Triangle II (easy)** - only the row is asked: keep one row of ones and fold updates
  right to left so each add reads the previous row before overwrite.
- **LC 169 Majority Element (easy)** - Boyer-Moore voting: candidate survives because the true majority
  outnumbers everything else combined; Counter version kept for comparison.
- **LC 198 House Robber (medium)** - dp over "money from first i houses": max(skip, rob). Two rolling vars.
- **LC 746 Min Cost Climbing Stairs (easy)** - reach the top paying the cheapest of the last two steps.
- **LC 55 Jump Game (medium)** - greedy reach: position past the current farthest index is unreachable.
- **LC 300 Longest Increasing Subsequence (medium)** - O(n^2) DP vs patience sorting with bisect_left;
  both variants in the file, tests assert they agree.
