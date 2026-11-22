from day37.best_time_buy_sell_stock import Solution as BuyStock
from day37.maximum_subarray import Solution as MaxSub


def test_lc121_basic():
    assert BuyStock().maxProfit([7, 1, 5, 3, 6, 4]) == 5


def test_lc121_no_profit():
    assert BuyStock().maxProfit([7, 6, 4, 3, 1]) == 0


def test_lc121_late_dip():
    assert BuyStock().maxProfit([2, 4, 1]) == 2


def test_lc53_classic():
    assert MaxSub().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6


def test_lc53_single():
    assert MaxSub().maxSubArray([1]) == 1


def test_lc53_all_positive():
    assert MaxSub().maxSubArray([5, 4, -1, 7, 8]) == 23


from day37.climbing_stairs import Solution as Climb
from day37.binary_search import Solution as BinSearch


def test_lc70_base():
    assert Climb().climbStairs(1) == 1
    assert Climb().climbStairs(2) == 2


def test_lc70_known_values():
    assert Climb().climbStairs(3) == 3
    assert Climb().climbStairs(10) == 89


def test_lc704_found():
    assert BinSearch().search([-1, 0, 3, 5, 9, 12], 9) == 4
    assert BinSearch().search([5], 5) == 0


def test_lc704_missing():
    assert BinSearch().search([-1, 0, 3, 5, 9, 12], 2) == -1
    assert BinSearch().search([5], -5) == -1


from day37.invert_binary_tree import TreeNode as TN1, Solution as Invert
from day37.same_tree import TreeNode as TN2, Solution as Same


def _tree(vals):
    if not vals:
        return None
    nodes = [None] + [TN2(v) if v is not None else None for v in vals]
    for i in range(1, len(vals) // 2 + 1):
        nodes[i].left = nodes[2 * i] if 2 * i < len(nodes) else None
        nodes[i].right = nodes[2 * i + 1] if 2 * i + 1 < len(nodes) else None
    return nodes[1]


def test_lc226_swap_children():
    root = _tree([4, 2, 7, 1, 3, 6, 9])
    out = Invert().invertTree(root)
    assert out.val == 4 and out.left.val == 7 and out.right.val == 2
    assert out.left.left.val == 9 and out.left.right.val == 6
    assert out.right.left.val == 3 and out.right.right.val == 1


def test_lc226_empty():
    assert Invert().invertTree(None) is None


def test_lc100_same():
    assert Same().isSameTree(_tree([1, 2, 3]), _tree([1, 2, 3])) is True
    assert Same().isSameTree(None, None) is True


def test_lc100_different():
    assert Same().isSameTree(_tree([1, 2]), _tree([1, None, 2])) is False
