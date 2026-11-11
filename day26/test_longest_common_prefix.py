from day26.longest_common_prefix import Solution


def test_flower():
    assert Solution().longestCommonPrefix(["flower", "flow", "flight"]) == "fl"


def test_no_common():
    assert Solution().longestCommonPrefix(["dog", "racecar", "car"]) == ""


def test_single_word():
    assert Solution().longestCommonPrefix(["hello"]) == "hello"


def test_same_words():
    assert Solution().longestCommonPrefix(["ab", "ab", "ab"]) == "ab"


def test_prefix_is_full_word():
    assert Solution().longestCommonPrefix(["flower", "flower", "flower"]) == "flower"
