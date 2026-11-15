import os
import sys

import pytest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from day30.next_greater_element import Solution


@pytest.mark.parametrize(
    "nums1,nums2,expected",
    [
        ([4, 1, 2], [1, 3, 4, 2], [-1, 3, -1]),
        ([2, 4], [1, 2, 3, 4], [3, -1]),
        ([1, 2, 3], [3, 2, 1], [-1, -1, -1]),
        ([1], [1], [-1]),
        ([4, 1, 2], [1, 2, 3, 4], [-1, 2, 3]),
    ],
)
def test_next_greater(nums1, nums2, expected):
    assert Solution().nextGreaterElement(nums1, nums2) == expected
