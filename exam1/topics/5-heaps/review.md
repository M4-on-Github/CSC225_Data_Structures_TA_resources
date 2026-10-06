# Topic 5 — Heaps

> ## ⚠ Read this before you read the topic
>
> **There is no heap lecture deck in this course.** Deck 6 s32 says *"recall the central
> idea from our heap data structure lecture"* and states the heap **property** and three
> **costs** — peek O(1), insert O(log n), remove O(log n) — and s35 adds *"a heap list is
> not fully sorted. It only maintains the heap property."* **That is the entire
> slide-derived heap record for this course.**
>
> Everything else on these three pages — the index arithmetic, the sift-up and sift-down
> code, `build_heap`, both heap sorts — is **your TA's**, written to match his conventions.
> It is correct and it is executed by the practice tests. It is **not** a prediction of
> what he will ask. **Confirm with Dr. Smith that heaps are on the exam** before putting
> serious hours into this topic.
>
> Study it anyway if it is on: a heap is the cheapest structure that makes "give me the
> smallest, repeatedly" fast, and it is the one sort with no bad case.

**Source:** Deck 6 s32 and s35 only, plus authored material. **Lecture weight:** two
slides — but the only topic in the package with a coding problem *and* an applied design
problem.

---

## What this topic is

A heap is the topic that sounds hardest and is shortest. It is a **tree with no nodes in
it**: no `Node` class, no `left` and `right` attributes, nothing but a plain Python list
and three lines of arithmetic that say where a node's parent and children *would* be if
you drew it. Get the arithmetic right and the rest is two loops.

---

## The ideas, in the order they depend on each other

- **The heap property is the whole definition.** In a **min**-heap, every node is **less
  than or equal to both of its children**. That is it. Nothing is said about left versus
  right, and nothing about two nodes that are not parent and child. (Deck 6 s32.)
- **The property is local, so the list is not sorted.** `[1, 3, 2, 9, 7, 8, 5]` is a valid
  min-heap: check every parent against its children and it holds; read it left to right and
  it is plainly not in order. The **only** position you can read off directly is index 0.
  (Deck 6 s35.)
- **The tree is the arithmetic.** For the item at index `i`:
  `parent_index(i)` = `(i - 1) // 2`, `left_index(i)` = `2i + 1`,
  `right_index(i)` = `2i + 2`. Memorise these three. `parent_index(0)` comes out **−1**,
  because Python's `//` floors downward — which conveniently means "no parent", and is why
  `_sift_up` guards with `while i > 0`.
- **Every index formula must be checked against `size` before you use it.**
  `left_index(4)` is 9 and `right_index(4)` is 10; in a heap of ten items the indices run 0
  to 9, so that node has a left child and **no** right child. Forgetting this check is the
  single most common heap bug.
- **A heap is always a complete tree** — every level full except possibly the last, which
  fills left to right. That is not a nicety; it is what lets the list have no gaps, and it
  is why `remove_min` moves the **last** item to the root rather than promoting a child.
- **insert = append, then sift up.** Put the new item at the end, then while it is smaller
  than its parent, swap the two and follow it up. At most one swap per level, so
  **O(log n)** in the worst case — and often zero swaps.
- **remove_min = save the root, move the last item into index 0, then sift down.** Sifting
  down means: find the **smaller** of the two children, and if it is smaller than the item
  you are holding, swap and follow. **O(log n)**.
- **`build_heap` is O(n), and n inserts is not.** `build_heap` sifts **down** from the last
  parent back to index 0. About half of any heap is leaves, which do not move at all, and
  only the handful of nodes near the root can travel the full height. Inserting instead
  sifts **up** from the bottom, where every one of the n items can climb the whole way:
  **O(n log n)**. Same heap, opposite direction, different cost.
- **A heap gives you no search.** `peek` is O(1) and `remove_min` is O(log n), but asking
  "is 42 in here?" is a linear scan: **O(n)**, exactly as bad as an unsorted list. A heap is
  a priority structure, not a lookup structure.
