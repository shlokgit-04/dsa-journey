# Day 15 (Oct 31): Hashing

Saturday regular day: one commit, two easy problems, both settled with a hash map/set.

## LC 217 Contains Duplicate (Easy)
Walk the array adding values to a set; the first value already present
proves a duplicate. O(n) time, O(n) space. Alternative worth knowing:
sort then scan neighbours in O(n log n) with O(1) extra space.

## LC 1 Two Sum (Easy)
One-pass complement map: for each value look up `target - value`
among earlier entries; the map holds value -> index so the returned
pair is always two distinct positions. O(n) time, O(n) space.

## Takeaway
The complement-map pattern turns "find a pair" into "have I seen this
difference before", and it is the single most reused hashing trick in
the whole array family.
