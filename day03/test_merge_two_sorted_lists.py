from day03.merge_two_sorted_lists import ListNode, merge_two_lists, to_list


def build(vals):
    head = None
    for v in reversed(vals):
        head = ListNode(v, head)
    return head


def test_example_1():
    assert to_list(merge_two_lists(build([1, 2, 4]), build([1, 3, 4]))) == [1, 1, 2, 3, 4, 4]


def test_both_empty():
    assert to_list(merge_two_lists(None, None)) == []


def test_one_empty():
    assert to_list(merge_two_lists(None, build([0]))) == [0]
