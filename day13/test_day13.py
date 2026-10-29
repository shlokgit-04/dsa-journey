from day13.squares_of_sorted_array import sorted_squares
from day13.roman_to_integer import roman_to_int


def test_squares_basic():
    assert sorted_squares([-4, -1, 0, 3, 10]) == [0, 1, 9, 16, 100]


def test_squares_all_negative():
    assert sorted_squares([-7, -3, -1]) == [1, 9, 49]


def test_squares_single():
    assert sorted_squares([-5]) == [25]


def test_roman_simple():
    assert roman_to_int("III") == 3
    assert roman_to_int("XII") == 12


def test_roman_subtractive():
    assert roman_to_int("IV") == 4
    assert roman_to_int("IX") == 9
    assert roman_to_int("LVIII") == 58


def test_roman_mixed():
    assert roman_to_int("MCMXCIV") == 1994
    assert roman_to_int("MMMCMXCIX") == 3999
