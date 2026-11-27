# Day 42 (Fri Nov 27, 2026) - two pointers + sorting + hashing

## LC 977 Squares of a Sorted Array
- nums is already sorted, so the biggest absolute values live at the two ends.
- Two pointers fill the result from the back: the larger |nums[l]| vs |nums[r]| wins the current tail slot; the smaller square naturally lands deeper in the array. O(n), no sort call.

## LC 414 Third Maximum Number
- Dedupe first, then sort descending: index 2 is the third maximum, else the maximum.
- The dedupe matters: repeated values are not distinct maxima, and "fewer than 3 distinct" flips the answer to plain max.

## LC 1207 Unique Number of Occurrences
- One pass builds value -> count; the answer is whether the count list itself has repeats.
- Test lesson: [1,1,2,2,2] is TRUE (counts 2 and 3 are unique), [1,1,2,2] is FALSE (both occur twice). Check each expectation against a brute force before trusting head math.
