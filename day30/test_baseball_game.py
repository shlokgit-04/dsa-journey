import os
import sys

import pytest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from day30.baseball_game import Solution


@pytest.mark.parametrize(
    "ops,expected",
    [
        (["5", "2", "C", "D", "+"], 30),
        (["5", "-2", "4", "C", "D", "9", "+", "+"], 27),
        (["1", "C"], 0),
        (["5", "-2", "4", "C", "D", "9", "+", "+"], 27),
        (["1", "D", "D", "D"], 15),
        (["1"], 1),
    ],
)
def test_cal_points(ops, expected):
    assert Solution().calPoints(ops) == expected
