# Topic 5 — solutions: heaps

> ⚠ **Heap provenance.** The heap property and the three costs are slide-derived
> (Deck 6 s32, s35). **Everything else below — the index arithmetic, the sift code,
> `build_heap`, both heap sorts and every trace — is your TA's**, written to the course
> conventions. There is no heap deck in this course. Practice, not a prediction. Full
> explanation in [review.md](review.md).

Answers to [mock.md](mock.md), in order, each followed by what a complete answer needs.
**Attempt the paper first.** Every heap list in this file was produced by running
`practice/solutions/p5_min_heap.py`, not written from memory.

---

## Part 1 — Drills

**5.1** For **every** node, the node's value is **less than or equal to both of its
children**. That is all. It says **nothing** about left versus right, and nothing about the
order of two nodes that are not parent and child. A sorted structure pins down the order of
every pair; a heap pins down only parent-to-child. That is exactly why a heap is cheap to
maintain and why it cannot answer "what is the 3rd smallest" in one step. (Deck 6 s32 is the slide-derived
statement of the property; the comparison is your TA's.)

**5.2** Because the property is **local**. `[1, 3, 2, 9, 7, 8, 5]` is a perfectly valid
min-heap — every parent is ≤ its children — and it is not in sorted order. The slides on
s35: *"a heap list is not fully sorted. It only maintains the heap property."* Index 0 is
the only position you can read off directly. (Deck 6 s35.)

**5.3** `parent_index(i)` = **`(i - 1) // 2`** · `left_index(i)` = **`2i + 1`** ·
`right_index(i)` = **`2i + 2`**. For index 4: parent **1**, left child **9**, right child
**10**. Ten items occupy indices 0–9, so the **right child does not exist** — index 4 has
one child. Every index formula has to be checked against `size` before you use it, and that
check is the bug students leave out. (Index arithmetic authored for this package.)

**5.4** The last item sits at index 9, so the **last parent** is `parent_index(9)` = **4**.
Everything after it — indices **5, 6, 7, 8, 9** — is a leaf. Roughly half of any heap is
leaves, which is the whole reason `build_heap` is cheap. (Authored.)

**5.5** **`[1, 3, 2, 5, 9, 8]`**. Inserting 4 appends it at index 6, whose parent is index
`(6-1)//2` = 2 holding **2**; 4 is not smaller than 2, so it stops — **zero swaps** —
giving `[1, 3, 2, 5, 9, 8, 4]`. Insert is O(log n) in the **worst** case, not every case.
(Authored; the property is Deck 6 s32.)

**5.6** After the first: **`[2, 3, 8, 5, 9]`** (returned 1). After the second:
**`[3, 5, 8, 9]`** (returned 2). The two steps: **save the root**, then **move the last item
into index 0** — that keeps the tree complete, which is the one shape rule a heap cannot
break. Only then does `_sift_down(0)` run. (Authored.)

**5.7** **`[1, 3, 2, 9, 7, 8, 5]`**. `build_heap` sifts **down** from the last parent back
to index 0. Sifting down is cheap for the many nodes near the bottom — about half the heap
are leaves and move not at all — and only the handful of nodes near the root can travel
log n levels, so the total is **O(n)**. Inserting instead sifts **up** from the bottom,
where every one of the n items can climb the full height. Same heap, different direction,
different cost. (Authored; the result is the classic heap result.)

**5.8** Not a bug. **Every sorted list is already a valid min-heap** — if the list is
ascending then `values[i] <= values[2i+1]` and `values[2i+2]` automatically. So sorted ⇒
heap, but **heap ⇏ sorted**. The implication runs one way only, and the exam asks it in the
direction that is false. (Authored.)

**5.9** (i) **O(1)** — it is index 0 · (ii) **O(log n)** · (iii) **O(log n)** · (iv)
**O(n)** — a heap gives you no search; you scan the list · (v) **O(n)** · (vi)
**O(n log n)** — one build, then n removals of O(log n) each. (The three heap costs are
Deck 6 s32; the rest follow from them.)

**5.10** Every input costs the same because the work is fixed by the **shape** of the heap,
not by the order of the values: n removals, each climbing at most the height of a complete
tree. Quick sort averages the same but degrades to **O(n²)** on a bad pivot, which for
the last-element pivot means already-sorted input. So when you cannot afford a worst
case — and especially when you also cannot afford merge sort's second list, since
`heap_sort_in_place` needs none — heap sort is the safe pick. (Authored; the quick sort half
is Deck 7 s23.)

**5.11** Sorting in place means the sorted values accumulate inside the same list, and the
only free slot at each step is **the end**. The value that belongs at the end is the
**largest**, and the only value a heap hands you cheaply is the one at the root — so the
root has to be the largest. Swap it to the end, shrink the heap by one, sift down, repeat. A
min-heap would build the list backwards. (Authored.)

---

## Part 2 — Exam-style questions

### Q1 — Min-heaps
**(a)** **Every node is less than or equal to both of its children.** Nothing is promised
about left versus right, and nothing is promised between cousins — the property is
**local**. It follows that the **minimum is at the root**, which is what makes `peek` O(1).
(Deck 6 s32.)

**(b)** **Complete** = every level is full except possibly the last, and the last fills
**left to right** with no gaps. No gaps means the nodes map onto list indices `0, 1, 2, …`
with nothing skipped, so a parent and its children can be found by **arithmetic** instead of
by following stored references: `left = 2i + 1`, `right = 2i + 2`, `parent = (i − 1) // 2`.

**(c)** The heap keeps it **at the root — index 0**, so finding it is **O(1)**: you read one
slot, you do not search. In an unsorted list the minimum can sit anywhere, so you must look
at all n slots — **O(n)**. That is the trade the heap makes: it pays O(log n) on every
insert and every removal to keep index 0 true, and it buys **only** that. Asking a heap
whether 42 is somewhere inside it is still an O(n) scan.

**What a complete answer needs**

- (a) Parent ≤ **both** children. "Smallest at the top" is the *consequence*, not the
  property. Any answer that compares left with right is wrong — the property says nothing
  about siblings.
- (b) No-gaps / left-to-right **and** the arithmetic. The index formulas need not be exact
  here; this is the concept question and Q3 is the one that tests the arithmetic.
- (c) Index 0 with **O(1)**, and the **O(n)** scan of the unsorted list. Adding that the
  heap still cannot search for anything other than the minimum answers Q2(a)'s last cell
  early.

### Q2 — Heap costs
**(a)**

| Operation | Big-O |
|---|---|
| `peek()` | **O(1)** |
| `insert(element)` | **O(log n)** |
| `remove_min()` | **O(log n)** |
| `build_heap(values)` on n items | **O(n)** |
| `heap_sort(values)` on n items | **O(n log n)** |
| decide whether 42 is in the heap | **O(n)** |

(The first three are Deck 6 s32.)

The last one is the one to think about: a heap has **no ordering you can search by**. The
only thing you know about `42` is that if the root is bigger than 42 it is absent;
otherwise you check **every** item. A heap is a bad structure for *"is this in there?"* and
that is the price of `peek` being free.

**(b)** From the tree's **height**. A heap is a **complete** binary tree, so its height is
⌊log₂ n⌋ — doubling the number of items adds **one** level. `insert` appends at the end and
sifts the new element **up**, swapping it with its parent at most once per level, so the
work is proportional to the height.

**(c)** `build_heap` **sifts down** from the **last parent** backwards to index 0, instead
of sifting n new elements up from the bottom. The difference is where the nodes are:
**half** the nodes are leaves and sift down zero levels, a quarter sift down at most one,
and only the single root can travel the full log n. That sum comes to **O(n)**. Sifting *up*
has it backwards — it makes the many nodes at the bottom do the long walk.

**What a complete answer needs**

- (a) All six cells.
- The search cell is the one that separates understanding from memorising. **O(log n)**
  there is the answer of someone who thinks a heap is a search tree, and it is the single
  most common heap mistake. The heap property is local; it tells you nothing about where a
  given value is.
- O(n log n) for `build_heap` is wrong but reasonable — it is the cost of n inserts, and
  (c) is where that gets corrected.
- (b) Height **and** complete-tree. "Because it halves" works if the halving is clearly
  the tree, not the list.
- (c) Sifting **down** from the last parent. The leaf-counting argument is the explanation
  rather than the answer — getting it means you understood more than the question asked.

### Q3 — A min-heap by hand
**(a)**

| Insert | The list after it |
|---|---|
| 5 | `[5]` |
| 3 | `[3, 5]` |
| 8 | `[3, 5, 8]` |
| 1 | `[1, 3, 8, 5]` |
| 9 | `[1, 3, 8, 5, 9]` |
| 2 | **`[1, 3, 2, 5, 9, 8]`** |

The two that do work are **1** and **2**. Inserting `1` appends it at index 3, whose parent
is index 1 — it swaps past `5`, then past `3`, and lands at the root. Inserting `9` appends
at index 4, whose parent is index 1 holding `3`; `9 > 3`, so it **stops immediately** and
nothing moves. Inserting `2` appends at index 5, parent index 2 holding `8`, so it swaps up
one level and then stops under the root.

**(b)** First call returns **1** and leaves `[2, 3, 8, 5, 9]`. Second call returns **2** and
leaves `[3, 5, 8, 9]`.

Walk the first one: take `1` off the root, `pop()` the **last** item `8` and put it at the
root → `[8, 3, 2, 5, 9]`, then sift it **down**, always swapping with the **smaller** child.
Index 0's children are `3` and `2`; the smaller is `2`, so they swap → `[2, 3, 8, 5, 9]`,
and index 2 has no children, so it stops. Swapping with the *larger* child breaks the heap
on the next line.

**(c)** The last item is at index 6, so the **last parent** is `(6 − 1) // 2 = 2`. The sift
order is **2, 1, 0** — backwards to the root. Final list: **`[1, 3, 2, 9, 7, 8, 5]`**.

**No, it is not sorted**, and it never will be. The heap property only constrains each node
against **its own children**, so `9` sits happily at index 3 in front of `7`, `8` and `5` —
none of them is its child. The slides again: *"a heap list is not fully sorted. It only
maintains the heap property."* (Deck 6 s35.)

**What a complete answer needs**

- (a) All six rows.
- Rows 1–3 are free. Row 4 (`[1, 3, 8, 5]`) is the first that needs a two-level sift up.
  Row 5 is the trap: `9` moves **nothing**, and anyone who has memorised "inserts bubble
  up" will move it.
- `[1, 3, 2, 5, 9, 8]` as the last row is the most important cell in the question — it is
  the list that (b) and the practice tests both start from.
- (b) Both calls, each needing **both** the value returned and the list left behind.
- The common error is promoting the smaller **child** into the root instead of moving the
  **last** item there first. That gives `[2, 3, 8, 5, 9]` here too, by luck, so check your
  working rather than your answer. The second call, `[3, 5, 8, 9]`, is where the shortcut
  breaks.
- (c) Index **2**, the order **2, 1, 0**, the final list, and "not sorted".
- Index 3 for the last parent (i.e. `n // 2`) is the off-by-one to expect; sifting index 3
  does nothing, so the final list can still come out right while the reasoning is wrong.

### Q4 — Write the class
**(a)**

```python
    def peek(self):
        if self.is_empty():
            return None
        return self._items[0]

    def insert(self, element):
        self._items.append(element)
        self._sift_up(len(self._items) - 1)

    def _sift_up(self, i):
        while i > 0:
            p = (i - 1) // 2
            if self._items[i] < self._items[p]:
                self._items[i], self._items[p] = self._items[p], self._items[i]
                i = p
            else:
                break
```

`insert` does the only two things it can: **put the element in the one slot that keeps the
tree complete** (the end of the list), then **repair the one thing that might now be
broken** (the path from that slot to the root). Nothing else in the heap can have been
affected.

The two halves of the `while` are both load-bearing. `i > 0` stops at the root, which has no
parent. The `break` in the `else` stops the moment the element is bigger than its parent —
without it you keep walking to the root pointlessly, and if you moved `i = p` outside the
`if` you would keep *swapping* and destroy the heap.

`peek` returns **`None`** on an empty heap rather than raising, which is the convention used
all through this course.

**(b)** **O(log n).** A heap is a **complete** binary tree, so its height is ⌊log₂ n⌋;
`_sift_up` swaps at most once per level on the single path from the new leaf to the root, so
the work is proportional to the height and not to n.

**(c)** The children of index `p` are at `2p + 1` and `2p + 2`. Inverting either one lands
on `p`: `(2p + 1 − 1) // 2 = p`, and `(2p + 2 − 1) // 2 = (2p + 1) // 2 = p` because the
floor division throws the remainder away. That is why **one** formula works for both
children.

For `i = 0` it gives `(0 − 1) // 2 = −1`, since Python floors **towards negative infinity**
rather than truncating. `-1` is not a valid index to compare against — it is the last
item — which is precisely why `_sift_up` is guarded by `while i > 0` and never asks for the
root's parent.

**What a complete answer needs**

Seven things in the code:

- **Class form** — all three methods read and write `self._items`, signatures exactly as
  given, `insert` calls `self._sift_up`, no globals and no extra parameters. A correct heap
  written as three free functions over a list is working code that answers a different
  question.
- `peek` returns `None` when empty. Raising, returning `-1` or `0`, or reading
  `self._items[0]` with no guard all break the convention.
- `peek` returns `self._items[0]` and does **not** remove it.
- `insert` appends **then** sifts, with the index of the **new last element**.
  `self._sift_up(len(self._items))` is off by one; sifting before appending sifts the wrong
  list.
- `_sift_up` computes the parent as `(i - 1) // 2`. `i // 2` is the 1-indexed formula.
- The loop is guarded against the root — `while i > 0`, or an equivalent
  `if i == 0: return`.
- It stops climbing once the parent is smaller, and reassigns `i = parent` **only** when it
  swapped. Climbing unconditionally can still come out right on this test input, which is
  exactly why it survives a weak test.
- A **max**-heap, correct in every other way, has the class form and the structure right
  and only the comparison backwards — a small fix, not a rewrite.
- (b) **O(log n)**, *and* height-of-a-complete-tree as the reason. "Because it halves the
  list" is the wrong mechanism — nothing here halves a list.
- (c) Either inverting `2p + 1` / `2p + 2`, or a worked numeric check on two or three
  indices. "−1 for `i = 0`, which is why the loop guards against it" is the whole idea.

### Q5 — Applying a heap
**(a)**

| Design | Add a patient | Take the next |
|---|---|---|
| A plain list, scanned when one is needed | **O(1)** *(append)* | **O(n)** *(scan every patient, then remove)* |
| A list kept sorted by urgency at all times | **O(n)** *(find the slot, shift everything after it)* | **O(1)** *(the most urgent is at one known end)* |
| A min-heap keyed on urgency | **O(log n)** | **O(log n)** |

**Ship the heap.** It is the only one of the three where **both** operations are
sub-linear, and the question says both happen constantly. The other two are each excellent
at one operation and linear at the other, so whichever you choose, the ER spends its day in
the O(n) half. A heap is slightly worse than either at that one operation and far better
than either overall — that trade is the answer. (Deck 6 s30, s32: *"a heap gives us exactly
the operations a priority queue needs."*)

**(b)** **No.** The heap property is **local** — each node is only ordered against its own
children — so the list is in heap order, not sorted order. Only index 0 is guaranteed to be
anything in particular. Reading it top to bottom and calling it a treatment order would put
patients on that screen in the wrong order, which is the kind of bug that reaches the
newspaper.

To get the real order it must **copy the heap and drain the copy** with repeated
`remove_min()` — n removals at O(log n) each, so **O(n log n)**. That is heap sort, and it
is where heap sort comes from. The copy matters: draining the live heap empties the waiting
list. (Deck 6 s35: *"a heap list is not fully sorted."*)

**(c)** Any of: the **k-th most urgent** patient directly by index, in O(1) — a heap cannot
find its own second-smallest without work; the **whole order for free**, with no draining;
**binary search**, which needs the total order a heap does not have; or the **least** urgent
patient in O(1), which in a min-heap is somewhere among the leaves.

**What a complete answer needs**

- (a) All six cells, plus the choice **and** its reason.
- Sorted-list **add O(n)** is the cell most often wrong: the usual answer is O(log n),
  which is the cost of **finding** the slot by binary search and forgets the **shift**. The
  search is O(log n); the insertion is still O(n).
- Plain-list **take** must be O(n). O(1) means you forgot the scan.
- Choosing the heap with no reason is half an answer. Choosing the **sorted list** and
  arguing it well — arrivals batched overnight, treatment constant — is a good answer to a
  different question than the one asked.
- (b) **No — the property is local, the list is not sorted**, and then: drain a **copy**
  with repeated removals, at O(n log n).
- Forgetting the copy still earns the right Big-O and empties the live waiting list. It is
  the difference between printing a report and causing an outage.
- (c) Any one correct capability. The k-th item and binary search are the two strongest
  answers.

---

## If you got it wrong

- Anything wrong in **Q1(a) or Q2(a)'s last cell** — those two are the heap. The property is
  local, and a heap cannot search. Everything else in the topic follows from them.
- Anything wrong in **Q3** — redo the trace, then check it with `to_list()` in
  `practice/solutions/p5_min_heap.py`. Paper first, code second; the point is to find out
  where your version diverges.
- Anything wrong in **Q4** — write the whole class: `practice/p5_min_heap.py`, checked by
  `python test_p5_min_heap.py`. The tests check the heap property after **every** operation,
  which catches the larger-child bug described above.
- Anything wrong in **Q5** — `practice/p6_triage_queue.py` is that question, built for real.
- And remember what this topic is: the costs and the property are slide-derived, the rest
  is your TA's.
  If your revision time is short, [Topic 4](../4-sorting/review.md) has the better claim on
  it.
