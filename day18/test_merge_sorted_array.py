from day18.merge_sorted_array import merge


def test_example():
    nums1, nums2 = [1, 2, 3, 0, 0, 0], [2, 5, 6]
    merge(nums1, 3, nums2, 3)
    assert nums1 == [1, 2, 2, 3, 5, 6]


def test_all_from_nums2():
    nums1, nums2 = [0], [1]
    merge(nums1, 0, nums2, 1)
    assert nums1 == [1]


def test_empty_nums2():
    nums1, nums2 = [1], []
    merge(nums1, 1, nums2, 0)
    assert nums1 == [1]


def test_reverse_order():
    nums1, nums2 = [4, 0, 0, 0, 0, 0], [1, 2, 3, 5, 6]
    merge(nums1, 1, nums2, 5)
    assert nums1 == [1, 2, 3, 4, 5, 6]


def test_interleaved():
    nums1, nums2 = [2, 3, 8, 0, 0, 0], [1, 5, 9]
    merge(nums1, 3, nums2, 3)
    assert nums1 == [1, 2, 3, 5, 8, 9]
