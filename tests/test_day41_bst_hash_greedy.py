import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "day41"))
from lc700_search_in_bst import Solution as S700, TreeNode
from lc219_contains_duplicate_ii import Solution as S219
from lc455_assign_cookies import Solution as S455

def n(v, l=None, r=None): return TreeNode(v, l, r)

def test_search_bst():
    root = n(4, n(2, n(1), n(3)), n(7))
    s = S700().searchBST(root, 2)
    assert s and s.val == 2 and s.left.val == 1 and s.right.val == 3
    assert S700().searchBST(root, 5) is None
    assert S700().searchBST(None, 1) is None
    one = S700().searchBST(n(1), 1)
    assert one and one.val == 1

def test_contains_nearby_duplicate():
    s = S219()
    assert s.containsNearbyDuplicate([1,2,3,1], 3) is True
    assert s.containsNearbyDuplicate([1,0,1,1], 1) is True
    assert s.containsNearbyDuplicate([1,2,3,1,2,3], 2) is False
    assert s.containsNearbyDuplicate([], 0) is False
    assert s.containsNearbyDuplicate([9,9], 0) is False
    assert s.containsNearbyDuplicate([99,99], 2) is True

def test_assign_cookies():
    s = S455()
    assert s.findContentChildren([1,2,3], [1,1]) == 1
    assert s.findContentChildren([1,2], [1,2,3]) == 2
    assert s.findContentChildren([10,9,8,7], [5,6,7,8]) == 2
    assert s.findContentChildren([], [1,2]) == 0
    assert s.findContentChildren([1], []) == 0
    assert s.findContentChildren([1,2,3], [3]) == 1
