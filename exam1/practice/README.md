# CSC130 Exam 1 -- practice coding problems

Six problems. You write the code, then you run a test file and it tells you whether you
got it right -- no answer key to read off, and nobody has to be in the room.

## How to use this folder

1. Open a problem file, e.g. `p1_bank_account.py`. The comment header at the top is the
   whole problem statement. The function and method bodies say `pass  # TODO`.
2. Replace each `pass  # TODO` with your code.
3. Run its test file from this folder:

   ```
   python test_p1_bank_account.py
   ```

   You will see one line per test and a count at the end. `OK` means you are done.
   A failure names the test that failed and what it expected.
4. **Only then** open `solutions/p1_bank_account.py` and compare. Reading the answer
   before you have attempted it feels like learning and is not; the tests exist so you
   can get unstuck without doing that.

To see where you stand across all six:

```
python check.py          one line per problem
python check.py 3        just problem 3
python check.py -v 3     problem 3, with the full test output
```

Nothing here needs installing. Python 3 and these files are the whole toolchain.

## The six problems

| | File | Topic | What it is |
|---|---|---|---|
| 1 | `p1_bank_account.py` | 1 -- Python review | A class with a private balance, plus the four argument-passing functions |
| 2 | `p2_search.py` | 3 and 2 -- arrays, Big-O | Linear and binary search, then the same two counting their own comparisons |
| 3 | `p3_sorts.py` | 4 -- sorting | All five sorts, in the lecture's style and with its return conventions |
| 4 | `p4_sortable_list.py` | 4 -- sorting | The same five sorts as methods on a class |
| 5 | `p5_min_heap.py` | 5 -- heaps | Index arithmetic, `MinHeap`, `build_heap`, both heap sorts |
| 6 | `p6_triage_queue.py` | 5 -- heaps | Using a heap to run an emergency room |

**Order matters in two places.** Problem 4 imports from problem 3, and problem 6 imports
from problem 5, so do 3 before 4 and 5 before 6. Otherwise the six are independent.

**If you only have time for one, do problem 3.** Sorting is the heaviest topic on the
exam. If you have time for two, add problem 4 -- Dr. Smith's own note says a coding
question would most likely involve a class.

## Two things the tests check that you might not expect

**The return conventions.** Selection, bubble and insertion sort in place and return
*the same list object*; merge and quick sort return a *new* list and leave the argument
alone. The tests check this with `assertIs` and `assertIsNot`, so a correctly sorted
result can still fail. That distinction is the one people most often get wrong,
which is exactly why it is tested.

**No `sort()`, no `sorted()`, no imports** in your answers. That is the course rule, not
a style preference. The one exception is the two files that import from an earlier
problem, where the import is already written for you.

## A warning about problems 5 and 6

**There is no heap lecture deck in this course.** The entire slide record for heaps is
three slides at the end of the stacks and queues deck -- the heap property and three
costs -- and they point at a lecture whose deck we do not have. Everything else in
problems 5 and 6 was written by your TA to fill that gap.

So **confirm with Dr. Smith that heaps are on the exam** before spending an evening
here. If he says yes, this is good preparation. If he says no, do problems 1 to 4 twice
instead.

## If a reference answer is wrong

`python check.py --solutions` runs all 122 tests against the files in `solutions/`.
It should report six passes. If it ever does not, the reference answer is wrong rather
than you -- tell your TA.
