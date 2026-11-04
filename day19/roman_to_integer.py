"""LC 13 Roman to Integer (Easy, Hash Table).

Map each symbol to its value; when a smaller value precedes a larger
one (IV, IX, XL, XC, CD, CM) subtract it instead of adding.
"""
class Solution:
    VALUES = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    def romanToInt(self, s: str) -> int:
        total = 0
        for i, ch in enumerate(s):
            value = self.VALUES[ch]
            if i + 1 < len(s) and value < self.VALUES[s[i + 1]]:
                total -= value
            else:
                total += value
        return total
