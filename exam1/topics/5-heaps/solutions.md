# Topic 5 — solutions: heaps

Try the [questions](mock.md) before checking these answers.

---

## Part 1 — Drills

**5.1** For **every** node, the node's value is **less than or equal to both of its
children**. This also orders ancestors before descendants, but says **nothing** about
the order between separate branches. A sorted structure pins down the order of
every pair; a heap does not. That is exactly why a heap is cheap to
maintain and why index `k - 1` need not hold the k-th smallest value.

**5.2** Because the property is **local**. `[1, 3, 2, 9, 7, 8, 5]` is a perfectly valid
min-heap — every parent is ≤ its children — and it is not in sorted order.
Index 0 is the only position you can read off directly.

**5.3** `parent_index(i)` = **`(i - 1) // 2`** · `left_index(i)` = **`2i + 1`** ·
`right_index(i)` = **`2i + 2`**. For index 4: parent **1**, left child **9**, right child
**10**. Ten items occupy indices 0–9, so the **right child does not exist** — index 4 has
one child. Check child indices against `size` before using them, and never ask for the
root's parent. Missing those checks is a common bug.

**5.4** The last item sits at index 9, so the **last parent** is `parent_index(9)` = **4**.
Everything after it — indices **5, 6, 7, 8, 9** — is a leaf. Roughly half of any heap is
leaves, which is the whole reason `build_heap` is cheap.

**5.5** Not a bug. **Every ascending list is already a valid min-heap** —
`values[i] <= values[2*i+1]` and `values[i] <= values[2*i+2]` whenever those children
exist. So ascending ⇒ min-heap, but **min-heap ⇏ ascending**. The implication runs one
way only, and the mock test asks it in the direction that is false.

**5.6** (i) **O(1)** — it is index 0 · (ii) **O(log n)** · (iii) **O(log n)** · (iv)
**O(n)** — an arbitrary search may scan the whole list · (v) **O(n)** · (vi)
**O(n log n)** — one build, then n removals of O(log n) each.

**5.7** The **height** of the heap bounds the work: n removals, each sifting down at most
the height of a complete tree, give an **O(n log n)** worst-case bound. Actual work can
vary; all-equal values take O(n) in this implementation because sifts stop immediately.
Quick sort has an **O(n²)** worst case with consistently bad pivots,
which for the last-element pivot means already-sorted input with distinct values. So when you cannot afford a
quadratic worst case — and especially when you also cannot afford merge sort's second list, since
`heap_sort_in_place` needs none — heap sort is the safe pick.

**5.8** In this in-place algorithm, the sorted values accumulate inside the same list,
at **the end**. The value that belongs at the end is the
**largest**, and the only value a heap hands you cheaply is the one at the root — so the
root has to be the largest. Swap it to the end, shrink the heap by one, sift down, repeat. A
min-heap would build the list backwards.

---

## Part 2 — Exam-style questions

### Q1 — Min-heaps
**(a)** **Every node is less than or equal to both of its children.** Nothing is promised
about left versus right, and nothing is promised between cousins — the property is
**local**. It follows that the **minimum is at the root**, which is what makes `peek` O(1).


**(b)** **Complete** = every level is full except possibly the last, and the last fills
**left to right** with no gaps. No gaps means the nodes map onto list indices `0, 1, 2, …`
with nothing skipped, so a parent and its children can be found by **arithmetic** instead of
by following stored references: `left = 2i + 1`, `right = 2i + 2`, `parent = (i − 1) // 2`.

**(c)** The heap keeps it **at the root — index 0**, so finding it is **O(1)**: you read one
slot, you do not search. In an unsorted list the minimum can sit anywhere, so you must look
at all n slots — **O(n)**. That is the trade the heap makes: it pays O(log n) on every
insert and every removal to keep index 0 true, and it buys **only** that. Asking a heap
whether 42 is somewhere inside it is still an O(n) scan.


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

These are worst-case bounds, treating list appends as amortized O(1).

The last one needs care: separate branches are not ordered against each other,
so finding an arbitrary value can require **O(n)** checks despite O(1) `peek`.

**(b)** From the tree's **height**. A heap is a **complete** binary tree, so its height is
⌊log₂ n⌋ — doubling the number of items adds **one** level. `insert` appends at the end and
sifts the new element **up**, swapping it with its parent at most once per level, so the
work is proportional to the height.

