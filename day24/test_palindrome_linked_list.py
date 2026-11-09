from palindrome_linked_list import ListNode, Solution


def build(vals):
    head = None
    for v in reversed(vals):
        head = ListNode(v, head)
    return head


def test_even_palindrome():
    assert Solution().isPalindrome(build([1, 2, 2, 1])) is True


def test_odd_palindrome():
    assert Solution().isPalindrome(build([1, 2, 1])) is True


def test_not_palindrome():
    assert Solution().isPalindrome(build([1, 2])) is False


def test_single_node():
    assert Solution().isPalindrome(build([7])) is True


def test_longer():
    assert Solution().isPalindrome(build([1, 2, 3, 2, 1])) is True
