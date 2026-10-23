"""LC 169 Majority Element (Easy) - Day 8

Boyer-Moore voting: keep a candidate and a counter; the true majority
element survives because it outweighs everything else combined.
"""
def majority_element(nums):
    candidate, count = None, 0
    for n in nums:
        if count == 0:
            candidate = n
        count += 1 if n == candidate else -1
    return candidate
