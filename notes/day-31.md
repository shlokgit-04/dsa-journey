# Day 31 - Mon, 16 Nov 2026

Regular day. Topic: two pointers (3 problems).

- **LC 125 Valid Palindrome (Easy)** - two pointers from both ends, skipping non-alphanumeric chars; compare lowercased. Trap: `"0P"` - `isdigit` on 'P' is false but char codes differ, so compare lowercase letters, not `ord()` tricks.
- **LC 344 Reverse String (Easy)** - classic in-place swap from both ends walking inward.
- **LC 167 Two Sum II - Input Array Is Sorted (Medium)** - left/right pointers; sum too small moves left up, too big moves right down. 1-indexed answer.

Key insight: two pointers works when movement of one pointer gives a monotonic signal - sorted array (167) or skip-and-compare from both ends (125).

Local test run: 12 passed (day31 suite, 5 + 3 + 4 cases).
