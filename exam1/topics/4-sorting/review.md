# Topic 4 — Sorting

Understand each method's steps, trace it on paper, and derive its **worst-case** cost.
Use plain-language pseudocode for written sorting questions. The coding practice asks
you to implement the methods yourself without `sort()` or `sorted()`.

## Sorting comparison table

These costs and behavior refer to the versions in this package.

| Sort | Core steps | Worst case | In place? | Stable? |
|---|---|---|---|---|
| Selection | Find the smallest remaining item; swap it into place | O(n²) | Yes | No |
| Bubble | Compare neighbors; swap if out of order; repeat passes | O(n²) | Yes | Yes |
| Insertion | Shift larger items right; insert the next item | O(n²) | Yes | Yes |
| Merge | Split in half; merge sorted halves | O(n log n) | No | Yes |
| Quick | Choose last item as pivot; build smaller, equal, larger lists; recurse | O(n²) | No | Yes for this version |

**Stable** means equal keys stay in their original order. Here, selection, bubble, and
insertion change and return the original list. Merge and quick return a new list for
inputs of at least two items. The tests check this convention.

## Why the costs differ

Selection always compares `(n−1) + ... + 1` pairs. Bubble and insertion can each make
that much work on a reversed list. Merge makes O(n) work at each of O(log n) splitting
levels. Quick makes O(n) work per partition; if the last-item pivot is always an extreme
value, the remaining sizes are `n−1, n−2, ...`, giving O(n²).

To trace bubble sort, write the list after each full pass; the largest remaining value
reaches its final position. To trace merge or quick sort, draw the smaller sublists,
then show how they combine.

## Check yourself

- Can you write one sort's loops and decisions as pseudocode without copying code?
- Can you name an input that reaches each worst case and count its work?
- Can you explain why a returned new list differs from sorting the original list?

Try the [mock](mock.md) and [solutions](solutions.md). Code [sorting
functions](../../practice/p3_sorts.py), then the [sortable
list](../../practice/p4_sortable_list.py).
