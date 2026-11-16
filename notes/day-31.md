# Day 31 - Mon, 16 Nov 2026

Regular day. Topic: two pointers (3 problems). Started with 125 and 344, then
caught they were already done (day 10 and day 28), so swapped for fresh picks.

- **LC 680 Valid Palindrome II (Easy)** - two pointers from both ends; on the
  first mismatch, try skipping either side and check the two remaining slices.
  Greedy: one deletion only.
- **LC 443 String Compression (Medium)** - read pointer counts a run, write
  pointer rewrites it in place; counts above 9 split into digits, so write
  them one by one.
- **LC 167 Two Sum II - Input Array Is Sorted (Medium)** - left/right pointers;
  sum too small moves left up, too big moves right down. 1-indexed answer.

Key insight: two pointers works when a pointer's move gives a monotonic signal -
sorted array (167), skip-and-compare from both ends (680), or run boundaries in
an in-place rewrite (443).

Local test run: 14 passed (day31 suite, 5 + 5 + 4 cases).
