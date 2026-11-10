from first_uniq_char import Solution


def test_leetcode_example():
    assert Solution().firstUniqChar("leetcode") == 0


def test_second_example():
    assert Solution().firstUniqChar("loveleetcode") == 2


def test_none_unique():
    assert Solution().firstUniqChar("aabb") == -1


def test_single_char():
    assert Solution().firstUniqChar("z") == 0


def test_unique_in_middle():
    assert Solution().firstUniqChar("aabbc") == 4
