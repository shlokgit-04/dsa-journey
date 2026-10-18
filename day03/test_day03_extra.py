from day03.roman_to_integer import Solution as R
from day03.longest_common_prefix import Solution as P


def test_roman_examples():
    r = R()
    assert r.romanToInt("III") == 3
    assert r.romanToInt("LVIII") == 58
    assert r.romanToInt("MCMXCIV") == 1994


def test_lcp_examples():
    p = P()
    assert p.longestCommonPrefix(["flower", "flow", "flight"]) == "fl"
    assert p.longestCommonPrefix(["dog", "racecar", "car"]) == ""
    assert p.longestCommonPrefix(["interspecies", "interstellar", "interstate"]) == "inters"