**(c)** `build_heap` **sifts down** from the **last parent** backwards to index 0, instead
of sifting n new elements up from the bottom. The difference is where the nodes are:
**roughly half** the nodes are leaves and sift down zero levels, roughly a quarter can
sift down one level, and only the root can travel the full height. That sum comes to **O(n)**. Sifting *up*
has it backwards — it makes the many nodes at the bottom do the long walk.


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

Final tree (`value(index)`):

```text
        1(0)
       /    \
    3(1)   2(2)
    /  \    /
 5(3) 9(4) 8(5)
```

The inserts of **1** and **2** are worth tracing closely. Inserting `1` appends it at index 3, whose parent
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
order is **2, 1, 0** — backwards to the root:

| Sifted index | List afterward |
|---|---|
| 2 | `[9, 7, 2, 3, 1, 8, 5]` |
| 1 | `[9, 1, 2, 3, 7, 8, 5]` |
| 0 | **`[1, 3, 2, 9, 7, 8, 5]`** |

**No, it is not sorted.** The heap property compares each node
against **its own children**, so `9` sits happily at index 3 in front of `7`, `8` and `5` —
none of them is its child.


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
parent. The `break` in the `else` stops the moment the element is greater than or equal to
its parent. Without that stop, and with `i` unchanged, the loop would repeat forever.
The swap must stay inside the comparison so that it only happens when the child is smaller.

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
rather than truncating. `-1` is not the root's parent — in Python it refers to the last
item — which is precisely why `_sift_up` is guarded by `while i > 0` and never asks for the
root's parent.


### Q5 — Applying a heap
**(a)**

| Design | Add a patient | Take the next |
|---|---|---|
| A plain list, scanned when one is needed | **O(1)** *(append)* | **O(n)** *(scan every patient, then remove)* |
| A list kept sorted by urgency at all times | **O(n)** *(find the slot, shift everything after it)* | **O(1)** *(keep the most urgent at the end, then pop)* |
| A min-heap keyed on urgency | **O(log n)** | **O(log n)** |

**Ship the heap.** It is the only one of the three where **both** operations are
sub-linear, and the question says both happen constantly. The other two are each excellent
at one operation and linear at the other, so whichever you choose, the ER spends its day in
the O(n) half. A heap is slightly worse than either at that one operation and far better
than either overall — that trade is the answer.

**(b)** **No.** The heap property is **local** — each node is only ordered against its own
children — so the list is in heap order, not sorted order. Only index 0 is guaranteed to be
anything in particular. Reading it top to bottom and calling it a treatment order would put
patients on that screen in the wrong order.

To get the real order it must **copy the heap and drain the copy** with repeated
`remove_min()` — n removals at O(log n) each, so **O(n log n)**. That is heap sort, and it
is where heap sort comes from. The copy matters: draining the live heap empties the waiting
list.

**(c)** A sorted list gives the **whole urgency order** directly, with no draining.
It also gives the k-th most urgent patient by index. A heap guarantees only its
minimum at the root.


### Q6 — From heap steps to Python

One translation, using the index functions from `p5_min_heap.py`:

```python
    def remove_min(self):
        if self.is_empty():
            return None
        smallest = self._items[0]
        last = self._items.pop()
        if not self.is_empty():
            self._items[0] = last
            self._sift_down(0)
        return smallest

    def _sift_down(self, i):
        n = len(self._items)
        while True:
            smallest = i
            left = left_index(i)
            right = right_index(i)
            if left < n and self._items[left] < self._items[smallest]:
                smallest = left
            if right < n and self._items[right] < self._items[smallest]:
                smallest = right
            if smallest == i:
                break
            self._items[i], self._items[smallest] = self._items[smallest], self._items[i]
            i = smallest


def build_heap(values):
    heap = MinHeap()
    heap._items = list(values)
    for i in range(parent_index(len(heap._items) - 1), -1, -1):
        heap._sift_down(i)
    return heap
```

The incorrect left swap makes `[4, 9, 2, 7, 6]`: root `4` is larger than
its right child `2`. The correct first swap gives `[2, 4, 9, 7, 6]`.
Comparing only children that exist also handles a lone left child.
