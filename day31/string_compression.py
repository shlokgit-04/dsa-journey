# 443. String Compression
# https://leetcode.com/problems/string-compression/
# Medium | Two Pointers, String


class Solution:
    def compress(self, chars: list[str]) -> int:
        write = 0
        read = 0
        n = len(chars)
        while read < n:
            group_start = read
            while read < n and chars[read] == chars[group_start]:
                read += 1
            chars[write] = chars[group_start]
            write += 1
            count = read - group_start
            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1
        return write


if __name__ == "__main__":
    chars = ["a", "a", "b", "b", "c", "c", "c"]
    assert Solution().compress(chars) == 6 and chars[:6] == ["a", "2", "b", "2", "c", "3"]
    chars = ["a"]
    assert Solution().compress(chars) == 1 and chars[:1] == ["a"]
    chars = ["a", "b", "b"]
    assert Solution().compress(chars) == 3 and chars[:3] == ["a", "b", "2"]
    print("ok")
