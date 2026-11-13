from day28.fizz_buzz import Solution


def test_three():
    assert Solution().fizzBuzz(3) == ["1", "2", "Fizz"]


def test_five():
    assert Solution().fizzBuzz(5) == ["1", "2", "Fizz", "4", "Buzz"]


def test_fifteen_has_fizzbuzz():
    assert Solution().fizzBuzz(15)[14] == "FizzBuzz"


def test_one():
    assert Solution().fizzBuzz(1) == ["1"]


def test_length():
    assert len(Solution().fizzBuzz(20)) == 20
