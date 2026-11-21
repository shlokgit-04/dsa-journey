"""LC 151: Reverse Words in a String (string) - Day 36, Sat Nov 21 2026."""
class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(s.split()[::-1])


def test():
    assert Solution().reverseWords("the sky is blue") == "blue is sky the"
    assert Solution().reverseWords("  hello world  ") == "world hello"
    assert Solution().reverseWords("a good   example") == "example good a"
    assert Solution().reverseWords("x") == "x"
    return "ok"
