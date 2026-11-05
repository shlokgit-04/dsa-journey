from majority_element import Solution

s = Solution()


def test_example():
    assert s.majorityElement([3, 2, 3]) == 3


def test_example_two():
    assert s.majorityElement([2, 2, 1, 1, 1, 2, 2]) == 2


def test_single():
    assert s.majorityElement([1]) == 1


def test_tail_shift():
    assert s.majorityElement([5, 5, 5, 1, 2]) == 5
