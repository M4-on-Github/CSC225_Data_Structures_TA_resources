# Topic 2 — solutions: Big-O and counting operations

Answers to [mock.md](mock.md), in order, each followed by what a complete answer needs.
**Attempt the paper first.** Every count in this file was produced by running the code, not from memory.

---

## Part 1 — Drills

**2.1** Wall-clock time depends on the machine, the language and what else is running. An
operation count depends on the algorithm and the input, so it still means
something on a different computer. (Deck 3 s6–s7.)

**2.2** **O(1)** indexing a list · **O(log n)** binary search · **O(n)** linear search ·
**O(n log n)** merge sort · **O(n²)** selection sort · **O(2ⁿ)** trying every subset.
(Deck 3 s20–s21.)

**2.3** Big-O keeps only the **fastest-growing term** and **throws away constant
factors**, because it describes how cost *scales*, not what it is at one particular n.
(Deck 3 s18–s19.)

**2.4** (i) **O(1)** · (ii) **O(n)** · (iii) **O(n)** — sequential blocks **add**, and
O(n) + O(n) = O(2n) = O(n) · (iv) **O(n²)** — nesting **multiplies** · (v) **O(log n)**.
(Deck 3 s19 for the simplifying rules, s25 for the two laws.)

**2.5** Big-O is about **growth, not a stopwatch reading at one input size**. An O(n²)
algorithm can easily beat an O(n log n) one on small n. The claim it makes is about what
happens when n gets large. In this question, it is a **worst-case upper bound**, not a
prediction of the run you just did. Big-O can also describe best- or average-case costs
when those are the cases being analysed. (Deck 3 s17, s22 — the "constants can fool us" table.)

---

## Part 2 — Exam-style questions

### Q1 — Counting operations
**(a)** Exactly **n** additions — one per element, no more and no fewer. **O(n)**: the
count is a constant multiple of n, and the loop body does a fixed amount of work.

**(b)** Worst case **n(n−1)/2** comparisons. The outer loop runs n times and the inner
loop starts at `i + 1`, so it runs n−1 times, then n−2, down to 0:
(n−1) + (n−2) + … + 1 = n(n−1)/2. That is **O(n²)**.

For n = 6 with no duplicates the count is exactly 15, which is 6 × 5 / 2.

Best case **O(1)**, from an input whose **first two items are equal** — for example
`[7, 7, 1, 2, 3, 4]`. It returns on the very first comparison, so the count is 1 whatever
n is, for n ≥ 2. This is an algorithm whose best and worst cases are in different growth
classes entirely, which is why the question has to say which one it wants.

**(c)** **O(log n)** — the loop divides `n` by two each pass, so the number of passes is
the number of halvings. For `n = 1000` it returns **9**: 1000 → 500 → 250 → 125 → 62 → 31
→ 15 → 7 → 3 → 1, which is nine divisions. (That is ⌊log₂ 1000⌋.)

**What a complete answer needs**

- (a) **n** *and* **O(n)**. "O(n)" on its own skips the counting, which is the thing being
  practised. "n + 2" is not the addition count: the initialisation and the return are not
  additions.
- (b) Three things: the shrinking sum **and** n(n−1)/2; **O(n²)**; and the **O(1)** best
  case **with an input that shows it**. If the only equal pair is the final two items,
  the function still makes all n(n−1)/2 comparisons, so that is a worst case.
- (c) **O(log n)** *and* **9**. 10 is the common slip — count the divisions, not the
  numbers in the chain.

### Q2 — Simplifying
**(a)**

| Operation count | Big-O |
|---|---|
| 3n² + 7n + 2 | **O(n²)** |
| 100n + 5000 | **O(n)** |
| n/2 | **O(n)** |
| n(n−1)/2 | **O(n²)** |

Row 2 and row 3 are the same class, which is the point of putting them next to each other:
a constant factor of 100 and a constant factor of ½ are both just constant factors.

**(b)** O(1), O(log n), O(n log n), O(n²).

**(c)** **O(1)**. The cost does not depend on n at all, so it is constant — and no, it is
not necessarily fast. A million operations is a million operations; O(1) says it will
**stay** a million as the input grows, not that the number is small. This is the other half
of the "constants can fool us" point (Deck 3 s22).

**What a complete answer needs**

- (a) All four rows. `O(3n²)` is equivalent to `O(n²)`, but it is not simplified — dropping
  the constant is the thing the question is testing.
- (b) The exact order; a single transposition means the ranking is not yet automatic.
- (c) **O(1)**, and then the harder half: O(1) is about **growth**, not about size.
  "Yes, O(1) is the fastest class" is the trained reflex, and it is the trap here.

### Q3 — The two laws
- **(a) O(n)** — the **add law**: two blocks one after the other add, and O(n) + O(n) =
  O(2n) = O(n).
