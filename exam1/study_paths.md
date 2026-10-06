# Choose a study path

Use the [foundation check](diagnostic/questions.md) first. Start with the earliest area you missed, guessed, or could not explain.

## Short review

1. Read only the relevant topic's review section.
2. Try its exercise in [guided practice](guided_practice.md).
3. Close the notes and try that area's retry in the [answer guide](diagnostic/answers.md#retry-after-reviewing).
4. If you can explain the retry, attempt the topic mock questions listed below. Otherwise, use one hint and retry before moving on.

## Full preparation

Follow the rows in order. Each topic folder has review.md, mock.md and solutions.md. Attempt a question before consulting its solution; help is available whenever you get stuck.

| Area | Read and practise | Independent check | Coding |
|---|---|---|---|
| Python | [Review](topics/1-python-review/review.md), then guided exercise 1 | [Mock Q2 and Q3](topics/1-python-review/mock.md#q2--code-reading) | Problem 1 |
| Complexity | [Review](topics/2-big-o/review.md), then guided exercise 2 | [Mock Q1 and Q3](topics/2-big-o/mock.md#q1--counting-operations) | Wait until you have read search in Topic 3 |
| Arrays and search | [Review](topics/3-arrays/review.md), then guided exercise 3 | [Mock Q1 and Q4](topics/3-arrays/mock.md#q1--amortized-append) | Problem 2 |
| Sorting | [Review](topics/4-sorting/review.md), then guided exercise 4 | [Mock Q1, Q2 and Q4](topics/4-sorting/mock.md#q1--sorting-vocabulary) | Problem 3, then 4 |
| Heaps if included | [Review](topics/5-heaps/review.md), then guided exercise 5 | [Mock Q1 and Q3](topics/5-heaps/mock.md#q1--min-heaps) | Problem 5 in stages; problem 6 after MinHeap works |

For sorting, learn selection, bubble and insertion first. Before merge and quick, trace a list splitting into smaller lists until each has at most one item. Then follow how the returned results combine. Use the [guided merge trace](guided_practice.md#4-sorting) before writing recursive code.

## Coding checkpoints

Work from the practice folder. Keep the starter filenames so the tests can find them.

- Problem 1: constructor and balance methods, then transfer and argument passing.
- Problem 2: linear search, binary search, then counting versions.
- Problem 3: selection, bubble, insertion, then merge and quick; finish the counting and snapshot helpers.
- Problem 4: constructor and checks, then sorting methods.
- Problem 5: run the test groups below as you build each part.

```sh
python -m unittest test_p5_min_heap.TestIndexArithmetic
python -m unittest test_p5_min_heap.TestEmptyHeap test_p5_min_heap.TestInsert
python -m unittest test_p5_min_heap.TestRemoveMin
```

Once these pass, you can try problem 6. Then return to the heap construction and sorting extensions:

```sh
python -m unittest test_p5_min_heap.TestBuildHeap
python -m unittest test_p5_min_heap.TestHeapSort
```

## Ready to practise independently

Try the [mixed readiness check](mock_exam/questions.md) without notes. For each missed area, review one explanation and solve a fresh variation. Continue when you can explain the result, trace it, and implement the matching task. Passing this small check does not guarantee coverage of the whole exam.
