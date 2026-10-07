# Mixed readiness check

Attempt without notes and explain each answer. Check [solutions](solutions.md) after trying.

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

## 2 Analyze the loops

What is the **tightest worst-case Big-O** in terms of `n = len(values)`? Explain
how many times the inner loop can run for each `i`, and give an input that reaches
the worst case.

```python
def nearby_duplicate(values):
    n = len(values)
    for i in range(n):
        for j in range(i + 1, min(i + 4, n)):
            if values[i] == values[j]:
                return True
    return False
```

## 3 Choose and explain a sort

You must sort an arbitrary list of n values and need a worst-case O(n log n) time guarantee. Choose between the taught insertion sort and merge sort. Give each sort's worst-case time and the extra space merge sort uses.

## 4 Write a method

Write `is_sorted(self)` for a class storing numbers in `self.values`. Return True for non-decreasing order, including empty and one-item lists. Do not change the list or call a sorting function. State the worst-case cost.

## 5 Optional heaps

Start with min-heap [1, 3, 2, 7, 5]. Remove the minimum using the taught algorithm. Give the returned value and resulting heap. Explain why the last item moves to the root first.
