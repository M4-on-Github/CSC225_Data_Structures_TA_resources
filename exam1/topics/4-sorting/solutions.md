# Topic 4 — solutions: sorting

Answers to [mock.md](mock.md), in order, each followed by what a complete answer needs.
**Attempt the paper first.** Every trace in this file was produced by running the reference sorts in
`practice/solutions/p3_sorts.py`, not written from memory — including the two buggy
versions in Q7.

---

## Part 1 — Drills

**4.1** (n−1) + (n−2) + … + 1 = **n(n−1)/2** = n²/2 − n/2. Drop the constant factor and
the lower-order term: **O(n²)**. This is the exact shape of selection sort. (Deck 3 s12.)

**4.2** `[1, 4, 2, 5, 8]`, **3 swaps** (5↔1, 5↔4, 5↔2). One pass guarantees only that the
**largest remaining value has reached its final slot** — which is why the inner range is
`range(n - 1 - pass_num)`. (Deck 7 s5–s6, code on s9.)

**4.3** If a whole pass makes no swap, the list is already sorted and the function breaks
out early. It turns bubble sort's **best case into O(n)**. It does nothing for the average
or worst case. (Deck 7 s7, s10.)

**4.4** Pass 1 scans the whole list for the **minimum** (1) and swaps it into position 0 →
`[1, 2, 9, 5]`. The full sort always makes **n(n−1)/2** comparisons — 6 here —
**regardless of the input**, including already-sorted input. Note selection sort is taught
in **Deck 3** (s10–s12), not the sorting deck; it only reappears in the summary table.

**4.5** Split: `[8,3,5,1]` → `[8,3]`, `[5,1]` → `[8]`, `[3]`, `[5]`, `[1]`. Merge: `[3,8]`
and `[1,5]` → `[1,3,5,8]`. The **merge** is where all the work is: compare the two front
elements, take the smaller, repeat. (Deck 7 s11–s13, code on s15.)

**4.6** `log n` is the **number of levels**: halving down to single elements takes log₂ n
splits. `n` is the **work per level**: merging all the pieces at one level touches every
element once. Levels × work per level = n log n. (Deck 7 s16 — he names the two repeated
actions, splitting and merging.)

**4.7** His code picks **`values[-1]` = 6**. left (< 6) = `[2, 1, 5, 4]`, middle (== 6) =
`[6]`, right (> 6) = `[7, 9]`. Then quick-sort left and right and concatenate.
(Deck 7 s18–s20, code on s22.)

**4.8** An **already-sorted (or reverse-sorted)** list. Taking the last element as pivot
then puts everything on one side, so the partition peels off one element at a time: n
levels instead of log n. He calls these **bad pivots**. (Deck 7 s23.)

**4.9**

| Sort | Best | Average | Worst |
|---|---|---|---|
| Selection | O(n²) | O(n²) | O(n²) |
| Bubble | **O(n)** | O(n²) | O(n²) |
| Insertion | **O(n)** | O(n²) | O(n²) |
| Merge | O(n log n) | O(n log n) | O(n log n) |
| Quick | O(n log n) | O(n log n) | **O(n²)** |

(Deck 7 s24, his five-row table.)

**4.10** **Merge and quick return new lists. Selection, bubble and insertion sort in
place** and return the same object. If you write `merge_sort(nums)` and then print `nums`
expecting it to be sorted, nothing happened — you threw the result away. (Deck 7 s15 and
s22 — compare his two functions line by line.)

---

## Part 2 — Exam-style questions

### Q1 — Sorting vocabulary
**(a)** **In place** — it rearranges the caller's list and returns that same list object,
using no second list. **Stable** — items that compare equal keep their original relative
order. (Deck 7 s15, s24.)

**(b)** **Bubble sort** or **insertion sort**. Both are stable and both are O(n²) in the
worst case. (Selection sort is O(n²) but is **not** stable; merge sort is stable but **is**
O(n log n).)

**What a complete answer needs**

- (a) Both definitions. "In place = no extra list" is enough; "stable = equal items keep
  their order" is enough.
- (b) Bubble **or** insertion. **Selection sort is wrong** — it is the trap in this
  question, because it scans the whole unsorted region whatever the data looks like.

### Q2 — Best cases
**(a)** The **`swapped` flag**: bubble sort notices when a whole pass makes no swaps and
**exits early**, so a sorted list costs one pass, O(n). Selection sort has no such check —
it must scan the entire unsorted region to be sure it has found the minimum, every pass,
whatever the data. (Deck 7 s4–s10; Deck 3 s10–s12.)

