# Topic 5 — mock test: heaps

> ⚠ **Heap provenance.** The heap property and the three costs are Dr. Smith's
> (Deck 6 s32, s35). **The index arithmetic, the sift code, `build_heap` and both heap
> sorts are your TA's** — there is no heap deck in this course. Practice, not a prediction.
> Confirm with Dr. Smith that heaps are on the exam. Full explanation in
> [review.md](review.md).

Part 1 is eleven drills, Part 2 is five exam-style questions.

**Attempt everything before you open [solutions.md](solutions.md).** The answers are in
that file, in order, with a note on what a complete answer needs. Reading them first feels
like studying and is
not — the thing being examined is whether you can produce the answer, and you cannot
practise that by recognising one.

No time limit is printed here on purpose. Work until you are done, note how long it took,
and compare that with however long Dr. Smith gives you.

**Throughout:** write every heap as a **list**, index 0 first, exactly as the
implementation stores it. **No imports, no `heapq`, no `sort()`, no `sorted()`.**

---

## Part 1 — Drills

**5.1** State the heap property precisely. Then say what it does **not** tell you — compare
it with what being *sorted* tells you.

**5.2** Why is the list inside a heap not sorted, even though the smallest value is always
at index 0?

**5.3** Write the three index formulas, then apply them: a heap holds 10 items. For the item
at index 4, give the parent, left-child and right-child indices — and say which of those
actually exist.

**5.4** Same heap of 10 items: which indices are leaves, and how do you work that out
without drawing the tree?

**5.5** Insert 5, 3, 8, 1, 9, 2 into an empty min-heap, in that order. Write the final list.
Then insert 4 and say how many swaps it costs.

**5.6** From `[1, 3, 2, 5, 9, 8]`, call `remove_min()` twice. Write the list after each
call, and state the two steps `remove_min` takes before it sifts.

**5.7** `build_heap([9, 7, 5, 3, 1, 8, 2])` — write the resulting list. Then explain why
building a heap this way is **O(n)** while inserting the same seven values one at a time is
O(n log n).

**5.8** `build_heap([1, 2, 3, 4, 5])` returns `[1, 2, 3, 4, 5]`, unchanged. Is that a bug?
What does it tell you about the relationship between sorted lists and heaps?

**5.9** Costs for a min-heap of n items: (i) `peek` · (ii) `insert` · (iii) `remove_min` ·
(iv) finding out whether the value 42 is in the heap · (v) `build_heap` · (vi) `heap_sort`.

**5.10** Heap sort is O(n log n) with no best case and no worst case. Say why, and name one
situation where that makes it the right choice over quick sort.

**5.11** `heap_sort_in_place` sorts ascending using a **max**-heap, not a min-heap. Why does
sorting in place force that switch?

---

## Part 2 — Exam-style questions

### Q1 — Min-heaps
**(a)** State the **min-heap property**. Be careful about what it compares with what.

**(b)** A heap is a **complete** binary tree. Say what complete means, and why it lets
the tree live in a plain list with no node objects at all.

**(c)** A min-heap and an **unsorted list** both contain the minimum somewhere. Where
does the heap keep it, and what does finding the minimum cost in each?

### Q2 — Heap costs
The heap holds n items in a list.

**(a)** Fill in the table.

| Operation | Big-O |
|---|---|
| `peek()` | |
| `insert(element)` | |
| `remove_min()` | |
| `build_heap(values)` on n items | |
| `heap_sort(values)` on n items | |
| decide whether 42 is in the heap | |

**(b)** Where does the `log n` in `insert` come from? Name the property of the tree that
puts it there.

**(c)** Building a heap by calling `insert` n times costs O(n log n). `build_heap` does
the same job in **O(n)**. What does it do differently?

### Q3 — A min-heap by hand
Write the heap as a **list**, index 0 first, exactly as the implementation stores it.

**(a)** Insert `5, 3, 8, 1, 9, 2` into an empty min-heap, one at a time. Write the list
after each insert.

| Insert | The list after it |
|---|---|
| 5 | |
| 3 | |
| 8 | |
| 1 | |
| 9 | |
| 2 | |

**(b)** Now call `remove_min()` **twice** on the list you ended with. Write the list
after each call, and say which value came out.

**(c)** `build_heap([9, 7, 5, 3, 1, 8, 2])`. Give the index of the **last parent**, the
order in which indices are sifted, and the final list. Is that final list sorted?

### Q4 — Write the class
Complete the three missing methods on `MinHeap`. `__init__`, `size`, `is_empty` and
`to_list` are given; `_sift_up` is yours to write and is called only by `insert`.

```python
class MinHeap:
    def __init__(self):
        self._items = []

    def size(self):
        return len(self._items)

    def is_empty(self):
        return len(self._items) == 0

    def to_list(self):
        return list(self._items)

    def peek(self):
        # your code here

    def insert(self, element):
        # your code here

    def _sift_up(self, i):
        # your code here


# it must satisfy all of these
h = MinHeap()
assert h.peek() is None
for value in (5, 3, 8, 1, 9, 2):
    h.insert(value)
assert h.to_list() == [1, 3, 2, 5, 9, 8]
assert h.peek() == 1
assert h.size() == 6
```

**(a)** Write the three methods.

**(b)** Give the cost of `insert`, and justify it in one sentence about the shape of the
tree.

**(c)** Your `_sift_up` needs the parent of index `i`. Why `(i - 1) // 2`, and what does
it give for `i = 0`?

### Q5 — Applying a heap
An emergency room treats the **most urgent** waiting patient next. Patients arrive
constantly and are treated constantly, so both operations happen all day.

**(a)** Three designs. Give the cost of **adding a patient** and of **taking the next
patient** for each, then say which you would ship and why.

| Design | Add a patient | Take the next |
|---|---|---|
| A plain list, scanned for the most urgent when one is needed | | |
| A list kept sorted by urgency at all times | | |
| A min-heap keyed on urgency | | |

**(b)** The waiting room also wants a screen listing **every** waiting patient in
urgency order. Can it read that straight off the heap's list? If not, what must it do, and
what does that cost?

**(c)** Name one thing the sorted list gives you that the heap does not.

---

## Part 3 — Write the code

This topic has two practice problems:

- `practice/p5_min_heap.py` — the full `MinHeap`, the three index functions, `build_heap`,
  `heap_sort` and `heap_sort_in_place`, checked by `python test_p5_min_heap.py`. Q4 above is
  the paper version of its first third.
- `practice/p6_triage_queue.py` — Q5's emergency room, built for real, checked by
  `python test_p6_triage_queue.py`. Do it after problem 5; it imports from it.

Problem 6 is the one place in the package where you **apply** a data structure to a problem
rather than implement one, which is the shape Dr. Smith's note describes. The tie-breaking
part of it is the whole question — read its header carefully.
