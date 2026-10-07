# Topic 4 — solutions: sorting

Try the [questions](mock.md) before checking these answers.

---

## Part 1 — Drills

**4.1** (n−1) + (n−2) + … + 1 = **n(n−1)/2** = n²/2 − n/2. Drop the constant factor and
the lower-order term: **O(n²)**. This is the exact shape of selection sort.

**4.2** After a pass with no swaps, the list is sorted, so the algorithm stops.

**4.3** Pass 1 scans the whole list for the **minimum** (1) and swaps it into position 0 →
`[1, 2, 9, 5]`. The full sort always makes **n(n−1)/2** comparisons — 6 here —
**regardless of the input**, including already-sorted input.

**4.4** Split: `[8,3,5,1]` → `[8,3]`, `[5,1]` → `[8]`, `[3]`, `[5]`, `[1]`. Merge: `[3,8]`
and `[1,5]` → `[1,3,5,8]`. The **merge** is where all the work is: compare the two front
elements, take the smaller, repeat.

**4.5** `log n` is the **number of levels**: halving down to single elements takes log₂ n
splits. `n` is the **work per level**: merging all the pieces at one level touches every
element once. Levels × work per level = n log n.

**4.6** The lecture version picks **`values[-1]` = 6**. left (< 6) = `[2, 1, 5, 4]`, middle (== 6) =
`[6]`, right (> 6) = `[7, 9]`. Then quick-sort left and right and concatenate.


**4.7** Sorted or reverse-sorted distinct values put the last-item pivot at one extreme each time. The remaining partitions have sizes `n−1, n−2, ...`, so the work is O(n²).

**4.8**

| Sort | Worst case | Why |
|---|---|---|
| Selection | O(n²) | Scans `(n−1) + ... + 1` pairs |
| Bubble | O(n²) | Reverse order needs repeated swaps |
| Insertion | O(n²) | Reverse order needs repeated shifts |
| Merge | O(n log n) | O(n) merge work at each of O(log n) levels |
| Quick | O(n²) | Extreme pivots leave one item behind per level |

**4.9** **Merge and quick return new lists** for inputs of length at least two; their
empty-list and singleton base cases return the original list. **Selection, bubble and
insertion sort in place** and return the same object. If you write `merge_sort(nums)` and
then print `nums` expecting an unsorted list to have changed, you threw the sorted result
away.

---

## Part 2 — Exam-style questions

### Q1 — Sorting vocabulary
**(a)** **In place** — it rearranges the caller's list using O(1) extra space; returning
that same object is a separate convention of these implementations. **Stable** — items
that compare equal keep their original relative order.

**(b)** **Bubble sort** or **insertion sort**. Both are stable and both are O(n²) in the
worst case. The three-way **quick sort shown here** also qualifies: its partitions
preserve input order, so it is stable, and its worst case is O(n²). Selection sort is
O(n²) but is **not** stable; merge sort is stable but **is** O(n log n).


### Q2 — Selection sort's repeated work
**(a)** Each pass scans the entire unsorted region to find its minimum, regardless of the input order.

**(b)** Each run makes `9 + 8 + ... + 1 = 45` comparisons. The implementation skips self-swaps, so its swaps can differ: zero on sorted input and five on reversed input. The comparisons determine the O(n²) worst-case cost.

### Q3 — Where the growth rates come from
**(a)** `[1, 2, 3, 4, 5]` makes pivot 5. The first split gives left `[1, 2, 3, 4]`, middle `[5]`, right `[]`. Each level scans its input but removes only one item: O(n²) total.

**(b)** Merge sort halves the input through O(log n) levels. Merging all pieces at any one level touches O(n) items, giving O(n log n).

**(c)** Merge sort has the better worst-case bound: O(n log n) versus bubble sort's O(n²). A reversed list makes bubble sort repeat many swaps.

### Q4 — Sorting by hand
**(a)**

| Pass | List after the pass | Any swaps? |
|---|---|---|
| 1 | `[1, 4, 2, 5, 8]` | yes |
| 2 | `[1, 2, 4, 5, 8]` | yes |
| 3 | `[1, 2, 4, 5, 8]` | **no** |
| 4 | — the loop has already broken | — |

