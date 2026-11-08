from fibonacci_number import Solution


def test_base_cases():
    assert Solution().fib(0) == 0
    assert Solution().fib(1) == 1


def test_small():
    assert Solution().fib(2) == 1
    assert Solution().fib(3) == 2


def test_ten():
    assert Solution().fib(10) == 55


def test_twenty():
    assert Solution().fib(20) == 6765


def test_matches_definition():
    s = Solution()
    for n in range(2, 15):
        assert s.fib(n) == s.fib(n - 1) + s.fib(n - 2)
