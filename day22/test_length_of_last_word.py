from length_of_last_word import Solution


def test_basic():
    assert Solution().lengthOfLastWord("Hello World") == 5


def test_trailing_spaces():
    assert Solution().lengthOfLastWord("   fly me   to   the moon  ") == 4


def test_single_word():
    assert Solution().lengthOfLastWord("luffy") == 5


def test_empty():
    assert Solution().lengthOfLastWord("") == 0


def test_spaces_only():
    assert Solution().lengthOfLastWord("   ") == 0
