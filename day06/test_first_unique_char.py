from day06.first_unique_char import first_unique_char


def test_examples():
    assert first_unique_char("leetcode") == 0
    assert first_unique_char("loveleetcode") == 2
    assert first_unique_char("aabb") == -1


def test_single_char():
    assert first_unique_char("z") == 0


def test_unique_at_end():
    assert first_unique_char("aab") == 2
