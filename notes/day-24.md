# Day 24 - Nov 9, 2026

Five fresh problems, all committed and tested locally (25 new pytest cases, all green).

- **LC 122 Best Time to Buy and Sell Stock II (medium)** - unlimited trades means take every positive day-over-day rise; O(n)/O(1).
- **LC 326 Power of Three** - keep dividing by 3; leaves 1 exactly for powers of three.
- **LC 225 Implement Stack using Queues** - one queue, re-rotate on push so the newest item sits at the front.
- **LC 234 Palindrome Linked List** - middle via slow/fast, reverse the second half, compare; O(n)/O(1).
- **LC 347 Top K Frequent Elements (medium)** - Counter + heapq.nlargest on frequency; O(n log k).

Topic rotation: greedy, math, design, linked list, hashing.