- **Heap sort is O(n log n) with no best case and no worst case.** Build the heap, then
  drain it. The work is fixed by the **shape** of a complete tree, not by the order of the
  values — which is the one thing quick sort cannot promise.
- **Sorted implies heap; heap does not imply sorted.** `build_heap([1, 2, 3, 4, 5])` returns
  the list unchanged, because an ascending list already satisfies the property. The
  implication runs one way only, and the exam asks it in the direction that is false.

---

## The picture

The list `[1, 3, 2, 5, 9, 8, 4]` is this tree:

```
index:      0
value:      1
          /   \
         3     2          indices 1, 2
        / \   / \
       5   9 8   4        indices 3, 4, 5, 6
```

Read the list and the tree side by side until the arithmetic is obvious: index 1's children
are 2·1+1 = 3 and 2·1+2 = 4, holding 5 and 9, and 3 ≤ both. Note `9` sits in front of `8`
and `4` in the list and nothing is wrong — none of them is its child.

---

## The costs

> *Heap provenance:* the three costs below marked (s32) are Dr. Smith's. The rest follow
> from the authored implementation.

| Operation | Cost | Why |
|---|---|---|
| `peek()` | **O(1)** (s32) | the minimum is at index 0, always |
| `insert(e)` | **O(log n)** (s32) | append at the end, then sift up at most one level per height |
| `remove_min()` | **O(log n)** (s32) | last item into index 0, then sift down one level at a time |
| `size()` / `is_empty()` | O(1) | it is the length of the list |
| is the value 42 in here? | **O(n)** | a heap gives you no search — you scan the list, like an unsorted list |
| `build_heap(values)` | **O(n)** | sift down from the last parent; about half the heap are leaves and never move |
| `heap_sort(values)` | O(n log n) | one O(n) build plus n removals of O(log n) — no best case, no worst case |

The search row is the one that separates understanding from memorising. **O(log n)** there
is the answer of someone who thinks a heap is a search tree.

---

## The code

Authored for this package, in his conventions. The full reference is
`practice/solutions/p5_min_heap.py`; this is the part worth being able to reproduce.

```python
def parent_index(i):
    return (i - 1) // 2          # -1 for the root, which is what we want


def left_index(i):
    return 2 * i + 1


def right_index(i):
    return 2 * i + 2


class MinHeap:

    def __init__(self):
        self._items = []

    def size(self):
        return len(self._items)

    def is_empty(self):
        return len(self._items) == 0

    def peek(self):
        if self.is_empty():
            return None          # his convention: None, not an exception
        return self._items[0]

    def insert(self, element):
        self._items.append(element)
        self._sift_up(len(self._items) - 1)

    def remove_min(self):
        if self.is_empty():
            return None
        smallest = self._items[0]
        last = self._items.pop()
        if not self.is_empty():
            self._items[0] = last        # the LAST item, not a child
            self._sift_down(0)
        return smallest

    def _sift_up(self, i):
        while i > 0:                     # the root has no parent
            p = parent_index(i)
            if self._items[i] < self._items[p]:
                self._items[i], self._items[p] = self._items[p], self._items[i]
                i = p                    # follow it up — do NOT move this out of the if
            else:
                break                    # parent is smaller: we are done

    def _sift_down(self, i):
        n = len(self._items)
        while True:
            left = left_index(i)
            right = right_index(i)
            smallest = i
            if left < n and self._items[left] < self._items[smallest]:
                smallest = left          # "left < n" is the size check
            if right < n and self._items[right] < self._items[smallest]:
                smallest = right
            if smallest == i:
                break
            self._items[i], self._items[smallest] = self._items[smallest], self._items[i]
            i = smallest
```

```python
def build_heap(values):
    heap = MinHeap()
    heap._items = list(values)
    start = parent_index(len(heap._items) - 1)    # the last parent
    for i in range(start, -1, -1):                # backwards to the root
        heap._sift_down(i)
    return heap


def heap_sort(values):
    heap = build_heap(values)
    result = []
    while not heap.is_empty():
        result.append(heap.remove_min())
    return result                                 # a NEW list, like merge and quick
```

