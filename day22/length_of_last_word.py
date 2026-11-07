# 58. Length of Last Word
# https://leetcode.com/problems/length-of-last-word/
# Easy | String


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        parts = s.split()
        return len(parts[-1]) if parts else 0


if __name__ == "__main__":
    assert Solution().lengthOfLastWord("Hello World") == 5
    assert Solution().lengthOfLastWord("   fly me   to   the moon  ") == 4
    print("ok")
