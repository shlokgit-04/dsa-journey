# Day 23 - Nov 8, 2026

Five fresh problems, all committed and tested locally (25 new pytest cases, all green).

- **LC 118 Pascal's Triangle** - each row is built from the one above it; O(n^2) values total.
- **LC 509 Fibonacci Number** - two-variable iteration, no recursion; O(n)/O(1).
- **LC 155 Min Stack (medium)** - push alongside a parallel stack that tracks the min at every depth.
- **LC 232 Implement Queue using Stacks** - inbox/outbox; shift only when the outbox runs dry, so amortized O(1).
- **LC 404 Sum of Left Leaves** - DFS with an is_left flag; a left leaf adds only when it has no children.

Topic rotation: array, DP, design, tree.
