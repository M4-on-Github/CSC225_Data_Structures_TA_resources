# Mixed readiness check

Attempt without notes. There is no time limit or grade. Explain each answer; this is a small sample, not a prediction of exam coverage. Use [solutions](solutions.md) after trying.

## 1 Shared state

Predict both outputs and explain the difference:

```python
def update(values):
    values.append(6)
    values = [9]
a = [2]
b = list(a)
update(a)
print(a)
print(b)
```

## 2 Count the work

An algorithm runs two consecutive loops. The first makes n constant-time checks; the second makes n times n constant-time checks. Give the total count and its tightest Big-O class.

## 3 Choose a search

You need one search in an unsorted list. Would binary search directly on that list be reliable? Choose a suitable search and give its worst-case cost. Then state what binary search requires.

## 4 Choose and explain a sort

A list is already sorted, then one new small value is appended. Choose between the taught insertion sort and the taught merge sort. Explain how your choice handles that last value and why its work is O(n) for this input pattern.

## 5 Write a method

Write `is_sorted(self)` for a class storing numbers in `self.values`. Return True for non-decreasing order, including empty and one-item lists. Do not change the list or call a sorting function. State the worst-case cost.

## 6 Optional heaps

Start with min-heap [1, 3, 2, 7, 5]. Remove the minimum using the taught algorithm. Give the returned value and resulting heap. Explain why the last item moves to the root first.
