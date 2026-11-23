# Day 38 notes - Monday strings night (Nov 23, 2026)

- LC 344 Reverse String: two pointers swap inward, return the same list.
  Gotcha: LeetCode wants the reversal in place, not a new string.
- LC 242 Valid Anagram: one counter, decrement for t. Early len check
  kills most wrong cases fast.
- LC 125 Valid Palindrome: skip non-alphanumerics inside the same loop,
  compare after lower(). "0P" is NOT a palindrome ('0' != 'p'), the
  trap is assuming alnum filtering alone settles it.