**`_sift_down`'s `while True` loop is where recursion would otherwise go.** Sifting down is
naturally "swap, then sift the child" — a recursive step — and this is the iterative way to
write the same thing. That is the only place in the package worth comparing the two, and it
is why recursion gets no section of its own.

---

## Why heap sort is the sort with no bad case

Every input costs the same, because the work is fixed by the **shape** of the heap and not
by the order of the values: n removals, each climbing at most the height of a complete
tree. Quick sort averages the same but degrades to **O(n²)** on a bad pivot, which for
Dr. Smith's last-element pivot means already-sorted input ([Topic 4](../4-sorting/review.md)).

And there is an in-place version. `heap_sort_in_place` sorts ascending using a **max**-heap,
and the switch is forced, not a choice: sorting in place means the sorted values accumulate
inside the same list, and the only free slot at each step is **the end**. The value that
belongs at the end is the **largest**, and the only value a heap hands you cheaply is the
one at the root — so the root has to be the largest. Swap it to the end, shrink the heap by
one, sift down, repeat. A min-heap would build the list backwards.

That makes it the only sort in this course that is **O(n log n) *and* in place**. What you
give up is stability.

---

## How he says it

| | |
|---|---|
| "A heap is a binary tree where each parent is smaller than (or equal to) its children." | Deck 6 s32 |
| "A heap list is not fully sorted. It only maintains the heap property." | Deck 6 s35 |
| "Insert O(log n), remove-min O(log n), peek O(1)." | Deck 6 s32 |
| "Python's heapq gives you this for free — but you should know what it is doing." | Deck 6 s34 |

Those four lines are the whole of his heap record. Everything else here is authored.

---

## Where people go wrong

- Saying a heap is sorted, or that the property reaches further than it does. It is **parent
  to child only** — nothing about left versus right, nothing about two nodes that are not
  parent and child. His s35 exists because this is the mistake.
- Sifting down by swapping with the **larger** child. It must be the smaller one, or the
  heap is broken and the next `remove_min` returns a wrong value.
- In `remove_min`, promoting a child into the root instead of moving the **last** item
  there. It gives the right answer on some inputs, which is why it survives a weak test,
  and it breaks completeness on the rest.
- Writing `i = p` **outside** the `if` in `_sift_up`, so the loop keeps swapping all the way
  to the root.
- Using `left_index(i)` or `right_index(i)` without checking it against the size first.
- Claiming `build_heap` is O(n log n) because it "does n sift-downs". It does, but most of
  them move nothing — the total is **O(n)**, and the reason matters more than the number.
- Saying a heap can find an arbitrary value quickly. It cannot: **O(n)**.
- Writing `i // 2` for the parent. That is the 1-indexed formula; this list is 0-indexed.

---

## Checklist

- [ ] State the min-heap property exactly, and what it does **not** say — Deck 6 s32
- [ ] "A heap list is not fully sorted" — Deck 6 s35
- [ ] The three index formulas, and `parent_index(0)` = −1 — authored **+**
- [ ] Complete tree: what it means and why the list has no gaps — authored **+**
- [ ] Trace six inserts and two `remove_min`s by hand, writing the list each time — **+**
- [ ] `build_heap`, its sift order, and why it is O(n) while n inserts is O(n log n) — **+**
- [ ] The full cost table, including search at O(n) — costs s32, the rest **+**
- [ ] Heap sort's no-best-no-worst argument, and why in place needs a max-heap — **+**

**+** flags an item that is **authored by your TA**, not drawn from a lecture deck. Those
items are correct and tested; they are not evidence about the exam.

---

## Next

- Work [mock.md](mock.md) with this page closed, then check yourself against
  [solutions.md](solutions.md).
- Write the code: `practice/p5_min_heap.py` (the class, `build_heap`, both heap sorts) and
  then `practice/p6_triage_queue.py` (applying it to a real problem), checked by
  `python test_p5_min_heap.py` and `python test_p6_triage_queue.py`.
- That is the end of the package. If you have time left over, go back to
  `practice/p3_sorts.py` — on the evidence of the slides, sorting is the likelier coding
  question.
