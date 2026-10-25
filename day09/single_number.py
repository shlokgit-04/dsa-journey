"""LC 136 Single Number (Easy) - Day 9

Every element appears twice except one. XOR everything: pairs cancel
(a ^ a = 0, a ^ 0 = a), so the survivor is the single number.
O(n) time, O(1) space.
"""
def single_number(nums: list[int]) -> int:
    seen = 0
    for n in nums:
        seen ^= n
    return seen
