"""LC 268 Missing Number (Easy) - Day 8

Given nums containing n distinct numbers in [0, n], return the one missing.
XOR trick: a^a = 0, so XOR all indices 0..n with all values; everything
cancels except the missing number.
"""
def missing_number(nums):
    res = len(nums)
    for i, n in enumerate(nums):
        res ^= i ^ n
    return res
