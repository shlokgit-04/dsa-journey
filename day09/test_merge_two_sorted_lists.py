from merge_two_sorted_lists import ListNode, merge_two_lists

def to_list(head):
    out = []
    while head:
        out.append(head.val)
        head = head.next
    return out

def test_basic():
    a = ListNode(1, ListNode(2, ListNode(4)))
    b = ListNode(1, ListNode(3, ListNode(4)))
    assert to_list(merge_two_lists(a, b)) == [1, 1, 2, 3, 4, 4]

def test_empty_first():
    assert to_list(merge_two_lists(None, ListNode(0))) == [0]

def test_empty_both():
    assert merge_two_lists(None, None) is None
