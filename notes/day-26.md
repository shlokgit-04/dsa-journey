# Day 26 - Nov 11, 2026 (dark day)

Five problems today, rotating into hashing, strings, and DP.

| LC | Title | Idea | Complexity |
|----|-------|------|------------|
| 242 | Valid Anagram | Counter equality; length check short-circuits | O(n) / O(1) (26 letters) |
| 13 | Roman to Integer | One pass; if current < next, subtract, else add | O(n) / O(1) |
| 14 | Longest Common Prefix | Shrink the candidate prefix until every word starts with it | O(S) / O(1) |
| 28 | strStr | Slide a window of len(needle) over haystack, compare slice | O(n*m) / O(1) |
| 198 | House Robber | Rolling DP: prev, curr = curr, max(curr, prev + x) | O(n) / O(1) |

Notes:
- 242: Counter(s) == Counter(t) is the cleanest Python; the length pre-check avoids counting both strings fully on a mismatch.
- 13: the subtractive rule (IV, IX, XL, XC, CD, CM) is just "current value less than next value means subtract current".
- 14: `startswith` shrinking is simpler than char-by-char columns and handles the single-word edge for free.
- 28: Python slices make the window compare one line; empty needle returns 0 because "" == "".
- 198: classic two-variable DP; max(curr, prev + x) encodes skip vs rob without an array.

25 tests green locally (5 per problem).
