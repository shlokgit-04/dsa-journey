import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from container_with_most_water import Solution as MaxArea
from find_the_duplicate_number import Solution as FindDup
from sqrt_x import Solution as MySqrt


class TestContainerWithMostWater:
    def test_example_1(self):
        assert MaxArea().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49

    def test_two_lines(self):
        assert MaxArea().maxArea([1, 1]) == 1

    def test_descending(self):
        assert MaxArea().maxArea([4, 3, 2, 1, 4]) == 16

    def test_single_tall(self):
        assert MaxArea().maxArea([1, 2, 1]) == 2

    def test_all_same(self):
        assert MaxArea().maxArea([3, 3, 3, 3]) == 9


class TestFindDuplicate:
    def test_example_1(self):
        assert FindDup().findDuplicate([1, 3, 4, 2, 2]) == 2

    def test_example_2(self):
        assert FindDup().findDuplicate([3, 1, 3, 4, 2]) == 3

    def test_small(self):
        assert FindDup().findDuplicate([1, 1]) == 1

    def test_duplicate_adjacent(self):
        assert FindDup().findDuplicate([2, 2, 2, 2, 2]) == 2

    def test_larger(self):
        assert FindDup().findDuplicate([1, 4, 6, 6, 6, 2, 3, 5]) == 6


class TestMySqrt:
    def test_zero(self):
        assert MySqrt().mySqrt(0) == 0

    def test_one(self):
        assert MySqrt().mySqrt(1) == 1

    def test_perfect(self):
        assert MySqrt().mySqrt(16) == 4

    def test_floor(self):
        assert MySqrt().mySqrt(8) == 2

    def test_large(self):
        assert MySqrt().mySqrt(2147395599) == 46339


if __name__ == "__main__":
    import pytest

    raise SystemExit(pytest.main([__file__, "-q"]))