The loop runs **3 passes**. The list is already sorted after pass 2, but bubble sort cannot
know that until a pass completes with no swaps — pass 3 leaves `swapped = False` and
triggers the `break`.

**(b)** Down: `[8,3,5,1,7,2]` → `[8,3,5]` and `[1,7,2]` → `[8]`, `[3,5]` and `[1]`,
`[7,2]` → `[3]`, `[5]` and `[7]`, `[2]`.

Up: `[3]`+`[5]` → `[3,5]`; `[8]`+`[3,5]` → `[3,5,8]`; `[7]`+`[2]` → `[2,7]`;
`[1]`+`[2,7]` → `[1,2,7]`; finally `[3,5,8]`+`[1,2,7]` → **`[1,2,3,5,7,8]`**.

Note `mid = len(values) // 2`, so the six-element list splits 3/3 and the three-element
lists split 1/2 — **not** 2/1.


### Q5 — Three more sorts by hand
**(a)**

| Pass | List after the pass |
|---|---|
| 1 | `[10, 29, 14, 37, 13]` |
| 2 | `[10, 13, 14, 37, 29]` |
| 3 | `[10, 13, 14, 37, 29]` *(unchanged)* |
| 4 | `[10, 13, 14, 29, 37]` |
| 5 | `[10, 13, 14, 29, 37]` *(unchanged)* |

**10 comparisons** — 4 + 3 + 2 + 1 + 0, which is 5 × 4 / 2. Passes 3 and 5 change nothing
because the minimum of the remaining region is **already in place**, so the element is
swapped with itself. Selection sort has no way to notice that and skip the pass.


**(b)** Pivot = **3**. `left = [2]` · `middle = [3]` · `right = [6, 8, 4, 10]`. It then
calls `quick_sort([2])` and `quick_sort([6, 8, 4, 10])`, and returns their results with
`middle` between them. The finished list is **`[2, 3, 4, 6, 8, 10]`**.

Note how badly that first split went: 1 item on the left and 4 on the right. The pivot was
the **second smallest** item in the list, and `values[-1]` has no way of knowing that.


**(c)**

| After i = | List |
|---|---|
| 1 | `[2, 5, 4, 1]` |
| 2 | `[2, 4, 5, 1]` |
| 3 | `[1, 2, 4, 5]` |

Three iterations, not four: the outer loop starts at **1**, because the one-element region
to the left of index 1 is already sorted by definition.


### Q6 — Reading the code
```
[1, 2, 3] True
[3, 1, 2] False
```

- **`bubble_sort` works in place**: it rearranges the caller's list and returns that same
  object, so `data` is sorted and `a is data` is `True`.
- **`merge_sort` builds a new list**: it returns a sorted copy and leaves the input alone,
  so `data2` is untouched and `b is data2` is `False`. The sorted result is in `b`.

This is the distinction that turns a correct algorithm into a wrong answer —
`merge_sort(data)` on its own, with the return value thrown away, leaves `data` unchanged.



### Q7 — Two sorts out of a student's homework
**(a)** The missing guard is **`j >= 0 and`**: the line should read
`while j >= 0 and values[j] > current:`. As written, nothing stops `j` going negative.

On `[5, 2, 4, 1, 3]` it raises **`IndexError: list index out of range`**. And it does
something worse before it gets there: once `j` is `-1`, `values[-1]` is **legal Python** —
it reads the *last* item of the list — so the loop keeps comparing and overwriting from the
far end of the list for a few turns, corrupting it, and only crashes once `j` runs past
`-len(values)`. Silent data corruption followed by a crash is a difficult kind of bug to
read.

`[1, 2, 3]` survives because **no element ever has to move**. The `while` test fails on the
very first check of every pass, so `j` is never decremented and never reaches `-1`. Testing
a sort on already-sorted input proves almost nothing — that is the lesson worth taking from
this one.

**(b)** `swapped = False` is **outside** the outer loop. It should be the first line
*inside* it, reset once per pass. As written it is set to `True` by the first swap anywhere
and then **never goes back to `False`**, so `if not swapped` can only ever fire on a pass
that is the very first pass.

