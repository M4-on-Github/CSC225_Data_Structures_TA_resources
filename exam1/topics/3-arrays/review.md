# Topic 3 — Arrays, lists, and search

An array stores equal-size slots side by side. Index `i` is found from the first address
plus `i × slot size`, so access is O(1). Python lists store **references** in those
slots; they can therefore hold objects of different types.

**Size** is the number of stored items. **Capacity** is the number of reserved slots. A
dynamic array reserves extra capacity and grows when full; a fixed array requires you to
allocate and copy a larger block yourself.

## Costs to explain

| Operation | Worst-case cost | Reason |
|---|---|---|
| `len(lst)`, `lst[i]`, `lst[i] = x` | O(1) | Stored size or direct indexing |
| One scan or `x in lst` | O(n) | May inspect every item |
| `lst.append(x)` | O(n) for one append | A full array must copy its items |
| `lst.insert(0, x)` or `lst.pop(0)` | O(n) | Remaining items shift |

A sequence of `n` appends from an empty array takes O(n) total with geometric capacity
growth, or **amortized O(1)** per append. A single append can still be O(n). In a
doubling model, the copies across resizes total `1 + 2 + 4 + ... < 2n`. If capacity grew
one slot at a time, copies would total `0 + 1 + ... + (n−1) = O(n²)`.

## Check yourself

- Why is indexing cheap but inserting at the front expensive?
- What are the size and capacity of a list with 3 items and 8 reserved slots?
- Why can one append cost O(n) while many appends cost O(n) total?

Try the [mock](mock.md) and [solutions](solutions.md). Then code [linear search
practice](../../practice/p2_search.py).
