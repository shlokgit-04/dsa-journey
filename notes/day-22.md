# Day 22 - Nov 7, 2026

Five fresh problems, all committed and tested locally (25 new pytest cases, all green).

- **LC 202 Happy Number** - digit-square sums land in a fixed cycle; hash set until 1 or a repeat; O(log n) per step.
- **LC 228 Summary Ranges** - walk with a start pointer, close the range when the run breaks.
- **LC 387 First Unique Character in a String** - one Counter pass, one scan; O(n).
- **LC 58 Length of Last Word** - split and read the last token; O(n).
- **LC 191 Number of 1 Bits** - Brian Kernighan's trick, n &= n-1 clears the lowest set bit each round.

Topic rotation: hashing, array, strings, bitwise.
