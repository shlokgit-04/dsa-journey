from happy_number import Solution, digit_square_sum


def test_true_case():
    assert Solution().isHappy(19) is True


def test_false_case():
    assert Solution().isHappy(2) is False


def test_one():
    assert Solution().isHappy(1) is True


def test_seven():
    assert Solution().isHappy(7) is True


def test_digit_sum():
    assert digit_square_sum(199) == 1 + 81 + 81
