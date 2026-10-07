# Coding practice

Six starter files. Read the task at the top of a file, replace its `pass  # TODO` lines,
then run its tests. Failures are expected until your code works.

```sh
python -m unittest discover -s . -p "test_p*.py" -v
```

Run this from the repository root, `exam1`, `exam1/practice`, or the clone's parent
folder. Change the pattern to `test_p3_sorts.py` to test only problem 3. `OK` means the
provided tests passed; `Ran 0 tests` means none were found. See the [main test
guide](../../README.md#run-your-tests) if needed.

| Problem | Starter | Focus |
|---|---|---|
| 1 | [Bank account](p1_bank_account.py) | Classes and argument passing |
| 2 | [Search](p2_search.py) | Linear and binary search |
| 3 | [Sorting functions](p3_sorts.py) | Five sorts |
| 4 | [Sortable list](p4_sortable_list.py) | Sorts as methods |
| 5 | [Min-heap](p5_min_heap.py) | Heap operations and sorting |
| 6 | [Triage queue](p6_triage_queue.py) | Apply a heap |

Do 3 before 4 and finish `MinHeap` in 5 before 6. The [coding
checkpoints](../study_paths.md#coding-checkpoints) split longer tasks into stages.

Selection, bubble, and insertion sorts change and return the original list. Merge and
quick sort return a new list for inputs of at least two items; their empty and one-item
base cases may return the original. The tests check this behavior. Do not use `sort()`,
`sorted()`, or imports beyond those already supplied in a starter.

If stuck, inspect the relevant test, use a [hint](../hints.md), then retry. Reference
answers are linked from the [main README](../../README.md#coding-practice). To check the
reference implementations, run `python check.py --solutions` from this folder.

Confirm heap coverage with your instructor before prioritizing problems 5 and 6.
