import os
import sys

import pytest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from day30.evaluate_rpn import Solution


@pytest.mark.parametrize(
    "tokens,expected",
    [
        (["2", "1", "+", "3", "*"], 9),
        (["4", "13", "5", "/", "+"], 6),
        (["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"], 22),
        (["18"], 18),
        (["6", "-132", "/"], 0),  # truncation toward zero
    ],
)
def test_eval_rpn(tokens, expected):
    assert Solution().evalRPN(tokens) == expected
