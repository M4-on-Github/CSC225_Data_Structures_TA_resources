# Topic 3 — Arrays, Python lists, and search

## What this topic is

This is where [Topic 2](../2-big-o/review.md)'s vocabulary first earns its keep, by
answering a question students rarely think to ask: **why is `L[5]` fast?**

The answer — contiguous equal-size slots and one line of address arithmetic — is also the
answer to why `L.insert(0, x)` is slow. One layout fact explains the entire cost table.
The topic ends on the amortized-append argument, which is the most subtle piece of
reasoning in the first half of the course, and on binary search, which is the cheapest
place to watch an O(log n) halving actually happen.

---

## The ideas, in the order they depend on each other

- **An array is contiguous slots, all the same size.** That single layout fact gives you
  `address of A[i] = address of A[0] + i × slot size`: one multiply, one add, **O(1)**, no
  matter how big `i` is.
- **Break either condition and this arithmetic stops working.** Gaps or slots of different
  sizes require more information about the layout; the simple formula no longer applies.
- **Size versus capacity.** **Size** is how many elements are actually stored; **capacity**
  is how many slots have been reserved. `len(L)` reports the **size**. Capacity is
  not exposed by the list interface, which handles resizing for you.
- **Static arrays** have a fixed capacity. Growing one means allocating a new, larger block
  and copying everything over by hand — *"this is the main motivation for dynamic arrays"*
- **Dynamic arrays** — which is what a CPython `list` is — do that for you: allocate a
  **multiplicatively** larger block, copy all n existing elements, release the old block,
  store the new element.
- **That one copying append is O(n).** But the resizes get rarer as the array grows, so the
  cost averaged over a long run of appends is constant: **O(1) amortized**.
- **Amortized is not "always cheap", and it is not average case.** Amortized spreads the
  cost of a **sequence of operations** across that sequence. Average case averages over
  random **inputs**. The slides: *"amortized does not mean every single append is cheap."*
- **Shifting is what makes the front expensive.** `insert(0, x)` moves every element up a
  slot; `pop(0)` moves every element down. Both **O(n)**. The end of a list is cheap, the
  front of a list is not.
- **A Python list stores references, not objects.** That is why `[10, "hi", 3.14]` is legal:
  every slot holds an address, and every address is the same size.
- **Interface versus implementation.** A *sequence* interface says **what** you can do:
  `len`, iterate, get at `i`, set at `i`, insert, delete. The implementation chooses
  **how** — and therefore chooses what each operation **costs**. Same interface, different
  implementation, very different costs. That comparison is the one every later topic makes.
- **Linear search is O(n); binary search is O(log n)** — but binary search requires a
  **sorted** list, and on unsorted input it may return a wrong answer without an error.

---

## The cost table to know cold

| Operation | Cost | Why |
|---|---|---|
| `len(lst)` | O(1) | the size is stored, not counted |
| `lst[i]` | O(1) | address arithmetic: base + i × slot size |
| `lst[i] = x` | O(1) | same arithmetic, then one write |
| `for x in lst` | O(n) | visits every element |
| `x in lst` | O(n) | linear search — it does not know the list is sorted |
| `lst.append(x)` | **amortized O(1)** | usually there is spare capacity; sometimes it resizes |
| `lst.pop()` | amortized O(1) | removes the last item; nothing shifts, but storage may occasionally shrink |
| `lst.insert(0, x)` | O(n) | every element shifts right to make room |
| `lst.pop(0)` | O(n) | every remaining element shifts left |
| `lst.insert(i, x)` / `lst.pop(i)` | O(n) | shifting again, even in the middle |
| build a list of n items | O(n) | n appends |
| grow a **static** array by one slot | O(n) | allocate, copy all n items, discard the old block |

**The distinction to have ready.** `lst.pop()` is **amortized O(1)**;
`lst.pop(0)` is **O(n)**. The usual O(1) label for an end-pop ignores occasional storage shrinking.
`lst.append(x)` is **amortized O(1)**; `lst.insert(0, x)` is **O(n)**. One character of
difference and a whole factor of n. This pair shows up on four separate slides

## Static versus dynamic

| | Static array | Dynamic array (a Python list) |
|---|---|---|
| Read / write by index | O(1) | O(1) |
| Insert / delete at the front | O(n) | O(n) |
| Append when full | O(n) to allocate a larger array and copy | O(n) for this append; **amortized O(1)** over a sequence |
| Grow past the current capacity | you cannot — allocate a new array and copy by hand | resize-and-copy, handled for you |

