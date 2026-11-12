from day27.reverse_linked_list import ListNode, reverse_list

def to_list(head):
    out = []
    while head:
        out.append(head.val)
        head = head.next
    return out

def from_list(vals):
    head = None
    for v in reversed(vals):
        head = ListNode(v, head)
    return head

def test_reverse_basic():
    assert to_list(reverse_list(from_list([1,2,3,4,5]))) == [5,4,3,2,1]

def test_reverse_two():
    assert to_list(reverse_list(from_list([1,2]))) == [2,1]

def test_reverse_empty():
    assert reverse_list(None) is None

def test_reverse_single():
    assert to_list(reverse_list(from_list([7]))) == [7]

def test_already_reversed_roundtrip():
    assert to_list(reverse_list(reverse_list(from_list([3,1,2])))) == [3,1,2]
