from day26.valid_anagram import Solution


def test_true_anagram():
    assert Solution().isAnagram("anagram", "nagaram") is True


def test_false_anagram():
    assert Solution().isAnagram("rat", "car") is False


def test_empty_both():
    assert Solution().isAnagram("", "") is True


def test_length_mismatch():
    assert Solution().isAnagram("a", "ab") is False


def test_repeated_letters():
    assert Solution().isAnagram("aacc", "ccac") is False
