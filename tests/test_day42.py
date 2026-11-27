from day42.lc977_squares_of_sorted_array import Solution as S977
from day42.lc414_third_maximum_number import Solution as S414
from day42.lc1207_unique_number_of_occurrences import Solution as S1207


def test_977_squares():
    s = S977()
    assert s.sortedSquares([-4, -1, 0, 3, 10]) == [0, 1, 9, 16, 100]
    assert s.sortedSquares([-7, -3, 2, 3, 11]) == [4, 9, 9, 49, 121]
    assert s.sortedSquares([0]) == [0]
    assert s.sortedSquares([-5, -4]) == [16, 25]
    assert s.sortedSquares([1, 2, 3]) == [1, 4, 9]
    assert s.sortedSquares([-3, -3, -2, 1]) == [1, 4, 9, 9]


def test_414_third_max():
    s = S414()
    assert s.thirdMax([3, 2, 1]) == 1
    assert s.thirdMax([1, 2]) == 2
    assert s.thirdMax([2, 2, 3, 1]) == 1
    assert s.thirdMax([5, 5, 5]) == 5
    assert s.thirdMax([1, 2, 2, 5, 3, 5]) == 2
    assert s.thirdMax([7]) == 7


def test_1207_unique_occurrences():
    s = S1207()
    assert s.uniqueOccurrences([1, 2, 2, 1, 1, 3]) is True
    assert s.uniqueOccurrences([1, 2]) is False
    assert s.uniqueOccurrences([-3, 0, 1, -3, 4, -3, 4, 4, -4, -1]) is False  # -3 and 4 both occur 3x
    assert s.uniqueOccurrences([5, 5, 5, 2, 2, 7, 7, 7, 7, 8, 8, 8, 8, 8]) is True  # counts 3,2,4,5 all distinct
    assert s.uniqueOccurrences([1]) is True
    assert s.uniqueOccurrences([1, 1, 2, 2]) is False  # 1 and 2 both occur 2x