- **(b) O(n²)** — the **multiply law**: the inner loop runs n times for each of the outer
  loop's n iterations, so the body runs n × n times.
- **(c) O(1)** — neither line depends on n. Indexing is address arithmetic and `len` reads
  a stored size; no loop, no growth.
- **(d) O(n log n)** — the multiply law again, with unequal factors: n iterations of the
  outer loop, each doing an O(log n) binary search, so n × log n.

**What a complete answer needs**

- Each snippet needs the Big-O **and** the law that decides it. The Big-O alone is the
  answer; the law is the reason, and the reason is the part worth practising.
- (a) being answered O(n²) is the single most common error in this question. Two loops
  **side by side** are O(n); two loops **nested** are O(n²), and on the page the difference
  is one level of indentation.
- (d) answered as O(n) means you read the binary search as a constant-time operation — it
  is the `while` loop inside the `for` that makes it O(n log n).

### Q4 — Where n(n−1)/2 comes from
**(a)** The first pass compares the candidate against n−1 items, the next against n−2, and
so on down to 1. The sum (n−1) + (n−2) + … + 1 is **n(n−1)/2**, which is O(n²).
(Deck 3 s10–s12.)

**(b)** **28.** 8 × 7 / 2 = 28. The count does not depend on the data at all, so "already
sorted" changes nothing — that is the point of asking it this way.

**(c)** **Yes.** n(n−1)/2 expands to n²/2 − n/2; drop the constant factor ½ and the
lower-order term n/2 and what is left is n². Same growth class, so the same Big-O.

**What a complete answer needs**

- (a) The shrinking sum written out **and** the closed form. The closed form quoted alone
  is a memorised fact, not a derivation.
- (b) **28**. "0" or "7" is the answer of someone who thinks sorted input helps.
- (c) **Yes**, with the dropped constant **and** the dropped lower-order term shown.
  "Yes, they are both quadratic" with no working skips the whole question.

### Q5 — Halving, and what Big-O is claiming
**(a)** Linear search: up to **1,000,000** comparisons — **O(n)**. Binary search: about
**20** — **O(log n)**, since 2²⁰ = 1,048,576, so twenty halvings cover a million items.
(Deck 3 s28–s30.)

**(b)** About **19 or 20** — and the measured answer from `binary_search_count` in
`practice/p2_search.py` is exactly **19** for the specified search for `-1`. The reason is
that binary search's cost grows with the number of **halvings**, not with the number of
items: 1,000 needs about 10
halvings and 1,000,000 needs about 20. Each extra comparison **doubles** the size of list
you can handle, so multiplying the data by a thousand adds roughly ten comparisons, not a
thousand.

That sentence is the whole value of O(log n), and it is why 9 → 19 is a better thing to
have seen than any amount of asserting that logarithms grow slowly.

**(c)** The small test hid the growth rate. At n = 20, n² is only 400, so a quadratic
algorithm can finish quickly. Going from 20 to 20,000 multiplies n by 1,000 and therefore
multiplies the **n² term** by **1,000,000**. If that term dominates the work, the operation
count grows by about that factor. For a cost proportional to n log₂ n, the corresponding
factor is roughly 1,000 × (14.3/4.3) ≈ 3,300. These are growth estimates, not exact running
times guaranteed by Big-O.

What Big-O **was** claiming: how the cost **grows** as n grows, as an upper bound on the
worst case. What it was **not** claiming: that the program would be slow at n = 20, or that
any particular run would take any particular number of seconds. Your friend tested a claim
Big-O never made and drew a conclusion about one it did. (Deck 3 s17, s22.)

**What a complete answer needs**

- (a) Both halves: 1,000,000 / O(n), and "about 20" / O(log n). "20 because 2²⁰ is about a
  million" is the justification worth having; a bare 20 with no reason is a remembered
  number.
- (b) A prediction in the high teens or twenty, **and** the doubling argument — each
  comparison doubles the list size you can cover. A prediction of 9,000 or of 9,000,000
  means the halving has not landed yet.
- (c) The growth argument with actual numbers (n × 1,000 gives the n² term × 1,000,000), **and**
  the separation between what Big-O claims (growth, worst case, large n) and what it does
  not (seconds, small n). "O(n²) is slow" does not answer the question, which is *why the
  small test was misleading*.

---

## If you got it wrong

- Anything wrong in **Q3** — Deck 3 s25–s27, the two laws. This is the most mechanical
  part of the topic and the cheapest to fix.
- Anything wrong in **Q1(b)** or **Q4** — Deck 3 s10–s12. The shrinking sum reappears as
  selection sort in [Topic 4](../4-sorting/review.md) and as the copying cost of a +1-growth
  array in [Topic 3](../3-arrays/review.md), so it is worth owning.
- Anything wrong in **Q5** — Deck 3 s17 and s22, then go and run
  `practice/p2_search.py`'s counting functions. Q5(b) stops being an argument once you
  have watched the number.
