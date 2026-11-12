# Day 27 - Nov 12, 2026 (Thu)

GitHub: 10 commits (4 problems x solution+test, notes, README).

## LC 121 Best Time to Buy and Sell Stock (Easy)
One pass: keep min price so far, answer = max(price - min). O(n) time, O(1) space.

## LC 169 Majority Element (Easy)
Boyer-Moore voting: cancel out pairs, survivor is the majority since it appears > n/2.

## LC 206 Reverse Linked List (Easy)
Iterative pointer reversal: save next, flip curr.next to prev, slide prev/curr forward.

## LC 217 Contains Duplicate (Easy)
Hash set membership while scanning; return True on first repeat.
