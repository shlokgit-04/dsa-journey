from day19.climbing_stairs import Solution


def test_base_cases():
    assert Solution().climbStairs(1) == 1
    assert Solution().climbStairs(2) == 2


def test_example():
    assert Solution().climbStairs(3) == 3
    assert Solution().climbStairs(4) == 5


def test_larger():
    assert Solution().climbStairs(10) == 89
