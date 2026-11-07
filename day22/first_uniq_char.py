# 387. First Unique Character in a String
# https://leetcode.com/problems/first-unique-character-in-a-string/
# Easy | Hash Table, String

from collections import Counter


class Solution:
    def firstUniqChar(self, s: str) -> int:
        counts = Counter(s)
        for i, ch in enumerate(s):
            if counts[ch] == 1:
                return i
        return -1


if __name__ == "__main__":
    assert Solution().firstUniqChar("leetcode") == 0
    assert Solution().firstUniqChar("aabb") == -1
    print("ok")
