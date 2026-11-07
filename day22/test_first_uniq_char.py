from first_uniq_char import Solution


def test_basic():
    assert Solution().firstUniqChar("leetcode") == 0


def test_loveleetcode():
    assert Solution().firstUniqChar("loveleetcode") == 2


def test_none():
    assert Solution().firstUniqChar("aabb") == -1


def test_single_char():
    assert Solution().firstUniqChar("z") == 0


def test_unique_at_end():
    assert Solution().firstUniqChar("aabc") == 2
