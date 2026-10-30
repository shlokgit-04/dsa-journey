from linked_list_cycle import ListNode, has_cycle


def list_to_nodes(values, pos):
    """pos: index the tail connects to, or -1."""
    nodes = [ListNode(v) for v in values]
    for a, b in zip(nodes, nodes[1:]):
        a.next = b
    if pos >= 0:
        nodes[-1].next = nodes[pos]
    return nodes[0] if nodes else None


def test_cycle_present():
    head = list_to_nodes([3, 2, 0, -4], 1)
    assert has_cycle(head) is True


def test_no_cycle_and_empty():
    assert has_cycle(list_to_nodes([1, 2], -1)) is False
    assert has_cycle(None) is False
