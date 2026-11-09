# 234. Palindrome Linked List
# https://leetcode.com/problems/palindrome-linked-list/
# Easy | Linked List, Two Pointers

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        # find the middle
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # reverse the second half
        prev = None
        while slow:
            slow.next, prev, slow = prev, slow, slow.next
        # compare both halves
        while prev:
            if prev.val != head.val:
                return False
            prev = prev.next
            head = head.next
        return True


if __name__ == "__main__":
    head = ListNode(1, ListNode(2, ListNode(2, ListNode(1))))
    assert Solution().isPalindrome(head) is True
    print("ok")
