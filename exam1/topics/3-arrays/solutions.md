# Topic 3 — solutions: arrays, Python lists, and search

Answers to [mock.md](mock.md), in order, each followed by what a complete answer needs.
**Attempt the paper first.** Q4's table and its code were produced by running the code, not from memory.

---

## Part 1 — Drills

**3.1** The slots must be **contiguous** (no gaps) and **all the same size**. Then
`address of A[i] = address of A[0] + i × slot size`. Break either one and the arithmetic
no longer applies without more information about the layout.

**3.2** **Size** is how many elements are actually stored; **capacity** is how many slots
have been reserved. `len(L)` reports the **size**. Capacity is not exposed by the list
interface, which handles resizing for you.

**3.3** Allocate a **new, larger** block (the growth is multiplicative, not +1), **copy all
n existing elements** across, release the old block, then store the new element. That one
append is **O(n)**.

**3.4** The expensive resizes are rare and get rarer as the array grows, so the cost spread
over a long run of appends is constant — **O(1) amortized**. The trap:
*"amortized does not mean every single append is cheap."* One particular append can still
be O(n).

**3.5** (i) **O(1)** · (ii) **O(1) amortized** · (iii) **O(n)** — everything shifts up ·
(iv) **O(1) amortized** · (v) **O(n)** — everything shifts down · (vi) **O(n)** — a linear scan.

The usual O(1) label for an end-pop ignores occasional storage shrinking.

**3.6** The **interface** is what the structure promises you can do (`append`, `pop`,
`len`). The **implementation** is how it keeps that promise (a dynamic array that quietly
resizes). Same interface, different implementation, very different costs — which is
exactly the comparison every later topic makes.

**3.7** Linear: **1,000,000** — O(n). Binary: about **20**, since 2²⁰ ≈ 1,000,000 —
O(log n).

**3.8** It must be **sorted**. On unsorted input binary search may quietly return the
wrong answer, because every halving decision assumes order.

---

## Part 2 — Exam-style questions

### Q1 — Amortized append
**(a)** That the **total** cost of n appends, starting from an empty array, is O(n), so the
**average cost per append** is constant.

**(b)** The append that finds the array **full**. It allocates a larger array, **copies all
n existing elements**, then adds the new one — that append is **O(n)**.

**(c)** Amortized spreads the cost of a **sequence of operations** across that sequence.
Average case averages over **random inputs**. The slides: *"amortized does not mean every
single append is cheap."*

**What a complete answer needs**

- (a) "Average over many operations", or "total O(n) for n appends". "Every append is
  O(1)" is the wrong answer — that is the claim amortized analysis exists to avoid making.
- (b) **Copying** and **O(n)**. "Resize" without the copy names the event but not the cost.
- (c) Sequence-of-operations versus random-inputs. This is the hardest single idea on this
  paper — missing it is normal.

### Q2 — Arrays, addresses and references
**(a)** The interface promises the **operations**: `len()`, iterate, get at `i`, set at
`i`, insert, delete. The implementation chooses **how** — contiguous memory, spare
capacity, a growth factor — and therefore chooses **what each operation costs**. The slides:
*"different implementations can support the same interface with very different costs."*

**(b)** **2024.** `address of A[6] = address of A[0] + 6 × 4 = 2000 + 24`. It is one
multiply and one add whatever the length is, so it is **O(1)** — the index can change, the
**number of steps** does not.

**(c)** **References** — a stored address pointing at an object somewhere else in memory.
Every slot is the same size because every slot holds an address, not the object, and that
is exactly why the types may differ.

**What a complete answer needs**

- (a) One operation on the interface side **and** one implementation choice.
  "Interface = what, implementation = how" with no example is the definition without the
  understanding.
- (b) **2024**, and a reason naming the fixed number of steps. 2000 + 6 = 2006 forgets the
  slot size.
- (c) **References**, **addresses** or **pointers**. "Objects" is wrong — the list does not
  contain the objects, and that distinction is the whole point of the question.

### Q3 — The cost table
| Structure | Operation | Big-O |
|---|---|---|
| Python list | `lst[i]` | **O(1)** — index arithmetic |
| Python list | `len(lst)` | **O(1)** — the size is stored, not counted |
| Python list | `lst.append(x)` | **amortized O(1)** — usually there is spare capacity |
| Python list | `lst.insert(0, x)` | **O(n)** — shift everything right |
| Python list | `lst.pop()` | **amortized O(1)** — no shifting; storage may occasionally shrink |
| Python list | `lst.pop(0)` | **O(n)** — shift everything left |
| Python list | `x in lst` | **O(n)** — linear search |
| Static array | grow it by one slot | **O(n)** — allocate, copy all n, discard the old |

The pattern worth seeing: a Python list is **fast at the end and slow at the front**.
`pop()` and `pop(0)` differ by one character and by a whole factor of n.

**What a complete answer needs**