**(b)** The **comparison** count is identical — **45** both times, which is 10 × 9 / 2 —
because the inner loop never stops early; it has to see every remaining item before it can
claim to have the minimum. The **swap** count differs: **0** on the sorted list and **5**
on the reversed one. So selection sort does notice the shape of the data, but only in the
cheap operation, and Big-O is quoted on the comparison count. (Those are the numbers
`selection_sort_count` in `practice/solutions/p3_sorts.py` reports.)

**What a complete answer needs**

- (a) The early exit named **and** the fact that selection sort must scan the whole region
  regardless. Naming only the flag is half the mechanism.
- (b) Comparisons identical, swaps different. Getting 45 as well is a bonus. "Both are the
  same" and "sorted input is faster" are both wrong — the two halves of the question are
  deliberately opposite, and that is the thing to notice.

### Q3 — Where the growth rates come from
**(a)** **`[1, 2, 3, 4, 5]`** — already sorted. The pivot is `values[-1]` = **5**, so
`left = [1, 2, 3, 4]`, `middle = [5]`, `right = []`. One side gets **everything** and the
other gets **nothing**, so the recursion shrinks by **one element per level** instead of
halving: n levels, O(n) partitioning work at each, **O(n²)**. Reverse-sorted input does the
same thing the other way round. (Deck 7 s22–s23.)

**(b)** The **`log n`** is the **number of levels**: `mid = len(values) // 2` halves the
list, and you can only halve n down to 1 about log₂ n times. The **`n`** is the **merging
work on one level**: across a level every element is copied exactly once. log n levels ×
O(n) per level = **O(n log n)**, and nothing about the data changes either factor.
(Deck 7 s11–s16.)

**(c)** **Bubble sort**, and it is not close. The `swapped` flag makes the first pass
finish with no swaps, so it **breaks out after one pass** — about 10,000 comparisons,
**O(n)**. Merge sort has no such check: it splits and merges all the way down regardless,
about 10,000 × 14 ≈ 140,000 operations. Sorted input is bubble sort's **only** win over
merge sort. (Deck 7 s9–s10.)

**What a complete answer needs**

- (a) A sorted or reverse-sorted list **with** the split written out (one side empty), and
  "shrinks by one per level, so n levels". The list without the working is a remembered
  fact.
- If you answered all-equal values, e.g. `[4, 4, 4, 4, 4]`, that is **wrong for this
  version** but a sharp reading: the three-way split puts every equal item in `middle`, so
  it finishes in one level. Worth understanding why your answer failed.
- (b) Both halves — levels from halving, **and** O(n) work per level. One half alone does
  not get you to n log n.
- (c) Bubble **and** the early exit. "Merge sort, because O(n log n) beats O(n²)" is the
  trained reflex and is wrong here — it ignores the best case entirely.

### Q4 — Sorting by hand
**(a)**

| Pass | List after the pass | Any swaps? |
|---|---|---|
| 1 | `[1, 4, 2, 5, 8]` | yes |
| 2 | `[1, 2, 4, 5, 8]` | yes |
| 3 | `[1, 2, 4, 5, 8]` | **no** |
| 4 | — the loop has already broken | — |

The loop runs **3 passes**. The list is already sorted after pass 2, but bubble sort cannot
know that until a pass completes with no swaps — pass 3 is what sets `swapped = False` and
triggers the `break`.

**(b)** Down: `[8,3,5,1,7,2]` → `[8,3,5]` and `[1,7,2]` → `[8]`, `[3,5]` and `[1]`,
`[7,2]` → `[3]`, `[5]` and `[7]`, `[2]`.

Up: `[3]`+`[5]` → `[3,5]`; `[8]`+`[3,5]` → `[3,5,8]`; `[7]`+`[2]` → `[2,7]`;
`[1]`+`[2,7]` → `[1,2,7]`; finally `[3,5,8]`+`[1,2,7]` → **`[1,2,3,5,7,8]`**.

Note `mid = len(values) // 2`, so the six-element list splits 3/3 and the three-element
lists split 1/2 — **not** 2/1. (Deck 7 s11–s16.)

**What a complete answer needs**

- (a) All three pass rows, with pass 3 recorded as "no swaps" — that row *is* the answer to
  "how many passes".
- The common wrong answer is 2 passes. If that was yours, the trace was right but you
  missed that the early exit needs one clean pass to notice it is done.
- (b) The 3/3 top split, the 1/2 sub-splits, the two merged halves `[3,5,8]` and
  `[1,2,7]`, and the final list.
- If you split 2/1, the rest of your tree can still be correct on its own terms — check
  the method before you check the match.

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
(Deck 3 s10–s12.)

