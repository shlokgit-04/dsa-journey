"""LC 414 Third Maximum Number (arrays/sorting).

Dedupe, sort descending; if fewer than 3 distinct values exist the
"third maximum" is defined as the maximum instead.
"""


class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        distinct = sorted(set(nums), reverse=True)
        return distinct[2] if len(distinct) >= 3 else distinct[0]
