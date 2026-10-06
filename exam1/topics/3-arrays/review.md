# Topic 3 — Arrays, Python lists, and search

**Source:** Array Data Structures (37 slides), plus the search slides of Algorithm
Efficiency (Deck 3 s28–s32). **Lecture weight:** heavy.

---

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
- **Break either condition and the arithmetic stops working.** Gaps, or slots of different
  sizes, and there is no formula — you would have to walk.
- **Size versus capacity.** **Size** is how many elements are actually stored; **capacity**
  is how many slots have been reserved. `len(L)` reports the **size**. Capacity is
  invisible from Python, which is why the resize is invisible too.
- **Static arrays** have a fixed capacity. Growing one means allocating a new, larger block
  and copying everything over by hand — *"this is the main motivation for dynamic arrays"*
  (Deck 4 s17).
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
- **Linear search is O(n); binary search is O(log n)** — but binary search is only correct
  on a **sorted** list, and on unsorted input it returns a wrong answer rather than an error.

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
| `lst.pop()` | O(1) | removes the last item, nothing shifts |
| `lst.insert(0, x)` | O(n) | every element shifts right to make room |
| `lst.pop(0)` | O(n) | every remaining element shifts left |
| `lst.insert(i, x)` / `lst.pop(i)` | O(n) | shifting again, even in the middle |
| build a list of n items | O(n) | n appends |
| grow a **static** array by one slot | O(n) | allocate, copy all n items, discard the old block |

**The distinction the deck keeps coming back to.** `lst.pop()` is **O(1)**; `lst.pop(0)` is **O(n)**.
`lst.append(x)` is **amortized O(1)**; `lst.insert(0, x)` is **O(n)**. One character of
difference and a whole factor of n. This pair shows up on four separate slides
(Deck 4 s32–s36).

## Static versus dynamic

| | Static array | Dynamic array (a Python list) |
|---|---|---|
| Read / write by index | O(1) | O(1) |
| Insert / delete at the front | O(n) | O(n) |
| Append at the end | O(n) | **amortized O(1)** |
| Grow past the current size | you cannot — allocate a new array and copy by hand | resize-and-copy, handled for you |

Both are O(1) to index and O(n) at the front, because both are contiguous equal-size
slots — the address arithmetic and the shifting are identical either way. The **only**
difference is who handles growing, and that one difference is the whole amortized
argument. (Deck 4 s18, s23–s24.)

---

## Why append is amortized O(1)

Capacity doubles: 1, 2, 4, 8, 16, … So the items copied across all the resizes total
1 + 2 + 4 + … + 2ᵏ, which is less than 2ᵏ⁺¹ and so **at most 2n**. n appends therefore cost
O(n) **in total**, which is O(1) per append on average. (Deck 4 s25.)

Now the contrast that makes it land. Suppose the array grew by **one slot** instead of
doubling. Then *every* append finds the array full and copies, so the total is
0 + 1 + 2 + … + (n−1) = **n(n−1)/2** copies — **O(n²)** to build the list. Doubling makes
each resize buy **twice as many** cheap appends as the last one, so the expensive appends
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

This is the version given in full on Deck 3 s30. Two details decide whether it works:

1. the loop condition is `while low <= high`, **not** `low < high` — with `<` the
   one-element range never gets checked, so some hits are reported as misses;
2. `mid` is `(low + high) // 2`, with **integer** division.

Get either wrong and the function still returns answers, just wrong ones on some inputs.
That is why you test misses as well as hits.

And the precondition is not optional: **the list must be sorted**. On unsorted input binary
search does not error, it quietly returns the wrong answer, because every halving decision
assumes order.

---

## How the slides put it

| | |
|---|---|
| "A sequence interface describes what we want to do. A data structure describes how we implement those operations." | Deck 4 s8 |
| "Different implementations can support the same interface with very different costs." | Deck 4 s8 |
| "Spread the total cost of a sequence of operations across that sequence." | Deck 4 s25 |
| "Amortized does not mean every single append is cheap." | Deck 4 s26 |
| "Each resize buys many cheap appends." | Deck 4 s24 |
| "Despite the name, a Python list is implemented like a dynamic array, not a linked list." | Deck 4 s30 |

---

## Where people go wrong

- Saying append is O(1) full stop. It is O(1) **amortized**; the word is doing work and the deck
  quizzes it directly.
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

- [ ] Contiguous equal-size slots; the address formula — Deck 4 s7–s11
- [ ] Size versus capacity — Deck 4 s20
- [ ] Static versus dynamic arrays; the resize-and-copy — Deck 4 s16–s24
- [ ] Amortized O(1) append, and its caveat — Deck 4 s25–s26
- [ ] The cost of each list operation — Deck 4 s32, s35–s36
- [ ] References in the slots, and why mixed types are legal — Deck 4 s30
- [ ] Interface versus implementation — Deck 4 s8
- [ ] Linear O(n) versus binary O(log n) search, and binary search's precondition — Deck 3 s28–s32

---

## Next

- Work [mock.md](mock.md) with this page closed, then check yourself against
  [solutions.md](solutions.md).
- Write the code: `practice/p2_search.py`, checked by `python test_p2_search.py`. Both
  searches, plus counting versions.
- Then [Topic 4](../4-sorting/review.md), which is this cost vocabulary applied to five
  algorithms over the same list.
