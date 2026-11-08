from pascal_triangle import Solution


def test_five_rows():
    assert Solution().generate(5) == [
        [1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]
    ]


def test_one_row():
    assert Solution().generate(1) == [[1]]


def test_zero_rows():
    assert Solution().generate(0) == []


def test_two_rows():
    assert Solution().generate(2) == [[1], [1, 1]]


def test_row_sums_are_powers():
    rows = Solution().generate(8)
    assert [sum(r) for r in rows] == [2 ** i for i in range(8)]
