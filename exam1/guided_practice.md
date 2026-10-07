# Guided practice

Try the blank steps before using [hints and worked answers](hints.md). Then close this page and attempt your topic's mock.

## 1 Python

`a = [2]`, then `b = a`. Both names point to one list.

After `b.append(5)`, a is ______. After `b = [8]`, a is ______.

Explain which line changed an object and which changed a name.

## 2 Complexity

An outer loop runs 3 times. Its inner loop runs 4 times on every outer iteration. It prints once each time.

Total prints: 3 times 4 = ______. If both loop lengths become n, the count is ______. If the two n-length loops run one after the other instead, the count is ______.

## 3 Arrays and search

A doubling array starts empty with capacity 1. After the first append, size = 1 and capacity = 1.

- After the second append: size ______, capacity ______, old items copied ______.
- After the third append: size ______, capacity ______, old items copied ______.

Insert `0` at the **front** of `[1, 3, 5]`. The new list is ______. How many old items shift right? ______. For n items, what is the worst-case cost? ______.

## 4 Sorting

Bubble sort starts with [3, 2, 1]. Compare the first pair: swap to get [2, 3, 1]. Compare the next pair: the list becomes ______. Which value is now in its final position?

For merge sort, follow calls down and returned results back up:

```text
merge_sort([3, 1, 2])
  left call:  [3] -> [3]          base case
  right call: [1, 2]
    split: [1] and [2]            both base cases
    merge returns: ______
  merge [3] with that result: ______
```

The base case returns without another recursive call. Each caller waits for its smaller calls to return before merging.

## 5 Heaps if included

A min-heap is [2, 5, 4]. Appending 1 gives [2, 5, 4, 1]. Its index is 3; its parent index is (3 - 1) // 2 = 1.

Swap with that parent: ______. Compare with the next parent and write the final heap: ______.

For ascending in-place heap sort, start from max-heap [3, 1, 2]. Swap the root with the final item: [2, 1, 3]. The active heap is now [2, 1]; the final 3 stays outside it. Does this active heap need a sift swap? ______. Move its root to its end: ______.
