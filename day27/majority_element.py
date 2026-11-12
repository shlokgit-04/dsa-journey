# LC 169 Majority Element (Easy)
# Counting trick: candidate survives because it appears > n/2 times.
def majority_element(nums: list[int]) -> int:
    count = 0
    candidate = None
    for x in nums:
        if count == 0:
            candidate = x
        count += 1 if x == candidate else -1
    return candidate
