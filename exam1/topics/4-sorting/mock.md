# Topic 4 — mock test: sorting

Part 1 is ten drills, Part 2 is nine exam-style questions. This is the
longest paper in the package, with particular emphasis on writing and tracing code.

**Try each question before opening [solutions.md](solutions.md).** If stuck, read one relevant explanation, close it, and retry. You may type or write your answers.

No time limit is printed here on purpose. Work until you are done, note how long it took,
and compare that with however long you get in the real exam.

**Throughout:** use the **lecture versions** of the sorts. Quick sort takes its pivot as
`values[-1]` and splits three ways; bubble sort has the `swapped` early exit; insertion
sort's outer loop starts at 1. **No `sort()`, no `sorted()`, no imports** anywhere you
write code.

---

## Part 1 — Drills

**4.1** Derive it: an outer loop runs `i` from 0 to n−1, and the inner loop runs from `i+1`
to n−1. How many inner iterations in total, and what Big-O is that?

**4.2** One pass of bubble sort on `[5, 1, 4, 2, 8]`. Write the list after the pass and say
how many swaps happened.

**4.3** What does the `swapped` flag buy you, and which case does it change?

**4.4** Selection sort on `[5, 2, 9, 1]`: what does one pass do, and how many comparisons
does the whole sort make?

**4.5** Merge sort on `[8, 3, 5, 1]`. Show the split-down and the merge-up.

**4.6** Why is merge sort O(n log n) — what do the `n` and the `log n` each count?

**4.7** Quick sort partitions `[7, 2, 9, 1, 5, 4, 6]` with the pivot the lecture version picks. Name
the pivot and write the three groups.

**4.8** Quick sort is O(n log n) on average but O(n²) in the worst case. What input causes
the worst case for *that* pivot choice, and why?

**4.9** Fill in the summary table from memory — best / average / worst for all five sorts.
For quick sort, distinguish all-equal input from input with distinct values.

| Sort | Best | Average | Worst |
|---|---|---|---|
| Selection | | | |
| Bubble | | | |
| Insertion | | | |
| Merge | | | |
| Quick | | | |

**4.10** Which of the five build a new list, and which sort in place? Note any base-case
exceptions, and explain why the return convention matters.

---

## Part 2 — Exam-style questions

### Q1 — Sorting vocabulary
**(a)** Define **in place** and **stable**, one sentence each.

**(b)** Name one of the five sorts that is stable but **not** O(n log n) in the worst
case.

### Q2 — Best cases
**(a)** Bubble sort's best case is O(n). What one feature gives it that, and why does
selection sort not have it?

**(b)** You run a counting selection sort on ten distinct items in sorted order, and again on
the same ten items reversed. It counts comparisons and swaps between different positions.
One of the two counts it reports is identical both times and
one is not. Which is which, and why?

### Q3 — Where the growth rates come from
**(a)** Quick sort averages O(n log n) but is O(n²) in the worst case. Give a list of
five numbers that triggers the worst case, show what the first split produces, and say why
that shape costs O(n²).

**(b)** Merge sort is O(n log n) on **every** input. Where does the `log n` come from,
and where does the `n` come from?

**(c)** You have 10,000 items **already in sorted order**. Of bubble sort and merge
sort, which finishes first, and why?

### Q4 — Sorting by hand
**(a)** Bubble sort `[5, 1, 4, 2, 8]`. Write the whole list after each **complete
pass**, then say how many passes the loop runs before its early exit.

| Pass | List after the pass | Any swaps? |
|---|---|---|
| 1 | | |
| 2 | | |
| 3 | | |
| 4 | | |

**(b)** Merge sort `[8, 3, 5, 1, 7, 2]`. Draw the splitting on the way down and the
merging on the way back up.

### Q5 — Three more sorts by hand
**(a)** **Selection sort** `[29, 10, 14, 37, 13]`. Write the whole list after each of
the five passes, then give the total number of comparisons.

| Pass | List after the pass |
|---|---|
| 1 | |
| 2 | |
| 3 | |
| 4 | |
| 5 | |

**(b)** **Quick sort** `[6, 2, 8, 4, 10, 3]`, pivot `values[-1]`, three-way split.
Write the first partition as `left` / `middle` / `right`, then the two recursive calls it
makes.

**(c)** **Insertion sort** `[5, 2, 4, 1]`. Write the list after each iteration of the
outer loop.

| After i = | List |
|---|---|
| | |
| | |
| | |

### Q6 — Reading the code
Both sorts below are the versions written in lecture. What are the two lines of output, and
why do they differ?

```python
data = [3, 1, 2]
a = bubble_sort(data)
print(data, a is data)

data2 = [3, 1, 2]
b = merge_sort(data2)
print(data2, b is data2)
```

### Q7 — Two sorts out of a student's homework
Neither is the lecture version.

**(a)** This insertion sort is missing a guard in its `while` condition. Say what is missing, what happens when
you run it on `[5, 2, 4, 1, 3]`, and why `[1, 2, 3]` survives it.

```python
def insertion_sort(values):
    for i in range(1, len(values)):
        current = values[i]
        j = i - 1
        while values[j] > current:
            values[j + 1] = values[j]
            j -= 1
        values[j + 1] = current
    return values
```

**(b)** This bubble sort sorts correctly on every input. Something is still wrong with
it. What, and what does it cost? Give an input that shows it.

```python
def bubble_sort(values):
    n = len(values)
    swapped = False
    for pass_num in range(n - 1):
        for i in range(n - 1 - pass_num):
            if values[i] > values[i + 1]:
                values[i], values[i + 1] = values[i + 1], values[i]
                swapped = True
        if not swapped:
            break
    return values
```

### Q8 — Write a sort as a method
Complete `insertion_sort` so that it sorts `self.values` **in place** and **returns that
same list**. Then answer the two short questions below it.

```python
class SortableList:
    def __init__(self, values):
        self.values = values

    def insertion_sort(self):
        # your code here


# it must satisfy all of these
lst = SortableList([5, 2, 4, 1, 3])
assert lst.insertion_sort() == [1, 2, 3, 4, 5]
assert lst.insertion_sort() is lst.values      # in place
assert SortableList([]).insertion_sort() == []
assert SortableList([7]).insertion_sort() == [7]
assert SortableList([2, 2, 1]).insertion_sort() == [1, 2, 2]
```

**(a)** Write the method.

**(b)** Give its best case and worst case, and say what input produces the best case.

**(c)** Insertion sort is **stable**. In one sentence, what does that mean about
`[2, 2, 1]`?

### Q9 — Choosing a sort for a real list
**(a)** A registrar's file of 40,000 student records is **already sorted by ID**.
Twelve late registrations are appended at the end, and the file must be sorted again. Which
of the five sorts would you run, and which operation inside it decides the matter?

**(b)** A different list: **2 million items in random order**, and you may **not** hold
a second copy of it in memory. Of the five sorts, which can you use and what does it cost
you? Name the algorithm from [Topic 5](../5-heaps/review.md) that removes the trade-off.

---

## Part 3 — Write the code

This topic has two practice problems, and they are the centre of the package:

- `practice/p3_sorts.py` — all five sorts as module-level functions, checked by
  `python -m unittest discover -s . -p "test_p3_sorts.py" -v`. **If you only do one practice problem, do this one.**
- `practice/p4_sortable_list.py` — the same five as **methods on a class**, checked by
  `python -m unittest discover -s . -p "test_p4_sortable_list.py" -v`. Do it after problem 3; it imports from it.

Q8 above is the paper version of problem 4: one method, by hand, under exam conditions.
