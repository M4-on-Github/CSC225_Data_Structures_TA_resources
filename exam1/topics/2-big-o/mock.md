# Topic 2 — mock test: Big-O and counting operations

Try the drills and questions before opening [solutions](solutions.md). Work at your own pace.

**Throughout:** give each Big-O cost with one sentence of reasoning.
Use worst-case costs unless another case is requested. Assume individual arithmetic,
comparison and output operations take constant time.

---

## Part 1 — Drills

**2.1** Why does the course count *operations* instead of timing the program with a
stopwatch?

**2.2** Name the six growth classes this course uses, in order, with one example of each.

**2.3** Why is O(n²) + O(n) just O(n²)? And why is O(3n²) just O(n²)?

**2.4** Give the Big-O of each: (i) `return L[0]` · (ii) one loop over `L` · (iii) two
loops one after the other · (iv) a loop inside a loop · (v) halving a number each
step. In (ii)–(iv), each loop traverses all n items of `L`, and the innermost body takes
constant time.

**2.5** A friend says "my algorithm is O(n²) but it ran fast, so Big-O is wrong." Answer
them.

---

## Part 2 — Exam-style questions

### Q1 — Counting operations
For (a) and (b), `values` holds n items. For (c), n is a positive integer.

```python
def total(values):                      # (a)
    running = 0
    for value in values:
        running = running + value
    return running


def any_duplicate(values):              # (b)
    for i in range(len(values)):
        for j in range(i + 1, len(values)):
            if values[i] == values[j]:
                return True
    return False


def halvings(n):                        # (c)
    count = 0
    while n > 1:
        n = n // 2
        count = count + 1
    return count
```

**(a)** How many additions does `total` perform, exactly, and what is its Big-O?

**(b)** For `any_duplicate`, give the **exact** number of `==` comparisons in the
worst case as a formula in n, the Big-O that follows from it, and an input that
reaches that case.

**(c)** What is `halvings`' Big-O, and what does it return for `n = 1000`?

### Q2 — Simplifying
**(a)** Give the Big-O of each expression.

| Operation count | Big-O |
|---|---|
| 3n² + 7n + 2 | |
| 100n + 5000 | |
| n/2 | |
| n(n−1)/2 | |

**(b)** Put these four in order, slowest-growing first: O(n log n), O(1), O(n²),
O(log n).

**(c)** An algorithm performs exactly 1,000,000 operations regardless of the size of
its input. What is its Big-O, and is it a fast algorithm?

### Q3 — The two laws
In each snippet, `values` holds n items, with n ≥ 1. Give the Big-O of each
**and the law or rule that decides it**.

```python
# (a)
for value in values:
    print(value)
for value in values:
    print(value)

# (b)
for a in values:
    for b in values:
        print(a, b)

# (c)
print(values[0])
print(len(values))

# (d)
for _ in values:
    width = len(values)
    while width > 1:
        width = width // 2
```

### Q4 — Where n(n−1)/2 comes from
Selection sort performs exactly **n(n−1)/2** comparisons.

**(a)** Show where n(n−1)/2 comes from. Write the sum, not just the closed form.

**(b)** How many comparisons on a list of **8 items that is already sorted**?

**(c)** Is n(n−1)/2 the same Big-O as n²? Justify it in one sentence.

### Q5 — Halving, and what Big-O is claiming
**(a)** Compare one loop over **1,000,000** items with repeatedly halving
`n = 1,000,000` until it reaches 1. Roughly how many iterations does each take,
and what is each Big-O?

**(b)** `halvings(1000)` from Q1(c) returns 9. Predict `halvings(1000000)`
before calculating it. Why does a thousand times larger `n` add only about ten steps?

**(c)** Your friend's program sorts 20 items and finishes instantly, so they conclude
their O(n²) sort is fine and ship it. Six months later the list holds 20,000 items and the
program takes minutes. Explain what happened in the language of this topic, and say what
Big-O was and was not claiming in the first place.

---

## Part 3 — Write the code

Use [Problem 2](../../practice/p2_search.py) to count the comparisons made by a
linear scan. See the [test instructions](../../../README.md#run-your-tests).
