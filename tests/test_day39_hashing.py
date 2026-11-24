import pytest

from day39.majority_element import Solution as MESolution, majority_element_counter
from day39.missing_number import Solution as MNSolution
from day39.single_number import Solution as SNSolution


class TestMajorityElement:
    @pytest.mark.parametrize(
        "nums, expected",
        [
            ([3, 2, 3], 3),
            ([2, 2, 1, 1, 1, 2, 2], 2),
            ([1], 1),
            ([6, 5, 5], 5),
        ],
    )
    def test_boyer_moore(self, nums, expected):
        assert MESolution().majorityElement(nums) == expected

    def test_counter_matches(self):
        assert majority_element_counter([2, 2, 1, 1, 1, 2, 2]) == 2


class TestSingleNumber:
    @pytest.mark.parametrize(
        "nums, expected",
        [
            ([2, 2, 1], 1),
            ([4, 1, 2, 1, 2], 4),
            ([1], 1),
        ],
    )
    def test_xor_folds(self, nums, expected):
        assert SNSolution().singleNumber(nums) == expected


class TestMissingNumber:
    @pytest.mark.parametrize(
        "nums, expected",
        [
            ([3, 0, 1], 2),
            ([0, 1], 2),
            ([9, 6, 4, 2, 3, 5, 7, 0, 1], 8),
            ([0], 1),
        ],
    )
    def test_gauss_sum(self, nums, expected):
        assert MNSolution().missingNumber(nums) == expected
