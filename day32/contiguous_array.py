# 525. Contiguous Array (Medium) - Day 32
# Treat 0 as -1; equal counts of 0 and 1 means the running sum repeats.
def findMaxLength(self, nums):
    first_at = {0: -1}
    s = best = 0
    for i, n in enumerate(nums):
        s += 1 if n else -1
        if s in first_at:
            best = max(best, i - first_at[s])
        else:
            first_at[s] = i
    return best

class Solution:
    findMaxLength = findMaxLength
