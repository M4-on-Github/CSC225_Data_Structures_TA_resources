# Topic 2 — Big-O and counting operations

**Source:** Algorithm Efficiency Introduction (39 slides). **Lecture weight:** heavy.

---

## What this topic is

A vocabulary with exactly **six words** in it, plus **two rules** for combining them, plus
**one habit**: count operations instead of seconds. That is the whole topic. It is short,
and every later topic is scored in its units — Topic 3 prices array operations with it,
Topic 4 compares five sorts with it, Topic 5 justifies a heap with it.

The reason it comes before the data structures is that it is the only way to compare two
structures that do the same job. Without it, "a list is slow at the front" is an opinion.

---

## The ideas, in the order they depend on each other

- **Count operations, not seconds.** A stopwatch measures your laptop, the language, and
  whatever else the machine was doing. An operation count measures the **algorithm**, and
  still means something on a different computer.
- **Count as a function of n**, where n is the size of the input — usually the length of
  the list.
- **The six classes, slowest-growing first:** O(1), O(log n), O(n), O(n log n), O(n²),
  O(2ⁿ). Nothing else is used in this course.
- **Drop constants and lower-order terms.** 3n² + 7n + 2 is **O(n²)**. Big-O describes how
  cost *scales*, not what it is at one particular n, so a factor of 3 and a `+ 7n` change
  nothing about the shape.
- **The add law:** code blocks one after another **add**. O(n) then O(n) is O(2n), which
  is **O(n)**.
- **The multiply law:** nested code **multiplies**. A loop of n inside a loop of n is
  **O(n²)**.
- **n(n−1)/2** is the count you get when an inner loop shrinks by one each pass:
  (n−1) + (n−2) + … + 1. It is **O(n²)**, and it is exactly selection sort's comparison
  count.
- **O(log n) means repeated halving.** Twenty halvings get you through a million items,
  and that is the entire argument for binary search over linear search.
- **Big-O is an upper bound on growth, not a prediction of a stopwatch reading.** An
  O(n²) algorithm can beat an O(n log n) one at n = 10. The claim is about large n.
- **Best, average and worst case are three different questions.** This course usually
  starts with the **worst** case. Some algorithms have all three the same (selection sort,
  merge sort) and the ones that differ are where the interesting questions live.

---

## The six growth classes

| Class | Name | Where you meet it in this course | One-line reason |
|---|---|---|---|
| O(1) | constant | `len(lst)`, `lst[i]`, `lst.pop()`, `heap.peek()` | doesn't care how big n is |
| O(log n) | logarithmic | binary search, heap `insert` and `remove_min` | halve the problem each step |
| O(n) | linear | one loop over the data, linear search, `build_heap` | touch each item once |
| O(n log n) | linearithmic | merge sort, heap sort, quick sort (average) | n items, log n levels of work |
| O(n²) | quadratic | selection, bubble and insertion sort; nested loops over n | every item against every item |
| O(2ⁿ) | exponential | named for contrast; nothing in this course is this | unusable past tiny n |

**The two laws, in one line each.** Sequential code **adds**: O(n) then O(n) is O(n).
Nested code **multiplies**: a loop of n inside a loop of n is O(n²). Then drop constants
and lower-order terms. (Deck 3 s18–s19, s25–s27.)

---

## Reading the shape off a loop

This is the mechanical skill the written exam tests, so it is worth having as a reflex:

| What you see | Cost | Why |
|---|---|---|
| `return values[0]` | O(1) | one indexing operation, whatever the length |
| one loop over the whole list | O(n) | one pass, n iterations |
| two loops, one after the other | O(n) | the add law — O(n) + O(n) |
| a loop inside a loop, both over n | O(n²) | the multiply law |
| an inner loop starting at `i + 1` | O(n²) | n(n−1)/2 iterations, which is still O(n²) |
| `while n > 1: n = n // 2` | O(log n) | the range halves each step |
| one loop containing a binary search | O(n log n) | n iterations times log n each |

The one that catches people is row three against row four. Two loops **side by side** are
O(n); two loops **nested** are O(n²). The difference on the page is one level of
indentation.

---

## The two derivations the slides actually do

### n(n−1)/2 — selection sort's comparison count

The first pass compares the candidate against n−1 items, the next against n−2, and so on
down to 1. The total is (n−1) + (n−2) + … + 1 = **n(n−1)/2**, which is O(n²).

It does not depend on the data **at all**, which is why a sorted input costs exactly as
much as a reversed one. (Deck 3 s10–s12.)

### Why binary search is O(log n)

Each comparison throws away **half** the remaining range. Starting from n items, the
number of halvings needed to get down to one is log₂ n. On a million items that is about
**20** comparisons, against a million for linear search — and on a billion it is about 30,
because each extra comparison doubles the number of items you can handle.
(Deck 3 s28–s32.)

---

## How the slides put it

| | |
|---|---|
| "Count operations as a function of input size n, where n is the length of the list." | Deck 3 s9 |
| "Big-O compares shapes, not exact stopwatch times." | Deck 3 s16 |
| "Big-O gives an upper bound on how fast the work grows." | Deck 3 s17 |
| "For this class, we usually begin with worst-case Big-O." | Deck 3 s14 |
| "A linear algorithm with a big constant can beat quadratic at first, but not forever." | Deck 3 s22 |

That last one is the "constants can fool us" table on s22, and it is the sentence that
answers almost every objection to Big-O.

---

## Where people go wrong

- Calling sequential loops O(n²). Two loops one *after* the other add: O(n).
- Writing O(2n) or O(n² + n) as a final answer. Simplify.
- Saying an O(n²) algorithm is "slow" full stop. It is slow **as n grows**; at n = 10 it
  may well win.
- Forgetting that the inner loop's trip count can depend on the outer variable. If it
  shrinks each pass you are in n(n−1)/2 territory, not n² exactly — though both are O(n²).
- Giving a bare `O(...)` with no justification. A cost you can state but not justify is
  half an understanding. "O(n) **because every remaining element shifts left**" is the
  whole of it.
- Treating worst case and average case as the same question, or quoting a best case when
  the question asked for a worst case.

---

## Checklist

- [ ] Counting operations; why not a stopwatch — Deck 3 s6–s9
- [ ] The six growth classes, in order — Deck 3 s20–s21
- [ ] Dropping constants and lower-order terms — Deck 3 s18–s19
- [ ] Add law (sequential) versus multiply law (nested) — Deck 3 s25–s27
- [ ] n(n−1)/2 and where it comes from — Deck 3 s12
- [ ] Why halving gives O(log n) — Deck 3 s28–s32
- [ ] Best, average and worst case as three distinct questions — Deck 3 s14

---

## Next

- Work [mock.md](mock.md) with this page closed, then check yourself against
  [solutions.md](solutions.md).
- Write the code: `practice/p2_search.py`, checked by `python test_p2_search.py`. The two
  counting functions in it turn O(log n) from a phrase into a number you can look at —
  run `binary_search_count` on a thousand items and then on a million and watch the
  comparison count go up by ten.
- Then read [Topic 3](../3-arrays/review.md), which is where this vocabulary first earns
  its keep.
