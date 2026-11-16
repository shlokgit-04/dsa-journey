import sys, unittest, pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "day31"))

from valid_palindrome import Solution as VP
from reverse_string import Solution as RS
from two_sum_ii import Solution as TS


class TestValidPalindrome(unittest.TestCase):
    def test_sentence_palindrome(self):
        self.assertTrue(VP().isPalindrome("A man, a plan, a canal: Panama"))

    def test_not_palindrome(self):
        self.assertFalse(VP().isPalindrome("race a car"))

    def test_empty_after_strip(self):
        self.assertTrue(VP().isPalindrome(" "))

    def test_alnum_edge(self):
        self.assertFalse(VP().isPalindrome("0P"))

    def test_mixed_case(self):
        self.assertTrue(VP().isPalindrome("Was it a car or a cat I saw?"))


class TestReverseString(unittest.TestCase):
    def test_odd_length(self):
        chars = ["h", "e", "l", "l", "o"]
        RS().reverseString(chars)
        self.assertEqual(chars, ["o", "l", "l", "e", "h"])

    def test_even_length(self):
        chars = ["H", "a", "n", "n", "a", "h"]
        RS().reverseString(chars)
        self.assertEqual(chars, ["h", "a", "n", "n", "a", "H"])

    def test_single(self):
        chars = ["x"]
        RS().reverseString(chars)
        self.assertEqual(chars, ["x"])


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
