# Day 36 notes (Sat, 21 Nov 2026)

- LC 49 Group Anagrams: canonical key = sorted string; defaultdict of lists. O(n * k log k).
- LC 3 Longest Substring Without Repeating: last-seen index map with a moving start pointer; when a repeat is inside the current window (last[c] >= start), jump start past it. Classic off-by-one trap is resetting start to a stale index.
- LC 151 Reverse Words: s.split() already collapses runs of whitespace, so reverse + rejoin. One-liner, but worth knowing why it handles "  hello world  " cleanly.
