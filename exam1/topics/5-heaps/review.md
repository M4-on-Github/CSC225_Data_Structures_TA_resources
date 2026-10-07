# Topic 5 — Heaps

Confirm heap coverage with your instructor before prioritizing these exercises.

A **min-heap** is a complete binary tree in which every parent is no greater than its
children. It is **not** a sorted list. Store its levels from left to right in a list:

```text
          1
        /   \
       3     2
      / \   / \
     5   9 8   4
```

For zero-based index `i`, the parent is `(i−1)//2`; children are `2i+1` and `2i+2`.
Check that a child exists before reading it.

## Operations

| Operation | Worst-case cost | Reason |
|---|---|---|
| Peek at minimum | O(1) | Root is index 0 |
| Insert | O(log n) | Add at end, then sift up the tree |
| Remove minimum | O(log n) | Move last item to root, then sift down |
| Search for any value | O(n) | Separate branches are not ordered |
| Build heap bottom up | O(n) | Most sift-downs start near leaves |
| Heap sort | O(n log n) | Build once, then remove `n` items |

To remove the minimum on paper: save the root, move the **last** item to the root, then
repeatedly swap it with its **smaller** child until the heap property holds. Draw the
tree or write the list after each swap. Sift-up after insertion compares the new item
with its parent and stops when no swap is needed.

Repeated removals from a min-heap produce a new ascending list. An in-place ascending
heap sort uses a **max-heap**: move its largest root to the end, shrink the heap, and
sift down. Its worst-case time is O(n log n) and its auxiliary space is O(1).

## Check yourself

- Can you draw `[2, 5, 3, 9, 7, 8, 4]` as a tree and remove its minimum?
- Why does the heap property give no fast search for an arbitrary value?
- Why does an in-place ascending heap sort use a max-heap?

Try the [mock](mock.md) and [solutions](solutions.md). Code [MinHeap
practice](../../practice/p5_min_heap.py) before the [triage
queue](../../practice/p6_triage_queue.py).
