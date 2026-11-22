# Day 37 notes - Sunday dark day (Nov 22, 2026)

Theme: DP + binary search + trees (rotating back to trees after two string days).

- LC 121 Best Time to Buy and Sell Stock: single pass, keep the running minimum and
  the best (price - min) seen. The "can't sell before you buy" constraint falls out
  of the order of the two updates for free.
- LC 53 Maximum Subarray: Kadane. cur = max(x, cur + x); best = max(best, cur).
  Negative-only arrays handled by initializing both to nums[0] instead of 0.
- LC 70 Climbing Stairs: Fibonacci. Two variables, n-1 iterations, no array.
- LC 704 Binary Search: standard closed-interval loop. Edge cases: single element,
  target absent on either side.
- LC 226 Invert Binary Tree: recurse, swap children. Base case None -> None.
- LC 100 Same Tree: three-way guard (both None, one None, value mismatch) then
  recurse on both children. Same shape as 226 but comparing instead of building.

Pattern noticed: 226 and 100 are the same traversal with different payloads; once
the guard order is muscle memory, both are one-liners.

Local: 14 pytest cases, all green before any commit.
