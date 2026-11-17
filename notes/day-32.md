# Day 32 - Tue, 17 Nov 2026

**Theme: hashing + prefix sums**

- **LC 205 Isomorphic Strings (Easy)** - two one-pass maps (s->t and t->s); a letter must map consistently both ways.
- **LC 560 Subarray Sum Equals K (Medium)** - prefix sums + hash map of prefix counts; count[s-k] subarrays ending here.
- **LC 525 Contiguous Array (Medium)** - treat 0 as -1; longest subarray with equal 0/1 = farthest pair of equal running sums.

Tests: `tests/test_day32.py` (11 cases) - all passing locally before commit.
