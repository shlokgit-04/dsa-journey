"""LC 13: Roman to Integer (hashing / lookahead).

A numeral subtracts when it is smaller than the one after it (IV = 4).
Scan left to right: add the value, and subtract double when a smaller
numeral precedes a bigger one.
"""
VALUES = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

def roman_to_int(s: str) -> int:
    total = 0
    for i, ch in enumerate(s):
        value = VALUES[ch]
        if i + 1 < len(s) and value < VALUES[s[i + 1]]:
            total -= value
        else:
            total += value
    return total
