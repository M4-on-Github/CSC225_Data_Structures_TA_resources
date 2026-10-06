# Exam 1 foundation check answer guide

Use this after attempting the questions. A wrong answer is a starting point for review. A correct guess also deserves a second look.

## Check your reasoning

Compare your answer and explanation. Mark any question you missed, guessed, or cannot explain. Do not use a total score to decide whether you are ready for the exam.

### 1 Yes

Both names refer to one list. Appending changes that shared object. A “No” answer suggests reviewing references and mutation.

### 2 No

The work adds: n + n = 2n, which grows linearly. Consecutive loops do not multiply their iteration counts.

### 3 No

Binary search discards a region based on sorted order. On an unsorted list it may miss a value that is present, even though some searches succeed by chance.

### 4 Yes

In place describes where sorting happens and how much extra space it uses. Returning the original list is a separate requirement of this package's in-place sorting exercises.

### 5 A

The output is [1, 2]. The addition creates a new list and the assignment changes only the local name items. B confuses rebinding with mutation; C confuses the caller's list with the new item; D assumes valid code raises an error.

### 6 C

The inner work repeats n times for each of n outer iterations: n times n. B counts only one loop; A ignores repetition; D would need a shrinking search range or similar behavior.

### 7 B

A full array must copy its items into larger storage. Doubling spreads that copying across many appends. A confuses amortized cost with a guarantee for each call; C ignores spare capacity; D confuses growth with binary search.

<!-- pagebreak -->

## Remaining answers

### 8 D

Size counts stored items; capacity counts available slots. A reverses the terms; B ignores unused slots; C counts unused slots as stored items.

### 9 B

Bo comes first because 1 is smaller than 2. Ada stays before Cy because equal keys keep their original order. A reverses that tie; C is not sorted; D treats stability as optional.

### 10 C

One pass makes n minus 1 comparisons and no swaps. The flag then stops the algorithm. A confuses swaps with comparisons; B describes halving; D incorrectly applies this behavior to every sort.

### 11 Output is 1 0

Each instance receives its own value attribute. Calling a.add() changes a.value only. An output of 1 1 suggests confusing separate instances with shared state.

### 12 Output is 3

The values after division are 4, 2, 1. Count the three divisions, not the four numbers including the starting 8. Repeated halving gives logarithmic growth.

### 13 No

A min-heap orders each parent before or equal to its children. Separate branches need not be in order. For example, [1, 3, 2] is a valid min-heap.

### 14 A

The appended item may be smaller than its parent. Swap upward while needed, stopping when the parent is smaller or equal or the item reaches the root. B does unnecessary work; C ignores intermediate parents; D can leave the heap property broken.

## Use the result

Start with the earliest area below that has a marked question. One mistake is a reason to investigate, not proof that the whole topic is weak.

- Questions 1, 5, 11: [Topic 1 Python](../topics/1-python-review/review.md). Then try mock Q2 and Q3.
- Questions 2, 6, 12: [Topic 2 complexity](../topics/2-big-o/review.md). Then try mock Q1 and Q3.
- Questions 3, 7, 8: [Topic 3 arrays and search](../topics/3-arrays/review.md). Then try mock Q1 and Q4.
- Questions 4, 9, 10: [Topic 4 sorting](../topics/4-sorting/review.md). Then try mock Q1, Q2 and Q4.
- Questions 13, 14: [Topic 5 heaps](../topics/5-heaps/review.md), if included. Then try mock Q1 and Q3.

The topic folders are inside exam1/topics. Their review.md files teach the material; mock.md contains the questions. Keep these documents with the folder so their links can work.

<!-- pagebreak -->

## Retry after reviewing

Close the review. Try the question for your area and explain your answer before checking below. Use a different example if you remember the answer without understanding it.

### Python

```python
items = [4]
other = items
other.append(7)
other = [9]
print(items)
```

Output and reason: _______________________________________

### Complexity

Start question 12 with n = 16. How many divisions occur? What changes if n doubles again?

Answer and reason: _______________________________________

### Arrays and search

An array has size 4 and capacity 4. It doubles when full. After appending one item, what are its size and capacity, and how many old items were copied?

Answer and reason: _______________________________________

### Sorting

Write the list after one left-to-right bubble-sort pass on [3, 1, 2]. Was a swap made? Can the early-exit flag stop after this pass?

Answer and reason: _______________________________________

### Optional heaps

Start with min-heap [2, 5, 4]. Append 1 and sift up. Write the resulting list.

Answer and reason: _______________________________________

## Check after trying

- Python: [4, 7]. Appending changes the shared list; rebinding other does not.
- Complexity: 4 divisions; doubling to 32 adds one division.
- Arrays: size 5, capacity 8, with 4 old items copied.
- Sorting: [1, 2, 3]. Swaps occurred, so the flag does not stop yet.
- Heaps: [1, 2, 4, 5]. The new item swaps with 5, then with 2.

If you can explain the retry, move to the matching coding task. If not, inspect one relevant hint or solution section, close it, and retry. Ask your TA with the exact step that confused you.

Finish with the [study paths](../study_paths.md) and [mixed readiness check](../mock_exam/questions.md).
