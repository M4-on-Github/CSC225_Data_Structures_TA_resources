# Topic 4 — Sorting: all five algorithms

**Source:** Merge / Bubble / Pivot Sorting (34 frames), plus selection sort from Algorithm
Efficiency (Deck 3 s10–s12). This is the largest topic in this practice package.

---

## What this topic is

Five algorithms that do the same job at wildly different costs, which makes this a natural
place to practise writing sorting methods from scratch. The homework on Deck 7 s33 assigns exactly four of
them — selection, bubble, merge and quick — while **insertion sort is taught in full but
left off that list**, under the heading "Insertion Sort: Why Mention It?". Read that how
you like; the sane response is to be able to write **all five**.

The one hard rule for this topic, from Deck 7 s8: **no `sort()`, no `sorted()`, no extra
packages.** You are being asked to write the sort, not to call one.

---

## The ideas, in the order they depend on each other

- **Selection sort:** find the minimum of the unsorted region, swap it into place. Taught
  back in **Deck 3 (s10–s12)**, not in the sorting deck — the sorting deck only lists it
  again in the summary table. Always **n(n−1)/2** comparisons, so **O(n²) even on
  already-sorted input**.
- **Bubble sort:** repeatedly swap adjacent out-of-order pairs. The `swapped` flag gives an
  early exit, which makes the **best case O(n)**. The inner range is
  `range(n - 1 - pass_num)` because each pass parks one more value at the end.
- **Insertion sort:** take the next element and slide it back into the sorted prefix. Best
  case **O(n)**, and it is genuinely fast on nearly-sorted data.
- **Merge sort:** split to single elements, then merge pairs back. **O(n log n) in all
  three cases** — log n levels, O(n) work per level. It is **stable** because the merge
  compares with `<=`.
- **Quick sort:** pick a pivot, partition, recurse. The lecture version takes **`values[-1]`** and does
  a three-way split into `left` / `middle` / `right`. O(n log n) average, but **O(n²) when
  the pivot keeps landing at an extreme** — which, for a last-element pivot, happens on
  sorted input with distinct values. All-equal input takes only O(n): every item goes into
  `middle` in one pass.
- **In place versus new list:** selection, bubble and insertion sort **in place** and return
  **the same object**. Merge and quick **return a new list** for inputs of length at least
  two; their empty-list and singleton base cases return the original list. The practice
  tests check this convention.
- **Stability** means equal items keep their original relative order. Bubble, insertion and
  merge are stable; selection is not. The three-way quick sort shown here is also stable,
  because it appends to each partition in the original order. Many in-place quick sorts
  are not stable.
- **Recursion lives here**, not as a topic of its own: merge and quick are both "solve two
  smaller versions of the same problem, then combine".

---

## The summary table (compare Deck 7 s24)

Use the costs for the exact implementations below; quick sort's stability and all-equal
best case depend on its three-way split.

| Sort | Best | Average | Worst | In place? | Stable? | The one thing to say about it |
|---|---|---|---|---|---|---|
| Selection | O(n²) | O(n²) | O(n²) | yes | no | always n(n−1)/2 comparisons — sorted input does not help |
| Bubble | **O(n)** | O(n²) | O(n²) | yes | yes | the O(n) best case **is** the `swapped` early exit |
| Insertion | **O(n)** | O(n²) | O(n²) | yes | yes | fast on nearly-sorted data; good on small inputs |
| Merge | O(n log n) | O(n log n) | O(n log n) | no | yes | the only one with no bad case; needs extra space |
| Quick | **O(n)** with all-equal values; O(n log n) with distinct values | O(n log n) | **O(n²)** | no | yes, for this version | the worst case is a pivot that splits badly every time |

Three cells carry most of the content: bubble's **O(n)** best case, selection's
**quadratic** best case, and quick's **O(n²)** worst case.

---

## Which sort, and why

