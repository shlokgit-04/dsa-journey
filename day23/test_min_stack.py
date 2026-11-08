from min_stack import MinStack


def test_leetcode_example():
    s = MinStack()
    s.push(-2)
    s.push(0)
    s.push(-3)
    assert s.getMin() == -3
    s.pop()
    assert s.top() == 0
    assert s.getMin() == -2


def test_min_updates_on_push():
    s = MinStack()
    s.push(5)
    s.push(1)
    assert s.getMin() == 1
    s.push(3)
    assert s.getMin() == 1


def test_min_restores_on_pop():
    s = MinStack()
    s.push(2)
    s.push(1)
    s.pop()
    assert s.getMin() == 2


def test_duplicates():
    s = MinStack()
    s.push(4)
    s.push(4)
    s.pop()
    assert s.getMin() == 4


def test_negative_values():
    s = MinStack()
    s.push(-10)
    s.push(-20)
    assert s.getMin() == -20
