import os
import sys

import pytest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from day30.valid_parentheses import Solution


@pytest.mark.parametrize(
    "s,expected",
    [
        ("()", True),
        ("()[]{}", True),
        ("(]", False),
        ("([)]", False),
        ("{[]}", True),
        ("", True),
        ("(", False),
        (")", False),
        ("([{}])", True),
        ("([{}]))", False),
    ],
)
def test_valid_parentheses(s, expected):
    assert Solution().isValid(s) is expected
