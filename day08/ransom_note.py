"""LC 383 Ransom Note (Easy) - Day 8

Can the note be built from magazine letters? Count each letter with
collections.Counter and check the note never exceeds the magazine's supply.
"""
from collections import Counter

def can_construct(ransom_note, magazine):
    need = Counter(ransom_note)
    have = Counter(magazine)
    return all(have[c] >= k for c, k in need.items())