**(b)** Pivot = **3**. `left = [2]` · `middle = [3]` · `right = [6, 8, 4, 10]`. It then
calls `quick_sort([2])` and `quick_sort([6, 8, 4, 10])`, and returns their results with
`middle` between them. The finished list is **`[2, 3, 4, 6, 8, 10]`**.

Note how badly that first split went: 1 item on the left and 4 on the right. The pivot was
the **second smallest** item in the list, and `values[-1]` has no way of knowing that.
(Deck 7 s22.)

**(c)**

| After i = | List |
|---|---|
| 1 | `[2, 5, 4, 1]` |
| 2 | `[2, 4, 5, 1]` |
| 3 | `[1, 2, 4, 5]` |

Three iterations, not four: the outer loop starts at **1**, because the one-element region
to the left of index 1 is already sorted by definition. (Deck 7 s26–s29.)

**What a complete answer needs**

- (a) All five pass rows, and **10**.
- Passes 3 and 5 being **unchanged** is what separates a real trace from a remembered one.
  Quietly "fixing" those rows to make progress traces a sort that does not exist.
- Either 10 or the working 4+3+2+1. Noticing that the last pass makes 0 comparisons is a
  good sign.
- (b) The three-way split with pivot 3, and the two recursive calls. A full correct trace
  to `[2, 3, 4, 6, 8, 10]` with a right side of `[6, 8, 4, 10]` has both.
- `left = [2]` and `right = [6, 8, 4, 10]` **in the original order** — the lecture version
  appends in one pass and does not sort the sides.
- (c) All three rows. Four rows instead of three means you started the outer loop at 0;
  the lists are still right, so the trace is sound and the loop bound is not.

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
`merge_sort(data)` on its own, with the return value thrown away, sorts nothing.
(Deck 7 s15, s22.)

**What a complete answer needs**

- Both output lines, and the in-place versus new-list explanation.
- `[1, 2, 3] False` on the second line means you know merge sort returns a new list but
  think it also mutates the original. The prose can still be right; the output is not.

### Q7 — Two sorts out of a student's homework
**(a)** The missing token is **`j >= 0`**: the line should read
`while j >= 0 and values[j] > current`. As written, nothing stops `j` going negative.

On `[5, 2, 4, 1, 3]` it raises **`IndexError: list index out of range`**. And it does
something worse before it gets there: once `j` is `-1`, `values[-1]` is **legal Python** —
it reads the *last* item of the list — so the loop keeps comparing and overwriting from the
far end of the list for a few turns, corrupting it, and only crashes once `j` runs past
`-len(values)`. A silent wrong answer followed by a crash is the hardest kind of bug to
read.

`[1, 2, 3]` survives because **no element ever has to move**. The `while` test fails on the
very first check of every pass, so `j` is never decremented and never reaches `-1`. Testing
a sort on already-sorted input proves almost nothing — that is the lesson worth taking from
this one.

**(b)** `swapped = False` is **outside** the outer loop. It should be the first line
*inside* it, reset once per pass. As written it is set to `True` by the first swap anywhere
and then **never goes back to `False`**, so `if not swapped` can only ever fire on a pass
that is the very first pass.

The output is still correct — the passes do the sorting and the flag only ever skipped
work — but the **early exit is dead**, so the best case decays from **O(n)** back to
**O(n²)**. Bubble sort's one advantage over selection sort is exactly that early exit, so
this version has no reason to exist.

**`[2, 1, 3, 4, 5, 6]`** shows it: the lecture version sorts it in **2 passes** (pass 1
swaps, pass 2 is clean and breaks). This version takes all **5**. Note
`[1, 2, 3, 4, 5, 6]` does *not* show it — both stop after one pass — so the input has to
need exactly one swap and then be done.

**What a complete answer needs**

- (a) The missing `j >= 0` named, **IndexError** on that input, and "nothing moves, so `j`
  never goes negative" on the sorted list.
- Noticing that `values[-1]` reads from the end **before** the crash is a better reading of
  the code than the question asks for.
- "It returns the wrong answer", with no IndexError, is a plausible guess — run it and see.
- (b) The flag not being reset per pass, and **the O(n) best case lost**, with an input
  that demonstrates it.
- `[1, 2, 3, 4, 5, 6]` is the input most people reach for and it does **not** demonstrate
  the bug — both versions break after one pass there. Trace it and see why.
- "Nothing is wrong, it sorts fine" is the honest answer of someone who only checked the
  output. The question says it sorts correctly; the cost is the point.

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
drop it into the gap. The region to the left of `i` is always sorted. (Deck 7 s26–s29.)

