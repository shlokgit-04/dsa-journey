# dsa-journey

Daily DSA practice for internship interviews. One problem a day, in Python.

Each day gets a working solution, a small test suite, and notes on the approach and complexity. Tests run with pytest: `pytest -q`.

Started October 18, 2026.
- Day 8 (Oct 23): Missing Number, Majority Element, Ransom Note - 9 tests green
- Day 9 (Oct 25): Single Number, Maximum Subarray, Merge Two Sorted Lists - 9 tests green
- Day 10 (Oct 26): Reverse String, Remove Element - 6 tests green
- Day 12 (Oct 28): Best Time to Buy and Sell Stock (LC 121) + Binary Search (LC 704) - single-pass min-price sweep, closed-interval binary search - 14 tests green
- Day 13 (Oct 29): Squares of a Sorted Array (LC 977) + Roman to Integer (LC 13), two-pointer end merge + subtraction lookahead, 6 tests green
- Day 14 (Oct 30): Longest Common Prefix (LC 14) + Linked List Cycle (LC 141) + House Robber (LC 198), horizontal scan + Floyd cycle detection + rolling take/skip DP, 9 tests green

| Day 15 | LC 217 Contains Duplicate + LC 1 Two Sum | hash set membership, one-pass complement map | [day15](day15) |
| Day 16 | LC 283 Move Zeroes + LC 20 Valid Parentheses + LC 110 Balanced Binary Tree | slow/fast partition, bracket stack, bottom-up height DFS | [day16](day16) |
| Day 17 | LC 268 Missing Number | XOR index^value accumulator | [day17](day17) |
| Day 18 | LC 242 Valid Anagram + LC 104 Max Depth + LC 88 Merge Sorted Array | Counter equality, bottom-up height DFS, back-to-front merge | [day18](day18) |
| Day 19 | LC 226 Invert BT + LC 101 Symmetric Tree + LC 70 Climbing Stairs + LC 344 Reverse String + LC 125 Valid Palindrome + LC 13 Roman to Integer | subtree swap, mirrored-pair DFS, Fibonacci DP, in-place two-pointer reverse, alnum two-pointer scan, symbol map with subtract rule | [day19](day19) |
| Day 20 | LC 206 Reverse Linked List + LC 121 Best Time to Buy and Sell Stock + LC 169 Majority Element + LC 35 Search Insert Position + LC 9 Palindrome Number | 27 |
| Day 21 | LC 27 Remove Element + LC 26 Remove Duplicates from Sorted Array + LC 350 Intersection of Two Arrays II + LC 66 Plus One + LC 189 Rotate Array | 25 |
| Day 22 | LC 202 Happy Number + LC 228 Summary Ranges + LC 387 First Unique Character in a String + LC 58 Length of Last Word + LC 191 Number of 1 Bits | 25 |
| Day 23 | LC 118 Pascal's Triangle + LC 509 Fibonacci Number + LC 155 Min Stack + LC 232 Implement Queue using Stacks + LC 404 Sum of Left Leaves | 25 |
| Day 24 | LC 122 Best Time to Buy and Sell Stock II + LC 326 Power of Three + LC 225 Implement Stack using Queues + LC 234 Palindrome Linked List + LC 347 Top K Frequent Elements | 25 |
| Day 25 | LC 387 First Unique Character in a String + LC 703 Kth Largest Element in a Stream + LC 108 Convert Sorted Array to BST | hash count two-pass scan, min-heap of size k, mid-element recursion | [day25](day25) |
| Day 26 | LC 242 Valid Anagram + LC 13 Roman to Integer + LC 14 Longest Common Prefix + LC 28 strStr + LC 198 House Robber | [notes](notes/day-26.md) |
| Day 27 | LC 121 Stock I + LC 169 Majority Element + LC 206 Reverse Linked List + LC 217 Contains Duplicate | one-pass min tracking, Boyer-Moore voting, pointer reversal, set scan |
