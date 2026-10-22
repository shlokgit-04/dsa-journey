# Day 7 — Valid Palindrome (LeetCode 125)

**Topic:** Two pointers / strings
**Complexity:** O(n) time, O(1) space.

## Idea
Two pointers walk inward. Skip anything that isn't alphanumeric, compare the
lowercased characters, and stop early on any mismatch.

## Key detail
`s.isalnum()` on Python str covers letters and digits (and the problem counts
both), so no explicit filtering pass is needed.

## Interview relevance
The canonical "clean input with two pointers without extra memory" template.
Also the natural follow-up to Day 5's two-pointer work.
