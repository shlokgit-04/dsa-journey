# Day 20 - Nov 5, 2026 (Thursday, dark day)

5 problems: LC 206 Reverse Linked List, LC 121 Best Time to Buy and Sell Stock,
LC 169 Majority Element, LC 35 Search Insert Position, LC 9 Palindrome Number.

- LC 206: iterative three-pointer (prev/cur/nxt), O(n) time O(1) space.
- LC 121: one pass, track min price so far, best = max(best, p - min).
- LC 169: Boyer-Moore vote, O(n) time O(1) space.
- LC 35: lower-bound binary search, lo/hi with mid compare.
- LC 9: negative and trailing-zero rejections, then reverse the back half.

27 new tests green; full day18+19+20 suite 62 passed.
