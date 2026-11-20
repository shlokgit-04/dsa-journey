# Day 35 notes - Fri, 20 Nov 2026

Two pointers + cycle detection + binary search day. Three problems, one commit each, 15-case
pytest run (test_day35.py) green before touching LeetCode.

- **LC 11 Container With Most Water (medium)** - area = min(h[l], h[r]) * (r-l). Only the shorter
  wall can possibly make a bigger area, so move the shorter side in each step. Greedy on which
  pointer to advance is the whole trick; never recompute from scratch.
- **LC 287 Find the Duplicate Number (medium)** - array of n+1 values in [1,n] read as a function
  f(i) = nums[i]; a duplicate value means two indices point at the same node, so the walk from
  index 0 has a cycle. Phase 1: slow = nums[slow], fast = nums[nums[fast]] until they meet inside
  the cycle. Phase 2: reset slow to 0, advance both one step; the meeting point is the duplicate
  entry point. O(n) time, O(1) space, no mutation - beats the sorting and hash-set alternatives.
- **LC 69 Sqrt(x) (easy)** - binary search on the integer answer, not Newton (avoids overflow
  traps on huge x). Track the floor: when lo > hi, hi holds floor(sqrt(x)). Edge: x = 0 and 1.
