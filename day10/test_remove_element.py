from day10.remove_element import remove_element


def test_basic():
    nums = [3, 2, 2, 3]
    k = remove_element(nums, 3)
    assert k == 2 and sorted(nums[:k]) == [2, 2]


def test_val_not_present():
    nums = [1, 2, 3]
    k = remove_element(nums, 9)
    assert k == 3 and nums[:k] == [1, 2, 3]


def test_all_match():
    nums = [4, 4, 4]
    k = remove_element(nums, 4)
    assert k == 0
