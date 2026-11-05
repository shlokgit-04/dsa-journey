from reverse_linked_list import Solution, to_list, from_list

s = Solution()


def test_example():
    assert from_list(s.reverseList(to_list([1, 2, 3, 4, 5]))) == [5, 4, 3, 2, 1]


def test_empty():
    assert s.reverseList(None) is None


def test_single():
    assert from_list(s.reverseList(to_list([1]))) == [1]


def test_two():
    assert from_list(s.reverseList(to_list([1, 2]))) == [2, 1]
