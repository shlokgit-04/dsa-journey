from day26.roman_to_integer import Solution


def test_three():
    assert Solution().romanToInt("III") == 3


def test_four():
    assert Solution().romanToInt("IV") == 4


def test_nine():
    assert Solution().romanToInt("IX") == 9


def test_1994():
    assert Solution().romanToInt("MCMXCIV") == 1994


def test_58():
    assert Solution().romanToInt("LVIII") == 58
