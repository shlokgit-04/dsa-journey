from power_of_three import Solution


def test_27():
    assert Solution().isPowerOfThree(27) is True


def test_1():
    assert Solution().isPowerOfThree(1) is True


def test_zero():
    assert Solution().isPowerOfThree(0) is False


def test_negative():
    assert Solution().isPowerOfThree(-3) is False


def test_not_a_power():
    assert Solution().isPowerOfThree(45) is False