| If the situation is … | Use | Because |
|---|---|---|
| The file is nearly sorted already | Insertion sort | its work is O(n + I), where I is the number of out-of-order pairs; it is O(n) when I is O(n) |
| Ties must keep the order they arrived in | Merge sort | the `<=` in its merge step makes it stable, with an O(n log n) worst-case guarantee |
| You need a guaranteed worst-case bound | Merge or heap sort | both have an O(n log n) worst-case guarantee; quick sort degrades to O(n²) on bad pivots |
| … and memory is tight, so no second list | Heap sort, in place | merge sort needs O(n) extra space; in-place heap sort needs O(1) |

The last row is the bridge to [Topic 5](../5-heaps/review.md): of everything in this
course, in-place heap sort is the only sort that is **both** O(n log n) in the worst case
**and** in place.

---

## The code, as lecture writes it

These are the five functions the solutions file ships and the practice tests check. The
comments flag the details that are easy to get wrong.

```python
def selection_sort(values):
    n = len(values)
    for start in range(n):
        min_index = start
        for j in range(start + 1, n):
            if values[j] < values[min_index]:
                min_index = j
        values[start], values[min_index] = values[min_index], values[start]
    return values          # the SAME list it was given
```

```python
def bubble_sort(values):
    n = len(values)
    for pass_num in range(n - 1):
        swapped = False                      # reset once PER PASS
        for i in range(n - 1 - pass_num):    # the parked tail is skipped
            if values[i] > values[i + 1]:
                temp = values[i]             # the three-line swap
                values[i] = values[i + 1]
                values[i + 1] = temp
                swapped = True
        if not swapped:                      # the whole O(n) best case
            break
    return values
```

```python
def insertion_sort(values):
    for i in range(1, len(values)):          # starts at 1, not 0
        current = values[i]
        j = i - 1
        while j >= 0 and values[j] > current:   # BOTH halves of the condition
            values[j + 1] = values[j]
            j -= 1
        values[j + 1] = current
    return values
```

```python
def merge_sort(values):
    if len(values) <= 1:
        return values

    mid = len(values) // 2
    left = merge_sort(values[:mid])
    right = merge_sort(values[mid:])

    result = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:              # "<=", not "<" — this is stability
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])                  # one side still has items
    result.extend(right[j:])
    return result                            # a NEW list
```

```python
def quick_sort(values):
    if len(values) <= 1:
        return values

    pivot = values[-1]                       # the pivot choice to keep
    left = []
    middle = []
    right = []
    for item in values:
        if item < pivot:
            left.append(item)
        elif item == pivot:
            middle.append(item)              # keep the middle, or lose duplicates
        else:
            right.append(item)
    return quick_sort(left) + middle + quick_sort(right)
```

Four lines to be able to reproduce under pressure: bubble's `swapped = False` **inside** the
outer loop, insertion's `while j >= 0 and …`, merge's `<=`, and quick's three-way split
with `middle` kept.

---

## Where the growth rates come from

**Selection sort, n(n−1)/2.** The first pass compares the candidate against n−1 items, the
next against n−2, down to 1: (n−1) + (n−2) + … + 1 = n(n−1)/2 = n²/2 − n/2, so **O(n²)**.
Nothing about the data appears anywhere in that count — on ten items it is 45 comparisons
whether the list is sorted or reversed. The counting version skips self-swaps, so it
reports 0 swaps against 5. The plain version above performs its assignment every pass.

**Merge sort, n log n.** The `log n` is the **number of levels**: `mid = len(values) // 2`
halves the list, and n can only be halved down to 1 about log₂ n times. The `n` is the
**work on one level**: merging all the pieces takes O(n) work in total. Levels × work
per level = n log n, and nothing about the data changes either factor.

