# Day 21 - Nov 6, 2026

Five fresh problems, all committed and tested locally (25 new pytest cases, all green).

- **LC 27 Remove Element** - overwrite with a slow pointer; O(n) time, O(1) space.
- **LC 26 Remove Duplicates from Sorted Array** - sorted input means only compare against the last kept value; O(n)/O(1).
- **LC 350 Intersection of Two Arrays II** - Counter on nums1, walk nums2 decrementing; O(n+m).
- **LC 66 Plus One** - in-place carry from the right; prepend 1 only if every digit was 9.
- **LC 189 Rotate Array (medium)** - reverse whole array, reverse first k, reverse the rest; O(n)/O(1).

Topic rotation: two pointers, hashing, math, array medium.
