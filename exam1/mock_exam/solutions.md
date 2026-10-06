# Mixed readiness check solutions

## 1 Shared state

Outputs: [2, 6], then [2]. Appending mutates a. Rebinding the function's local name does not replace a. The copy b is independent. Review [Python](../topics/1-python-review/review.md) if either distinction was unclear.

## 2 Count the work

n + n squared checks, so O(n squared). Consecutive blocks add; the larger term dominates. Review [complexity](../topics/2-big-o/review.md).

## 3 Choose a search

Use linear search: O(n) worst case. Binary search needs sorted input and may miss existing values without it. For one search, sorting first is unnecessary. Review [arrays and search](../topics/3-arrays/review.md).

## 4 Choose and explain a sort

Insertion sort scans the sorted prefix without shifts, then shifts larger values right to place the appended value. One added item causes at most n minus 1 shifts, so total work is O(n). The taught merge sort still splits and merges throughout the list. Review [sorting](../topics/4-sorting/review.md).

## 5 Write a method

```python
def is_sorted(self):
    for i in range(1, len(self.values)):
        if self.values[i - 1] > self.values[i]:
            return False
    return True
```

The method checks adjacent pairs and stops at the first decrease. With fewer than two items, there are no pairs to reject. Worst-case time is O(n), with O(1) extra space. Try [2, 2], [3, 1], [] and [7]. Then implement [problem 4](../practice/p4_sortable_list.py) if needed.

## 6 Optional heaps

Return 1. Pop the last value 5 and move it to the root: [5, 3, 2, 7]. Swap with the smaller child 2 to get [2, 3, 5, 7]. Moving the last item preserves the complete tree's gap-free layout. Review [heaps](../topics/5-heaps/review.md).

## Decide what to do next

For each missed or uncertain answer, review that area and solve a fresh variation without notes. For coding, explain each condition and run the relevant tests. If you remain stuck, bring your attempt and one specific question to your TA.
