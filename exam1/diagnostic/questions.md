# Exam 1 foundation check

Find what to review before you start. This is practice, not a grade or an exam prediction. There is no time limit.

Try questions 1 to 12 without notes. Type or write your answers. For every answer, mark confidence as sure, unsure, or guessed. Use “not sure” whenever needed. Then open the separate answer guide.

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

An outer loop runs n times. For each outer iteration, an inner loop runs n times and does constant work per iteration. What is the tightest growth class?

A. O(1)
B. O(n)
C. O(n squared)
D. O(log n)

Answer: ______  Confidence: ______

### 7 Dynamic array append

A dynamic array doubles its capacity when full. Which statement is correct?

A. Every append takes constant time.
B. One append can take O(n); n appends from empty take O(n) total.
C. Every append copies all existing items.
D. Appending at the end takes O(log n).

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

Why does bubble sort with an early-exit flag take O(n) on already-sorted input?

A. It makes no comparisons.
B. It halves the list on every pass.
C. One pass makes no swaps, so it stops.
D. All sorting algorithms take O(n) on sorted input.

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

## Optional heap check

Skip questions 13 and 14 unless your instructor includes heaps. They do not affect your core review route.

### 13 Heap order

Must a min-heap's underlying list be fully sorted?

Answer: Yes / No / Not sure. Confidence: ______

Reason: _________________________________________________

### 14 Heap insertion

After appending an item to a min-heap, which action restores its order?

A. Sift up toward the parent.
B. Sort the entire list.
C. Swap with the root every time.
D. Always leave it in place.

Answer: ______  Confidence: ______

Next: open [the answer guide](answers.md). Choose one review area to start with.
