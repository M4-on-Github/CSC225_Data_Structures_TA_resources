# Topic 3 — solutions: arrays, Python lists, and search

Try the [questions](mock.md) before checking these answers.

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
over a long run of appends is constant — **O(1) amortized**. One particular append can
still be O(n).

**3.5** (i) **O(1)** · (ii) **O(1) amortized** · (iii) **O(n)** — everything shifts up ·
(iv) **O(1) amortized** · (v) **O(n)** — everything shifts down · (vi) **O(n)** — a linear scan.

The usual O(1) label for an end-pop ignores occasional storage shrinking.

**3.6** The **interface** is what the structure promises you can do (`append`, `pop`,
`len`). The **implementation** is how it keeps that promise (a dynamic array that quietly
resizes). Same interface, different implementation, very different costs — which is
exactly the comparison every later topic makes.

---

## Part 2 — Exam-style questions

### Q1 — Amortized append
**(a)** That the **total** cost of n appends, starting from an empty array, is O(n), so the
**average cost per append** is constant.

**(b)** The append that finds the array **full**. It allocates a larger array, **copies all
n existing elements**, then adds the new one — that append is **O(n)**.


### Q2 — Arrays, addresses and references
**(a)** The interface promises the **operations**: `len()`, iterate, get at `i`, set at
`i`, insert, delete. The implementation chooses **how** — contiguous memory, spare
capacity, a growth factor — and therefore chooses **what each operation costs**.


**(b)** **2024.** `address of A[6] = address of A[0] + 6 × 4 = 2000 + 24`. It is one
multiply and one add whatever the length is, so it is **O(1)** — the index can change, the
**number of steps** does not.

**(c)** **References** — a stored address pointing at an object somewhere else in memory.
Every slot is the same size because every slot holds an address, not the object, and that
is exactly why the types may differ.


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
rarer exactly as fast as they get dearer.

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
