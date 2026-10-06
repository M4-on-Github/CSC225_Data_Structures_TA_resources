# Topic 2 — mock test: Big-O and counting operations

Part 1 is five quick drills, Part 2 is five exam-style questions.

**Try each question before opening [solutions.md](solutions.md).** If stuck, read one relevant explanation, close it, and retry. You may type or write your answers.

No time limit is printed here on purpose. Work until you are done, note how long it took,
and compare that with however long you get in the real exam.

**Throughout:** give the Big-O **and one line of justification**. A bare `O(...)` with no
reason is only half an answer — the reasoning is the part worth practising.
Use worst-case costs unless another case is requested. Assume individual arithmetic,
comparison and output operations take constant time.

---

## Part 1 — Drills

**2.1** Why does the course count *operations* instead of timing the program with a
stopwatch?

**2.2** Name the six growth classes this course uses, in order, with one example of each.

**2.3** Why is O(n²) + O(n) just O(n²)? And why is O(3n²) just O(n²)?

**2.4** Give the Big-O of each: (i) `return L[0]` · (ii) one loop over `L` · (iii) two
loops one after the other · (iv) a loop inside a loop · (v) halving the search range each
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
worst case as a formula in n, the Big-O that follows from it, and the **best** case with
an input that produces it.

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
In each snippet, `values` holds n items, with n ≥ 1; `sorted_other_list` also holds n
items. Give the Big-O of each **and the law or rule that decides it**.

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
for value in values:
    found = binary_search(sorted_other_list, value)
```

### Q4 — Where n(n−1)/2 comes from
Selection sort performs exactly **n(n−1)/2** comparisons.

**(a)** Show where n(n−1)/2 comes from. Write the sum, not just the closed form.

**(b)** How many comparisons on a list of **8 items that is already sorted**?

**(c)** Is n(n−1)/2 the same Big-O as n²? Justify it in one sentence.

### Q5 — Halving, and what Big-O is claiming
**(a)** Linear search and binary search on **1,000,000** sorted items: give the
worst-case number of comparisons for each, roughly, and the Big-O of each.
Count one comparison per item examined, as the practice counters do.

**(b)** Using the practice implementation of `binary_search_count`, you search for `-1`
in `list(range(1000))` and it reports 9 comparisons. Predict roughly what it reports
when you search for `-1` in `list(range(1000000))` **before** reading on, then explain in
one sentence why a thousand times more data costs so little more.

**(c)** Your friend's program sorts 20 items and finishes instantly, so they conclude
their O(n²) sort is fine and ship it. Six months later the list holds 20,000 items and the
program takes minutes. Explain what happened in the language of this topic, and say what
Big-O was and was not claiming in the first place.

---

## Part 3 — Write the code

This topic's practice problem is `practice/p2_search.py`, checked by
`python -m unittest discover -s . -p "test_p2_search.py" -v` from the `practice/` folder. It shares a file with Topic 3
because the two searches are the cheapest place to watch O(n) and O(log n) side by side —
the two counting functions in it make Q5 something you can measure rather than recite.