Both are O(1) to index and O(n) at the front, because both are contiguous equal-size
slots — the address arithmetic and the shifting are identical either way. When there is
spare capacity, storing an item at the end is O(1) in either structure. Dynamic arrays
handle growth automatically and reserve extra space; that growth policy is what supports
the amortized argument.

---

## Why append is amortized O(1)

In the doubling model, capacity grows as 1, 2, 4, 8, 16, … So the items copied across all the resizes total
1 + 2 + 4 + … + 2ᵏ, which is less than 2ᵏ⁺¹ and so **at most 2n**. n appends therefore cost
O(n) **in total**, starting from an empty array, which is O(1) per append on average.
The argument works for other fixed growth factors greater than 1 too; Python lists need
not double their capacity.

Now the contrast that makes it land. Suppose the array grew by **one slot** instead of
doubling. Then *every* append finds the array full and copies, so the total is
0 + 1 + 2 + … + (n−1) = **n(n−1)/2** copies — **O(n²)** to build the list. Doubling makes
each resize leave roughly **twice as much** spare capacity as the last one, so the expensive appends
get rarer exactly as fast as they get dearer.

That `n(n−1)/2` is the same sum as selection sort's comparison count in
[Topic 2](../2-big-o/review.md). It is worth noticing that the two most different-looking
derivations in the course are the same piece of arithmetic.

---

## The two searches

```python
def binary_search(values, element):
    low = 0
    high = len(values) - 1
    while low <= high:
        mid = (low + high) // 2
        if values[mid] == element:
            return mid
        elif values[mid] < element:
            low = mid + 1          # discard the whole left half
        else:
            high = mid - 1         # discard the whole right half
    return -1
```

Two details decide whether this works:

1. the loop condition is `while low <= high`, **not** `low < high` — with `<` the
   one-element range never gets checked, so some hits are reported as misses;
2. `mid` is `(low + high) // 2`, with **integer** division.

Using `<` can return a wrong answer; using `/` instead of `//` produces a float index and
raises `TypeError` when the loop tries to index the list. Test misses as well as hits.

And the precondition is not optional: **the list must be sorted**. On unsorted input binary
search may quietly return the wrong answer, because every halving decision
assumes order.

---

## Say it this way

Six sentences worth having word for word:

- A sequence interface describes what we want to do. A data structure describes how we
  implement those operations.
- Different implementations can support the same interface with very different costs.
- Amortized spreads the total cost of a sequence of operations across that sequence.
- Amortized does not mean every single append is cheap.
- Each resize buys many cheap appends.
- Despite the name, a Python list is implemented like a dynamic array, not a linked list.

---

## Where people go wrong

- Saying append is O(1) full stop. It is O(1) **amortized**, and the word is doing work.
- Confusing size with capacity, and then being unable to explain when a resize happens.
- Thinking `insert(0, x)` is cheap because the list "knows where the front is". Knowing
  where it is costs nothing; **making room** costs n shifts.
- Giving `x in L` as O(1). It is a linear scan: **O(n)**.
- Describing the resize as "adding one slot". It allocates a **multiplicatively** larger
  block — that is precisely why the amortized argument works.
- Computing an address as `base + i` and forgetting the slot size.
- Saying a Python list "contains" its objects. It contains **references** to them, and
  that distinction is the whole idea.
- Using binary search on an unsorted list in a code-reading question and not noticing.

---

## Checklist

- [ ] Contiguous equal-size slots; the address formula
- [ ] Size versus capacity
- [ ] Static versus dynamic arrays; the resize-and-copy
- [ ] Amortized O(1) append, and its caveat
- [ ] The cost of each list operation
- [ ] References in the slots, and why mixed types are legal
- [ ] Interface versus implementation
- [ ] Linear O(n) versus binary O(log n) search, and binary search's precondition

---

## Next

- Work [mock.md](mock.md) with this page closed, then check yourself against
  [solutions.md](solutions.md).
- Write the code: `practice/p2_search.py`, checked by `python -m unittest discover -s . -p "test_p2_search.py" -v`. Both
  searches, plus counting versions.
- Then [Topic 4](../4-sorting/review.md), which is this cost vocabulary applied to five
  algorithms over the same list.
