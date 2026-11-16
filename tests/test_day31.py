import sys, unittest, pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "day31"))

from valid_palindrome_ii import Solution as VPII
from string_compression import Solution as SC
from two_sum_ii import Solution as TS


class TestValidPalindromeII(unittest.TestCase):
    def test_already_palindrome(self):
        self.assertTrue(VPII().validPalindrome("aba"))

    def test_one_delete(self):
        self.assertTrue(VPII().validPalindrome("abca"))

    def test_needs_two(self):
        self.assertFalse(VPII().validPalindrome("abc"))

    def test_front_delete(self):
        self.assertTrue(VPII().validPalindrome("cuucu"))

    def test_single_char(self):
        self.assertTrue(VPII().validPalindrome("z"))


class TestStringCompression(unittest.TestCase):
    def test_groups(self):
        chars = ["a", "a", "b", "b", "c", "c", "c"]
        self.assertEqual(SC().compress(chars), 6)
        self.assertEqual(chars[:6], ["a", "2", "b", "2", "c", "3"])

    def test_single_char(self):
        chars = ["a"]
        self.assertEqual(SC().compress(chars), 1)
        self.assertEqual(chars[:1], ["a"])

    def test_two_same(self):
        chars = ["a", "a"]
        self.assertEqual(SC().compress(chars), 2)
        self.assertEqual(chars[:2], ["a", "2"])

    def test_two_digit_count(self):
        chars = ["a"] * 12
        self.assertEqual(SC().compress(chars), 3)
        self.assertEqual(chars[:3], ["a", "1", "2"])

    def test_no_change(self):
        chars = ["a", "b", "b"]
        self.assertEqual(SC().compress(chars), 3)
        self.assertEqual(chars[:3], ["a", "b", "2"])


class TestTwoSumII(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(TS().twoSum([2, 7, 11, 15], 9), [1, 2])

    def test_inner_pair(self):
        self.assertEqual(TS().twoSum([2, 3, 4], 6), [1, 3])

    def test_negatives(self):
        self.assertEqual(TS().twoSum([-1, 0], -1), [1, 2])

    def test_middle_pair(self):
        self.assertEqual(TS().twoSum([1, 3, 4, 5, 7, 11], 9), [3, 4])


if __name__ == "__main__":
    unittest.main()
