"""LeetCode 283. Move Zeroes (Easy, Two Pointers)

Move all zeros to the end of the array while keeping the relative order
of the non-zero elements. Two pointers: one scans, one marks where the
next non-zero belongs; overwrite, then pad the tail with zeros.

Interview relevance: the canonical in-place array partition problem,
same write-pointer pattern behind remove-element and sort-colors.
"""


def move_zeroes(nums: list[int]) -> list[int]:
    write = 0
    for read in range(len(nums)):
        if nums[read] != 0:
            nums[write] = nums[read]
            write += 1
    for i in range(write, len(nums)):
        nums[i] = 0
    return nums


class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        move_zeroes(nums)
