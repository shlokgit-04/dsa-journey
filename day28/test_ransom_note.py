from day28.ransom_note import Solution


def test_cant():
    assert Solution().canConstruct("a", "b") is False


def test_not_enough():
    assert Solution().canConstruct("aa", "ab") is False


def test_can():
    assert Solution().canConstruct("aa", "aab") is True


def test_empty_note():
    assert Solution().canConstruct("", "abc") is True


def test_same_string():
    assert Solution().canConstruct("abc", "abc") is True