**(b)** **Best case O(n)** — an **already-sorted** list: the `while` condition fails
immediately on every pass, so each element is compared once. **Worst case O(n²)** — a
reverse-sorted list, where every element slides all the way to the front.

**(c)** **Stable:** the two `2`s come out in the order they went in, because the `while`
test is `values[j] > current` and not `>=` — an equal element stops the slide rather than
being stepped over.

**What a complete answer needs**

Five things in the code, and every one of them is a place people slip:

- **Class form** — reads and writes `self.values`, signature `def insertion_sort(self)`,
  no globals, no extra parameters.
- **Outer loop starts at 1**, not 0. Starting at 0 still sorts, but it means the invariant
  ("everything left of `i` is already in order") has not landed.
- **The inner slide:** `while j >= 0 and values[j] > current`, with **both** halves of the
  condition. Missing `j >= 0` is an `IndexError`, as Q7 just showed.
- `values[j + 1] = current` **after** the loop, with the `+ 1` right.
- `return values` (or `return self.values`) — the **same object**, not a copy.
  `return list(values)` breaks the convention the tests check with `assertIs`.
- A correct **selection** or **bubble** sort here is working code that answers a different
  question: this one names the algorithm.
- (b) O(n) / O(n²) **and** sorted input named.
- (c) Equal items keeping their relative order. Mentioning the `>` versus `>=` is better
  still.

### Q9 — Choosing a sort for a real list
**(a)** **Insertion sort.** The deciding operation is its inner
`while j >= 0 and values[j] > current` — for each of the 40,000 records already in place
that test **fails on the first check**, so they cost one comparison each and never move.
Only the 12 appended records actually slide, and each slides only as far as it has to.
Total work is about n plus the number of out-of-order pairs, so this is near-O(n) in
practice even though insertion sort is O(n²) in the worst case. (Deck 7 s26–s29.)

Bubble sort is a defensible second answer — its `swapped` early exit also loves
nearly-sorted data — but it is weaker here, because a record appended at the **end** that
belongs at the **front** moves only one slot per pass, so bubble sort needs many passes
where insertion sort needs one slide. Merge sort is the wrong answer: it does the same
O(n log n) work whatever the input, and sorted input buys it nothing.

**(b)** Of the five, only **selection, bubble and insertion sort are in place**, so those
are the three you can use — and all three are **O(n²)**, which on 2 million items is
roughly 2 × 10¹² comparisons. That is the cost. **Merge sort** allocates a new list at
every level of the recursion and **quick sort**, as lecture writes it, builds `left`,
`middle` and `right` on every call, so both are out on the memory rule no matter how good
their growth rate is.

The algorithm that removes the trade-off is **heap sort** — specifically the in-place
version, which builds a max-heap inside the list itself and then repeatedly swaps the root
to the back. It is **O(n log n)** *and* **in place**, which no other sort in this course
manages. It is not stable, and that is the one thing you do give up.
([Topic 5](../5-heaps/review.md).)

**What a complete answer needs**

- (a) **Insertion sort** (or bubble, if you argue it), **and** the inner `while` / the
  early exit named as the deciding operation. The algorithm without the mechanism is a
  guess that happened to land.
- **Merge sort is the wrong answer here**, and it is the most common one, because
  O(n log n) has been drilled as the better number. The whole point of the question is that
  the shape of the input beats the asymptotic class.
- (b) The in-place three named **and** the O(n²) price, plus **heap sort** as the in-place
  O(n log n) answer.
- "Merge sort is fine because O(n log n) is better" ignores the constraint the question
  sets. Quick sort "is in place" is a reasonable belief from other courses but not from
  **this** code — look at the three lists it builds.
- Losing stability is worth adding.

---

## If you got it wrong

- Anything wrong in **Q4 or Q5** — you cannot write a sort you cannot trace. Redo the trace
  on paper, then check it with `bubble_sort_passes` and `selection_sort_count` in
  `practice/solutions/p3_sorts.py`, which exist for exactly this.
- Anything wrong in **Q6** — Deck 7 s15 against s22, side by side. In place versus new list
  is the cheapest thing in the topic to get right and the most commonly thrown away.
- Anything wrong in **Q8** — go and write all five sorts: `practice/p3_sorts.py`, then
  `practice/p4_sortable_list.py`. The tests check the return-object convention with
  `assertIs`, so they catch exactly what Q8 is checking.
- Anything wrong in **Q9** — the "which sort, and why" table in [review.md](review.md).
  Both halves of that question punish answering O(n log n) by reflex.
