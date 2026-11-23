"""LC 242 Valid Anagram (Easy) - hashing.

One frequency counter, decrement for the second word.
O(n) time, O(1) space (26 lowercase letters).
"""


class Solution:
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        counts = {}
        for ch in s:
            counts[ch] = counts.get(ch, 0) + 1
        for ch in t:
            if counts.get(ch, 0) == 0:
                return False
            counts[ch] -= 1
        return True


if __name__ == "__main__":
    assert Solution().isAnagram("anagram", "nagaram")
    assert not Solution().isAnagram("rat", "car")
    assert Solution().isAnagram("", "")
    assert not Solution().isAnagram("ab", "a")
    print("ok")
