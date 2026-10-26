# Day 10 - Oct 26, 2026

Two-pointer work day (regular intensity: 1 commit).

- **LC 344 Reverse String (Easy)** - classic left/right pointer swap in place. O(n) time, O(1) space. Trivial but a good warmup: the pointer dance (`swap, left+=1, right-=1`) shows up everywhere.
- **LC 27 Remove Element (Easy)** - write-index technique: one pointer reads every element, the other only writes the keepers. Same pattern powers LC 26, LC 283 (already done), and partition steps in quicksort.

Pattern note: "read pointer scans everything, write pointer collects what survives" is the core of in-place array filtering. Both problems: O(n) time, O(1) space.
