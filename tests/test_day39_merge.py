import pytest

from day39.merge_sorted_array import Solution


class TestMergeSortedArray:
    @pytest.mark.parametrize(
        "nums1, m, nums2, n, expected",
        [
            ([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3, [1, 2, 2, 3, 5, 6]),
            ([1], 1, [], 0, [1]),
            ([0], 0, [1], 1, [1]),
        ],
    )
    def test_backwards_merge(self, nums1, m, nums2, n, expected):
        Solution().merge(nums1, m, nums2, n)
        assert nums1 == expected