**Quick sort's worst case.** With the pivot at `values[-1]`, feed it `[1, 2, 3, 4, 5]`:
pivot 5, `left = [1, 2, 3, 4]`, `middle = [5]`, `right = []`. One side gets everything and
the other gets nothing, so the recursion shrinks by **one element per level** instead of
halving — n levels, O(n) work each, **O(n²)**. Already-sorted input is the worst case for
*that* pivot choice when the values are distinct, which is the opposite of what people expect.

**Bubble sort's best case.** One pass over a sorted list makes no swap, `swapped` stays
`False`, and the `break` fires: n−1 comparisons, **O(n)**. Take the flag out and the same
algorithm is O(n²) on the same input — which is why an exam answer has to say *which
version* it means.

---

## How the slides put it

| | |
|---|---|
| "How does it work? How fast does it grow as n gets large?" | Deck 7, the two questions asked of every algorithm |
| "Large values gradually bubble to the right." | Deck 7 s4 |
| "After one full pass, the largest unsorted value is in its correct final position." | Deck 7 s6 |
| "Break the list into tiny pieces, then carefully stitch sorted pieces back together." | Deck 7 s11 |
| "The pivot is not necessarily the middle value. It is just the value we choose to split around." | Deck 7 s17 |
| "Quadratic growth is a lot faster-growing than linear or n log n growth." | Deck 7 s24 |

---

## Where people go wrong

- Giving bubble sort's best case as O(n²). With the `swapped` exit it is **O(n)** — and
  without the flag it would be O(n²), so say which version you mean.
- Giving selection sort a best case of O(n). Its best case is still **O(n²)**; the scan happens regardless.
- Writing `merge_sort(nums)` and then printing `nums`. Merge sort returns a **new** list;
  you just threw it away.
- Using `range(n)` for bubble's inner loop, which reads past the end on `values[i + 1]`.
  Using `range(n - 1)` is safe but repeats work over the already-parked tail.
- Putting `swapped = False` **outside** the outer loop. The sort still works, but the early
  exit stops working after the first swap. Already-sorted input still takes O(n), but
  even one out-of-order pair can force O(n²) work — a bug with no wrong output.
- Dropping insertion sort's `j >= 0`. `values[-1]` is legal Python, so the loop corrupts the
  list from the far end before it eventually raises `IndexError`.
- Dropping the `middle` group in quick sort's three-way split, which loses every duplicate
  of the pivot.
- Claiming quick sort's **worst** case is O(n log n). Average, yes. Worst, **O(n²)**.
- Answering "merge sort" to every *choose a sort* question. Insertion sort can do less work
  on nearly-sorted data, and this merge sort needs extra memory; both issues appear on the mock.

---

## Checklist

- [ ] Write all five sorts from memory, in the lecture form — Deck 7 s9, s15, s22, s28; Deck 3 s11
- [ ] The summary table: best / average / worst / in place / stable — Deck 7 s24
- [ ] Which three sort in place, and which two build new lists except in their base cases
- [ ] n(n−1)/2 derived, not quoted — Deck 3 s10–s12
- [ ] Merge sort's levels × work-per-level argument — Deck 7 s11–s16
- [ ] Quick sort's pivot, three-way split, and the input that gives it O(n²) — Deck 7 s17–s23
- [ ] Bubble's `swapped` flag, and what it does and does not buy — Deck 7 s7, s10
- [ ] Stability, and the `<=` in the merge that causes it — Deck 7 s15
- [ ] Trace each sort by hand on a five- or six-item list, writing every pass

---

## Next

- Work [mock.md](mock.md) with this page closed, then check yourself against
  [solutions.md](solutions.md).
- Write the code: `practice/p3_sorts.py` (all five as functions), then
  `practice/p4_sortable_list.py` (the same five as methods on a class), checked by
  `python test_p3_sorts.py` and `python test_p4_sortable_list.py`. Work on one sort at a
  time; use the [study paths](../../study_paths.md) to choose your next task.
- Then [Topic 5](../5-heaps/review.md), which gives you the only sort in the course that is
  O(n log n) in the worst case *and* in place.