- All eight cells. Include **amortized** for `append`, as in Q1.
- `lst.pop()` and `lst.pop(0)` are the two that separate careful readers. Writing both
  O(n), or both O(1), is the common answer and misses that one end of a list is cheap and
  the other is not.

### Q4 — Watching a dynamic array grow
**(a)**

| Append | Capacity after | Elements copied |
|---|---|---|
| 1st | 1 | 0 |
| 2nd | 2 | 1 |
| 3rd | 4 | 2 |
| 4th | 4 | 0 |
| 5th | 8 | 4 |
| 6th | 8 | 0 |
| 7th | 8 | 0 |
| 8th | 8 | 0 |
| 9th | 16 | 8 |

Only four of the nine appends copy anything — the 2nd, 3rd, 5th and 9th, the ones that
found the array exactly full. The other five drop the value into a spare slot and are
genuinely **O(1)**.

**(b)** **15** copies in total: 1 + 2 + 4 + 8. With n = 9, **2n = 18**, and 15 < 18. That
is the bound given: the copies form the doubling sum 1 + 2 + … + 2ᵏ, which is less than 2ᵏ⁺¹ and
so at most **2n**. So nine appends cost O(n) in total, which is what **amortized O(1) per
append** means.

**(c)** Because adding one slot means **every append after the first** finds the array
full, so it copies the existing items:
0 + 1 + 2 + … + (n−1) = n(n−1)/2 copies, **O(n²)** to build the list. Doubling makes each
resize leave roughly **twice as much** spare capacity as the last one, so the expensive appends get
rarer exactly as fast as they get dearer. The slides: *"each resize buys many cheap
appends."*

**(d)**

```python
class DynamicArray:

    def __init__(self):
        self._slots = [None]
        self._size = 0

    def size(self):
        return self._size

    def capacity(self):
        return len(self._slots)

    def get(self, i):
        if i < 0 or i >= self._size:
            return None
        return self._slots[i]

    def append(self, element):
        if self._size == len(self._slots):
            self._resize()
        self._slots[self._size] = element
        self._size = self._size + 1

    def _resize(self):
        bigger = [None] * (len(self._slots) * 2)
        for i in range(self._size):
            bigger[i] = self._slots[i]
        self._slots = bigger
```

Three things this code makes concrete, each of which turns up elsewhere on the paper:

- **`size` and `capacity` are genuinely different numbers.** `self._size` is a counter you
  maintain; `len(self._slots)` is the capacity. Nothing in the class can read the size off
  the storage, because the spare slots hold `None` and `None` is a legal element.
- **The copy loop is the O(n).** `_resize` runs `self._size` assignments. It is the only
  loop in the class, and every other method is a fixed number of steps — which is exactly
  why `append` is O(1) **except** when `_resize` fires.
- **The resize test is `==`, before storing.** Checking after storing would write past the
  end of the list and raise `IndexError`.

The condition `if self._size == len(self._slots)` is the line the whole topic is about: it
fires on appends 2, 3, 5 and 9 in this nine-append example, as shown in the table in
part (a).

**What a complete answer needs**

- (a) Both columns. The 1st append copying **0** is the one to watch — capacity is already
  1, so there is room. Writing 1 there shifts the whole table down a row.
- (b) **15**, compared against 18 or against 2n. The number alone misses the point, which
  is that the total copying is linear in n.
- (c) That +1 growth makes **every append after the first** copy. Naming n(n−1)/2 or O(n²) is better
  still — it is the same sum as selection sort's comparisons in
  [Topic 2](../2-big-o/mock.md) Q4.
- (d) Five separate things:
  - `size` returns the counter and `capacity` returns `len(self._slots)`. Returning
    `len(self._slots)` from `size` breaks the first assertion.
  - `get` guards **both** ends and returns `None` rather than raising. Guarding only the
    upper end means `get(-1)` reads the last storage slot. A spare slot containing `None`
    can hide the bug; the assertion on the full array `b` catches it.
  - `append` resizes **only when full**, then stores at index `self._size`, then
    increments. Storing before resizing, or incrementing before storing, both break it.
  - `_resize` builds a new list of **double** the length and copies the stored elements
    across. Growing by a fixed amount works but defeats the purpose; forgetting to
    reassign `self._slots` throws the copy away.
  - No banned list method anywhere — no `append`, `insert`, `pop` or `remove` on
    `self._slots`. Delegating storage growth to `self._slots.append(element)` bypasses
    the task: the question is how a dynamic array is built, and that method already does
    the resizing for you.

---

## If you got it wrong

- Anything wrong in **Q1 or Q4(b)(c)**
  subtlest reasoning in the first half of the course, and the word is examinable on its own.
- Anything wrong in **Q3**
  answer key. Learn that page as facts plus one reason each.
- Anything wrong in **Q2(b)**
- Then write it: `practice/p2_search.py`, checked by `python -m unittest discover -s . -p "test_p2_search.py" -v`.
