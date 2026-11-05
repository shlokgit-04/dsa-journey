"""LC 206 Reverse Linked List (iterative three-pointer)."""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_list(head):
    prev = None
    cur = head
    while cur:
        nxt = cur.next
        cur.next = prev
        prev = cur
        cur = nxt
    return prev


class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        return reverse_list(head)


def to_list(values):
    head = None
    for v in reversed(values):
        head = ListNode(v, head)
    return head


def from_list(head):
    out = []
    while head:
        out.append(head.val)
        head = head.next
    return out
