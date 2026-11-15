# 496. Next Greater Element I
# https://leetcode.com/problems/next-greater-element-i/
# Easy | Array, Hash Map, Stack


class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        next_greater = {}
        stack = []
        for num in nums2:
            while stack and num > stack[-1]:
                next_greater[stack.pop()] = num
            stack.append(num)
        return [next_greater.get(n, -1) for n in nums1]


if __name__ == "__main__":
    assert Solution().nextGreaterElement([4, 1, 2], [1, 3, 4, 2]) == [-1, 3, -1]
    assert Solution().nextGreaterElement([2, 4], [1, 2, 3, 4]) == [3, -1]
    print("ok")
