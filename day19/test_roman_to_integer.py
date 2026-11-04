from day19.roman_to_integer import Solution


def test_examples():
    assert Solution().romanToInt("III") == 3
    assert Solution().romanToInt("LVIII") == 58
    assert Solution().romanToInt("MCMXCIV") == 1994


def test_subtractive_pairs():
    assert Solution().romanToInt("IV") == 4
    assert Solution().romanToInt("IX") == 9
    assert Solution().romanToInt("XL") == 40
    assert Solution().romanToInt("CM") == 900


def test_single():
    assert Solution().romanToInt("M") == 1000
