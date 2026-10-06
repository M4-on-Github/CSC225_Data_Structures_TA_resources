# Quick reference

Use after practice; close this page during readiness checks.

- **Mutation** changes an object. **Rebinding** changes which object a name refers to.
- **Sequential work** adds; nested loops multiply their iteration counts when each repeats fully.
- **Size** counts stored items; **capacity** counts reserved slots.
- **Binary search** requires sorted input. It checks O(log n) middle positions in the worst case; linear search checks O(n) items.
- **Amortized O(1) append** permits occasional O(n) copies. With geometric growth, n appends from empty take O(n) total.
- **In place** means constant auxiliary space here. Returning the same list is a separate exercise convention.
- **Stable sorting** preserves the order of records with equal comparison keys.
- [Sorting comparison table](topics/4-sorting/review.md#the-summary-table): use the exact implementations taught here.
- **Min-heap**: each parent is no greater than either child. Parent `(i - 1) // 2`; children `2*i + 1`, `2*i + 2`. Guard the root and missing children.

Return to [study paths](study_paths.md) for your next activity.
