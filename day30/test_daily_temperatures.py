import os
import sys

import pytest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from day30.daily_temperatures import Solution


@pytest.mark.parametrize(
    "temps,expected",
    [
        ([73, 74, 75, 71, 69, 72, 76, 73], [1, 1, 4, 2, 1, 1, 0, 0]),
        ([30, 40, 50, 60], [1, 1, 1, 0]),
        ([30, 60, 90], [1, 1, 0]),
        ([60, 50, 40], [0, 0, 0]),
        ([50], [0]),
        ([73, 74, 75, 71, 69, 72, 76, 73], [1, 1, 4, 2, 1, 1, 0, 0]),
    ],
)
def test_daily_temperatures(temps, expected):
    assert Solution().dailyTemperatures(temps) == expected
