from implement_queue import MyQueue


def test_leetcode_example():
    q = MyQueue()
    q.push(1)
    q.push(2)
    assert q.peek() == 1
    assert q.pop() == 1
    assert not q.empty()


def test_empty_flag():
    q = MyQueue()
    assert q.empty()
    q.push(7)
    assert not q.empty()
    q.pop()
    assert q.empty()


def test_fifo_across_pushes():
    q = MyQueue()
    for x in [1, 2, 3]:
        q.push(x)
    assert [q.pop() for _ in range(3)] == [1, 2, 3]


def test_interleaved():
    q = MyQueue()
    q.push(1)
    assert q.pop() == 1
    q.push(2)
    q.push(3)
    assert q.pop() == 2


def test_peek_after_shift():
    q = MyQueue()
    q.push(5)
    q.push(6)
    assert q.peek() == 5
    assert q.peek() == 5
