"""LC 21 Merge Two Sorted Lists (Easy) - Day 9

Splice two sorted linked lists with a dummy head: tie the smaller
node each step, then attach the remainder.
O(n + m) time, O(1) space (relinks nodes, allocates only the dummy).
"""
from dataclasses import dataclass

@dataclass
class ListNode:
    val: int
    next: "ListNode | None" = None

def merge_two_lists(list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
    dummy = tail = ListNode(0)
    a, b = list1, list2
    while a and b:
        if a.val <= b.val:
            tail.next, a = a, a.next
        else:
            tail.next, b = b, b.next
        tail = tail.next
    tail.next = a or b
    return dummy.next
