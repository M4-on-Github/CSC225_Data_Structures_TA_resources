# Exam 1 foundation check

Find what to review before you start. This four-page check is practice, not a grade or an exam prediction.

Try questions 1 to 13 without notes, including page 4. All efficiency questions ask for worst-case costs. Use pseudocode for sorting; Python syntax is not required there. Mark confidence as sure, unsure, or guessed. Aim for 22 minutes in class. Speed is not scored.

## Yes or no

### 1 Shared lists

Two names refer to the same list. One name is used to append an item. Does the other name see that item?

Answer: Yes / No / Not sure. Confidence: ______

Reason in a few words: ____________________________________

### 2 Consecutive loops

Two loops run one after the other. Each visits n items and does constant work per item. Is their total running time proportional to n squared?

Answer: Yes / No / Not sure. Confidence: ______

Reason in a few words: ____________________________________

### 3 Binary search

Can the binary search taught here reliably find a value in an unsorted list?

Answer: Yes / No / Not sure. Confidence: ______

Reason in a few words: ____________________________________

### 4 Sorting in place

A function rearranges the original list using constant extra space. Can it sort in place even if it returns None?

Answer: Yes / No / Not sure. Confidence: ______

Reason in a few words: ____________________________________

### 5 Rebinding a parameter

What prints? Choose one answer, or write “not sure”.

```python
def change(items):
    items = items + [3]
values = [1, 2]
change(values)
print(values)
```

A. [1, 2]
B. [1, 2, 3]
C. [3]
D. An error

Answer: ______  Confidence: ______

<!-- pagebreak -->

## Multiple choice

Choose one answer per question, or write “not sure”.

### 6 Nested loops

An outer loop runs n times. For each outer iteration, an inner loop runs n times and does constant work per iteration. What is its tightest worst-case Big-O cost?

A. O(1)
B. O(n)
C. O(n squared)
D. O(log n)

Answer: ______  Confidence: ______

### 7 Dynamic array append

A dynamic array doubles its capacity when full. With n items already stored, what is the worst-case cost of one append?

A. O(1)
B. O(n)
C. O(n squared)
D. O(log n)

Answer: ______  Confidence: ______

### 8 Size and capacity

A dynamic array stores 3 items in 8 reserved slots. What are its size and capacity?

A. Size 8, capacity 3
B. Size 3, capacity 3
C. Size 8, capacity 8
D. Size 3, capacity 8

Answer: ______  Confidence: ______

### 9 Stable sorting

Records (2, Ada), (1, Bo), (2, Cy) are sorted by number only. Which output preserves stability?

A. (1, Bo), (2, Cy), (2, Ada)
B. (1, Bo), (2, Ada), (2, Cy)
C. (2, Ada), (1, Bo), (2, Cy)
D. Either A or B

Answer: ______  Confidence: ______

### 10 Bubble sort

Trace this pseudocode on [4, 1, 3, 2]. What is the list after this single pass?

```text
FOR each adjacent pair, from left to right
    IF the left value is greater than the right value
        SWAP the two values
```

A. [1, 2, 3, 4]
B. [4, 1, 3, 2]
C. [1, 3, 2, 4]
D. [4, 3, 2, 1]

Answer: ______  Confidence: ______

<!-- pagebreak -->

## Short traces

Write the output and a short reason. You may write “not sure”.

### 11 Independent objects

```python
class Counter:
    def __init__(self):
        self.value = 0
    def add(self):
        self.value += 1
a = Counter()
b = Counter()
a.add()
print(a.value, b.value)
```

Output: ______  Confidence: ______

Reason: _________________________________________________

### 12 Halving

```python
n = 8
steps = 0
while n > 1:
    n = n // 2
    steps += 1
print(steps)
```

Output: ______  Confidence: ______

Values of n after each division: ___________________________

## Heap work on paper

### H1 Draw and update a heap

If heaps are included, draw the binary tree stored by this min-heap list: [2, 5, 3, 9, 7, 8, 4]. Put one value at each node. Otherwise, continue to question 13 on the next page.

Use the space below for your drawing. You may instead describe the levels and parent-child links in text.

________________________________________________________

________________________________________________________

________________________________________________________

Now remove the minimum. Show the last item moving to the root, then each sift-down swap. Use arrows on your drawing or write the intermediate lists.

Steps: __________________________________________________

________________________________________________________

Returned value: ______  Final list: __________________________

Confidence: ______

<!-- pagebreak -->

## Sorting costs and reasoning

### 13 Derive the running time

Fill in the tightest worst-case Big-O cost and give a short derivation for each sort. Use n for the number of items. Comparisons and moves take constant time. Assume distinct keys.

Use the taught versions: bubble sort may stop after a pass with no swaps; merge sort splits and merges; quick sort uses the last item as pivot and builds three lists. Write “not sure” when needed.

| Algorithm | Worst case | Derivation or repeated work |
|---|---|---|
| Selection | ______ | __________________________ |
| Bubble | ______ | __________________________ |
| Insertion | ______ | __________________________ |
| Merge | ______ | __________________________ |
| Quick | ______ | __________________________ |

## Explain one sort in pseudocode

Choose one algorithm from the table. Write its steps in plain-language pseudocode, using indentation for loops or decisions. Do not write Python code. Then connect those steps to its worst-case cost.

Chosen algorithm: __________________  Confidence: ______

________________________________________________________

________________________________________________________

________________________________________________________

________________________________________________________

________________________________________________________

An input pattern that reaches its worst case: __________________

Why the steps above give that cost: __________________________

________________________________________________________

Next: open [the answer guide](answers.md) when your TA asks. Review a flagged concept, then try a fresh question without notes.
