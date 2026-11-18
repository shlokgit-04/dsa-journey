# Day 33 - Wed, 18 Nov 2026

Theme: two pointers + prefix products.

Set: LC 15 3Sum, LC 238 Product of Array Except Self, LC 844 Backspace String Compare, 12 pytest cases in day33/.

- LC 15 3Sum: sort, fix the smallest element, two-pointer scan for the pair completing 0. Skip duplicate anchors and duplicate lefts so triples stay unique.
- LC 238 Product of Array Except Self: result starts as the left product per index, then one right-to-left pass folds in the running suffix. No division, O(1) extra.
- LC 844 Backspace String Compare: walk both strings from the end, skipping '#'s and dropping one real char per pending backspace, then compare survivors. O(1) space instead of rebuilding both strings.
