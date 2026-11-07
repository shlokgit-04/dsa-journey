from number_of_one_bits import Solution


def test_eleven():
    assert Solution().hammingWeight(11) == 3


def test_zero():
    assert Solution().hammingWeight(0) == 0


def test_all_ones_32bit():
    assert Solution().hammingWeight(4294967295) == 32


def test_power_of_two():
    assert Solution().hammingWeight(128) == 1


def test_alternating():
    assert Solution().hammingWeight(0b10101010) == 4
