# Topic 3 — mock test: arrays, Python lists, and search

Try the drills and questions before opening [solutions](solutions.md). Work at your own pace.

**Throughout:** give each Big-O cost with one sentence of reasoning.

---

## Part 1 — Drills

**3.1** What two things must be true of an array's memory for O(1) indexing to work?

**3.2** `size` versus `capacity` — define both, and say which one `len(L)` gives you.

**3.3** A dynamic array is full and one more append arrives. Walk through what happens.

**3.4** So why is append still called O(1), and what is the trap in that word?

**3.5** Costs: (i) `L[5]` · (ii) `L.append(x)` · (iii) `L.insert(0, x)`
· (iv) `L.pop()` · (v) `L.pop(0)` · (vi) `x in L`.

**3.6** "Interface versus implementation" — what is the distinction, and why does the
course keep coming back to it?

**3.7** Linear search versus binary search on 1,000,000 sorted items: roughly how many
items does each inspect in the worst case? Count one inspection per loop iteration.

**3.8** What must be true of the list before `binary_search` is allowed to run, and what
happens if it isn't?

---

## Part 2 — Exam-style questions

### Q1 — Amortized append
`lst.append(x)` on a Python list is described as **amortized O(1)**.

**(a)** What does "amortized O(1)" promise?

**(b)** Describe one append that is **not** O(1), and say what it costs.

**(c)** Amortized is not the same as average case. Give the difference in one sentence.

### Q2 — Arrays, addresses and references
**(a)** A *sequence* is an **interface**; a Python `list` is an **implementation** of
it. Give one thing the interface promises and one thing the implementation chooses.

**(b)** An array of ints starts at address 2000 and each int takes 4 bytes. What is
the address of `A[6]`, and why does finding it not get slower as the array gets longer?

**(c)** A Python list can hold `[10, "hi", 3.14]` all at once. What does it actually
store in its slots?

### Q3 — The cost table
Fill in the cost of each operation. `lst` is an ordinary Python list holding n items.


| Structure | Operation | Big-O |
|---|---|---|
| Python list | `lst[i]` | |
| Python list | `len(lst)` | |
| Python list | `lst.append(x)` | |
| Python list | `lst.insert(0, x)` | |
| Python list | `lst.pop()` | |
| Python list | `lst.pop(0)` | |
| Python list | `x in lst` | |
| Static array | grow it by one slot | |

### Q4 — Watching a dynamic array grow
A dynamic array starts with **capacity 1** and **doubles** whenever an append finds it
full. Nine items are appended, one at a time.

**(a)** Fill in the table: the capacity after each append, and how many existing
elements **that** append had to copy.

| Append | Capacity after | Elements copied |
|---|---|---|
| 1st | | |
| 2nd | | |
| 3rd | | |
| 4th | | |
| 5th | | |
| 6th | | |
| 7th | | |
| 8th | | |
| 9th | | |

**(b)** Total elements copied across all nine appends? Compare it with 2n.

**(c)** Why double, rather than add one slot each time?

**(d)** Write a `DynamicArray` class that does this, using a Python list **only as
fixed-size storage** — so you may index and assign into it, and read its length, but you
may **not** call `append`, `insert`, `pop` or any other method that changes its size. No
imports.

```python
class DynamicArray:
    def __init__(self):
        self._slots = [None]       # capacity 1, size 0
        self._size = 0

    def size(self):
        # your code here

    def capacity(self):
        # your code here

    def get(self, i):
        # your code here

    def append(self, element):
        # your code here

    def _resize(self):
        # your code here


# it must satisfy all of these
a = DynamicArray()
assert a.size() == 0 and a.capacity() == 1
for value in range(9):
    a.append(value)
assert a.size() == 9
assert a.capacity() == 16
assert a.get(0) == 0 and a.get(8) == 8
assert a.get(9) is None            # out of range: None, not an exception
assert a.get(-1) is None

b = DynamicArray()
b.append(7)                       # full storage: catches an unguarded negative index
assert b.get(-1) is None
```

`_resize` doubles the capacity: it builds a new list of `None` twice as long, copies every
stored element across, and keeps it. `append` calls `_resize` **only** when the array is
full, then stores the element and increases the size. `get` returns `None` for an index
that is not in `0` to `size − 1`.

---

## Part 3 — Write the code

This topic's practice problem is `practice/p2_search.py`, checked by
`python -m unittest discover -s . -p "test_p2_search.py" -v` from the `practice/` folder: linear and binary search plus
counting versions of both. Q4(d) above is the one place here where you build
the dynamic array itself rather than using one.
