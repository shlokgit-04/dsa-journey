# 383. Ransom Note
# https://leetcode.com/problems/ransom-note/
# Easy | Hashing, Counting

from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        return not (Counter(ransomNote) - Counter(magazine))


if __name__ == "__main__":
    assert Solution().canConstruct("a", "b") is False
    assert Solution().canConstruct("aa", "ab") is False
    assert Solution().canConstruct("aa", "aab") is True
    print("ok")
