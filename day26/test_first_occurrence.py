from day26.first_occurrence import Solution


def test_sad_but_sad():
    assert Solution().strStr("sadbutsad", "sad") == 0


def test_leetcode_middle():
    assert Solution().strStr("leetcode", "leeto") == -1


def test_middle_match():
    assert Solution().strStr("hello", "ll") == 2


def test_needle_empty():
    assert Solution().strStr("abc", "") == 0


def test_needle_longer():
    assert Solution().strStr("a", "aaa") == -1
