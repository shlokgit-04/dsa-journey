# Day 39 notes - Tuesday, arrays + hashing + bit tricks

## LC 169 Majority Element
Boyer-Moore voting: hold a candidate, add a vote for a match, subtract
one for a mismatch, re-candidate on zero. Every non-majority element
cancels another, so the true majority (> n/2) survives. O(n) time,
O(1) space. Kept a Counter version beside it as the readable baseline.

## LC 136 Single Number
`reduce(xor, nums, 0)` is the whole problem: xor is associative,
commutative, and a ^ a = 0, so paired values vanish and only the
unpaired one is left. O(1) space beats the Counter/hash-set answers.

## LC 268 Missing Number
Gauss sum n(n+1)/2 minus the array sum. In Python the closed form has
no overflow worry; the xor trick from LC 136 would work here too
(xor 0..n against every element).

## LC 283 Move Zeroes
Same slow/fast shape as LC 27 but with a swap so relative order of the
non-zeros is preserved. Return nothing, mutate the list in place.

## LC 27 Remove Element
Overwrite variant: copy keep-elements forward with a write pointer and
return the write index. The test checks nums[:k], not full equality,
because LeetCode only guarantees the first k slots.

## LC 88 Merge Sorted Array
Merge backwards from index m+n-1. Filling from the back means the
placeholder zeros in nums1 are consumed first, so nothing gets
overwritten before it is read. Only j >= 0 needs handling: if j runs
dry first, the leftover nums1 prefix is already in place.

## Pattern of the day
Three problems (27, 283, 88) are the same write-pointer family with
slightly different rules (overwrite vs swap vs backwards fill).
Spotting that family is the actual skill being trained.
