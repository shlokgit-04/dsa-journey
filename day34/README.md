# Day 34 - Thu, 19 Nov 2026

Theme: DP basics + greedy + counting.

| LC | Problem | Difficulty | File | Idea |
|----|---------|-----------|------|------|
| 118 | Pascal's Triangle | Easy | pascals_triangle.py | row i from row i-1 |
| 119 | Pascal's Triangle II | Easy | pascals_triangle_ii.py | one rolling row, update right to left |
| 169 | Majority Element | Easy | majority_element.py | Boyer-Moore voting, O(1) space |
| 198 | House Robber | Medium | house_robber.py | rolling max(skip, rob) |
| 746 | Min Cost Climbing Stairs | Easy | min_cost_climbing_stairs.py | min of last two running totals |
| 55 | Jump Game | Medium | jump_game.py | greedy farthest-reach scan |
| 300 | Longest Increasing Subsequence | Medium | longest_increasing_subsequence.py | DP table + patience sorting O(n log n) |

Run tests: `python3 -m pytest day34/test_day34.py -q`
