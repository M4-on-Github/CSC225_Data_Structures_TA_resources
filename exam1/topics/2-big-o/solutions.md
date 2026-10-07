# Topic 2 — solutions: Big-O and counting operations

Try the [questions](mock.md) before checking these answers.

---

## Part 1 — Drills

**2.1** Wall-clock time depends on the machine, the language and what else is running. An
operation count depends on the algorithm and the input, so it still means
something on a different computer.

**2.2** **O(1)** indexing a list · **O(log n)** repeated halving · **O(n)** linear search ·
**O(n log n)** merge sort · **O(n²)** selection sort · **O(2ⁿ)** trying every subset.


**2.3** Big-O keeps only the **fastest-growing term** and **throws away constant
factors**, because it describes how cost *scales*, not what it is at one particular n.


**2.4** (i) **O(1)** · (ii) **O(n)** · (iii) **O(n)** — sequential blocks **add**, and
O(n) + O(n) = O(2n) = O(n) · (iv) **O(n²)** — nesting **multiplies** · (v) **O(log n)**.


**2.5** Big-O is about **growth, not a stopwatch reading at one input size**. An O(n²)
algorithm can easily beat an O(n log n) one on small n. The claim it makes is about what
happens when n gets large. In this question, it is a **worst-case upper bound**, not a
prediction of the run you just did.

---

## Part 2 — Exam-style questions

### Q1 — Counting operations
**(a)** Exactly **n** additions — one per element, no more and no fewer. **O(n)**: the
count is a constant multiple of n, and the loop body does a fixed amount of work.

**(b)** Worst case **n(n−1)/2** comparisons. The outer loop runs n times and the inner
loop starts at `i + 1`, so it runs n−1 times, then n−2, down to 0:
(n−1) + (n−2) + … + 1 = n(n−1)/2. That is **O(n²)**.

For n = 6 with no duplicates the count is exactly 15, which is 6 × 5 / 2.

**(c)** **O(log n)** — the loop divides `n` by two each pass, so the number of passes is
the number of halvings. For `n = 1000` it returns **9**: 1000 → 500 → 250 → 125 → 62 → 31
→ 15 → 7 → 3 → 1, which is nine divisions. (That is ⌊log₂ 1000⌋.)


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
of the "constants can fool us" point.


### Q3 — The two laws
- **(a) O(n)** — the **add law**: two blocks one after the other add, and O(n) + O(n) =
  O(2n) = O(n).
- **(b) O(n²)** — the **multiply law**: the inner loop runs n times for each of the outer
  loop's n iterations, so the body runs n × n times.
- **(c) O(1)** — neither line depends on n. Indexing is address arithmetic and `len` reads
  a stored size; no loop, no growth.
- **(d) O(n log n)** — the multiply law again: n outer iterations, each halving
  `width` O(log n) times.


### Q4 — Where n(n−1)/2 comes from
**(a)** The first pass compares the candidate against n−1 items, the next against n−2, and
so on down to 1. The sum (n−1) + (n−2) + … + 1 is **n(n−1)/2**, which is O(n²).


**(b)** **28.** 8 × 7 / 2 = 28. The count does not depend on the data at all, so "already
sorted" changes nothing — that is the point of asking it this way.

**(c)** **Yes.** n(n−1)/2 expands to n²/2 − n/2; drop the constant factor ½ and the
lower-order term n/2 and what is left is n². Same growth class, so the same Big-O.


### Q5 — Halving, and what Big-O is claiming
**(a)** A full scan takes **1,000,000** iterations — **O(n)**. Repeated halving
takes **19** divisions — **O(log n)** — to bring 1,000,000 down to 1.


**(b)** **19**. Dividing 1,000,000 by two until it reaches 1 takes ten more
steps than dividing 1,000. Each additional halving lets the starting size be
about twice as large, so a thousandfold increase adds about ten steps.

**(c)** The small test hid the growth rate. At n = 20, n² is only 400, so a quadratic
algorithm can finish quickly. Going from 20 to 20,000 multiplies n by 1,000 and therefore
multiplies the **n² term** by **1,000,000**. If that term dominates the work, the operation
count grows by about that factor. For a cost proportional to n log₂ n, the corresponding
factor is roughly 1,000 × (14.3/4.3) ≈ 3,300. These are growth estimates, not exact running
times guaranteed by Big-O.

What Big-O **was** claiming: how the cost **grows** as n grows, as an upper bound on the
worst case. What it was **not** claiming: that the program would be slow at n = 20, or that
any particular run would take any particular number of seconds. Your friend tested a claim
Big-O never made and drew a conclusion about one it did.
