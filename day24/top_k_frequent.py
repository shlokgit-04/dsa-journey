# 347. Top K Frequent Elements
# https://leetcode.com/problems/top-k-frequent-elements/
# Medium | Hash Table, Heap

from collections import Counter
import heapq
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        return [x for x, _ in heapq.nlargest(k, counts.items(), key=lambda p: p[1])]


if __name__ == "__main__":
    assert sorted(Solution().topKFrequent([1, 1, 1, 2, 2, 3], 2)) == [1, 2]
    print("ok")
