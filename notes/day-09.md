# Day 9 - Oct 25, 2026

Bright-graph day (Sunday): three problems, committed one at a time.

- **Single Number (LC 136)**: XOR everything; pairs cancel to 0, the lone value survives. O(n)/O(1).
- **Maximum Subarray (LC 53)**: Kadane's. Carry the best sum ending here, reset when it drags, track the global best. O(n)/O(1).
- **Merge Two Sorted Lists (LC 21)**: dummy head, tie the smaller node each step, attach the tail. O(n+m)/O(1).

Pattern of the day: O(1)-space tricks. XOR for cancellation, running-sum reset for subarrays, pointer relinking for lists.
