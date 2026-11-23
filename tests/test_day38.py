from day38.reverse_string import Solution as RS
from day38.valid_anagram import Solution as VA
from day38.valid_palindrome import Solution as VP


def test_reverse_string_basic():
    assert RS().reverseString(list("hello")) == list("olleh")


def test_reverse_string_cases():
    assert RS().reverseString(list("Hannah")) == list("hannaH")
    assert RS().reverseString(list("a")) == list("a")
    assert RS().reverseString([]) == []


def test_anagram_true():
    assert VA().isAnagram("anagram", "nagaram")
    assert VA().isAnagram("", "")


def test_anagram_false():
    assert not VA().isAnagram("rat", "car")
    assert not VA().isAnagram("ab", "a")
    assert not VA().isAnagram("aacc", "ccac")


def test_palindrome_true():
    assert VP().isPalindrome("A man, a plan, a canal: Panama")
    assert VP().isPalindrome(" ")
    assert VP().isPalindrome(".,;")


def test_palindrome_false():
    assert not VP().isPalindrome("race a car")
    assert not VP().isPalindrome("0P")
