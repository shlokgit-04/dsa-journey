# Day 30 - Sun, 15 Nov 2026

Dark day. Topic: stacks (5 problems).

- **LC 20 Valid Parentheses (Easy)** - stack, match closers against openers; a mismatch or an opener left over at the end fails.
- **LC 682 Baseball Game (Easy)** - stack of scores; +, D, C operate on the top two / top / top.
- **LC 496 Next Greater Element I (Easy)** - monotonic decreasing stack over nums2, pop into a next-greater map, then map nums1.
- **LC 739 Daily Temperatures (Medium)** - monotonic stack of indices; popping j when a warmer i arrives gives answer[j] = i - j.
- **LC 150 Evaluate Reverse Polish Notation (Medium)** - stack eval; division must truncate toward zero, so use int(a / b) not a // b (Python floors).

Key insight: the "truncation toward zero" trap in LC 150 - `int(a / b)` handles negatives correctly where `a // b` floors.

Local test run: 32 passed (day30 suite), after fixing two wrong expected values (1+2+4+8 = 15 not 30; 4 has no next greater so [-1,2,3]).
