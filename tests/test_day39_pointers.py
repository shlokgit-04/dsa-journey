import pytest

from day39.move_zeroes import Solution as MZSolution
from day39.remove_element import Solution as RESolution


class TestMoveZeroes:
    @pytest.mark.parametrize(
        "nums, expected",
        [
            ([0, 1, 0, 3, 12], [1, 3, 12, 0, 0]),
            ([0], [0]),
            ([1], [1]),
            ([0, 0, 0], [0, 0, 0]),
        ],
    )
    def test_in_place(self, nums, expected):
        MZSolution().moveZeroes(nums)
        assert nums == expected


class TestRemoveElement:
    @pytest.mark.parametrize(
        "nums, val, k, expected_prefix",
        [
            ([3, 2, 2, 3], 3, 2, [2, 2]),
            ([0, 1, 2, 2, 3, 0, 4, 2], 2, 5, [0, 1, 3, 0, 4]),
            ([1], 1, 0, []),
            ([4, 4, 4], 5, 3, [4, 4, 4]),
        ],
    )
    def test_in_place(self, nums, val, k, expected_prefix):
        new_len = RESolution().removeElement(nums, val)
        assert new_len == k
        assert nums[:k] == expected_prefix