The output is still correct — the passes do the sorting and the flag only skips work —
but the **early exit stops working after the first swap**.

**`[2, 1, 3, 4, 5, 6]`** shows it: the lecture version sorts it in **2 passes** (pass 1
swaps, pass 2 is clean and breaks). This version takes all **5**. Note
`[1, 2, 3, 4, 5, 6]` does *not* show it — both stop after one pass. Choose an input that
needs a swap but becomes sorted well before the final pass.


### Q8 — Write a sort as a method
**(a)**

```python
    def insertion_sort(self):
        values = self.values
        for i in range(1, len(values)):
            current = values[i]
            j = i - 1
            while j >= 0 and values[j] > current:
                values[j + 1] = values[j]
                j -= 1
            values[j + 1] = current
        return values
```

Take each element from index 1 onward, slide everything larger one slot to the right, and
drop it into the gap. The region to the left of `i` is always sorted.

**(b)** **Worst case O(n²)** on a reverse-sorted list: each next item shifts all the way to the front.

**(c)** **Stable:** the two `2`s come out in the order they went in, because the `while`
test is `values[j] > current` and not `>=` — an equal element stops the slide rather than
being stepped over.


### Q9 — Choosing a sort for a real list
**(a)** **Merge sort.** It is stable, so equal IDs retain their order, and its worst-case cost is O(n log n). The question permits the extra memory it needs.

**(b)** Selection, bubble and insertion sort are the in-place choices among these five, each with O(n²) worst-case cost. The taught merge and quick sorts build new lists. The in-place **heap sort** from [Topic 5](../5-heaps/review.md) uses O(1) auxiliary space and O(n log n) worst-case time, but it is not stable.

### Q10 — From name to pseudocode to Python

**(a)** One valid version of each. Wording may differ; check the bounds, comparisons,
base cases, and return behavior.

```text
SELECTION(A):
    FOR i from 0 to second-last index:
        smallest = i
        FOR j from i + 1 to last index:
            IF A[j] < A[smallest]: smallest = j
        SWAP A[i] and A[smallest]
    RETURN A

BUBBLE(A):
    FOR each pass from 0 to second-last index:
        swapped = false
        FOR j from 0 to n - 2 - pass:
            IF A[j] > A[j + 1]: SWAP them; swapped = true
        IF not swapped: STOP
    RETURN A

INSERTION(A):
    FOR i from 1 to last index:
        current = A[i]; j = i - 1
        WHILE j >= 0 AND A[j] > current:
            MOVE A[j] to A[j + 1]; DECREASE j
        PUT current at A[j + 1]
    RETURN A

MERGE(A):
    IF size <= 1: RETURN A
    SPLIT A in half; recursively sort each half with MERGE
    WHILE both sorted halves have items: TAKE the smaller front item
        into a new list (take from left on a tie)
    APPEND all leftovers to the new list
    RETURN the new list

QUICK(A):
    IF size <= 1: RETURN A
    CHOOSE the last item as pivot
    SCAN A into smaller, equal, larger lists
    RETURN QUICK(smaller) + equal + QUICK(larger)
```

**(b)** **Insertion sort.** After `i = 1, 2, 3`, the lists are
`[2, 4, 3, 1]`, `[2, 3, 4, 1]`, and `[1, 2, 3, 4]`. A direct Python translation is:

```python
def insertion_sort(values):
    for i in range(1, len(values)):
        current = values[i]
        j = i - 1
        while j >= 0 and values[j] > current:
            values[j + 1] = values[j]
            j -= 1
        values[j + 1] = current
    return values
```

**(c)** 1 **Bubble**, 2 **selection**: both change and return the input list.
3 **Merge**, 4 **quick**: both return a new list for length greater than one.
The three partitions and last-item pivot distinguish this quick sort.

**(d)** `smallest` must start at **`i`**, the first position still unsorted. With
`smallest = 0`, `[1, 3, 2]` stays the same after pass 0, but pass 1 swaps positions
1 and 0 and gives `[3, 1, 2]`. The minimum at position 0 was already finished.
