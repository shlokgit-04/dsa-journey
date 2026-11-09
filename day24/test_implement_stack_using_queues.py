from implement_stack_using_queues import MyStack


def test_leetcode_example():
    s = MyStack()
    s.push(1)
    s.push(2)
    assert s.top() == 2
    assert s.pop() == 2
    assert not s.empty()


def test_lifo_order():
    s = MyStack()
    for x in [1, 2, 3]:
        s.push(x)
    assert [s.pop() for _ in range(3)] == [3, 2, 1]


def test_empty_flag():
    s = MyStack()
    assert s.empty()
    s.push(9)
    assert not s.empty()
    s.pop()
    assert s.empty()


def test_top_does_not_pop():
    s = MyStack()
    s.push(4)
    assert s.top() == 4
    assert s.top() == 4


def test_push_after_pop():
    s = MyStack()
    s.push(1)
    s.pop()
    s.push(2)
    assert s.top() == 2
