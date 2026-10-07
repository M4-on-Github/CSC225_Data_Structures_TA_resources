# Reference solution -- Problem 2: linear search and operation counts.


def linear_search(values, target):
    for i in range(len(values)):
        if values[i] == target:
            return i
    return -1


def linear_search_count(values, target):
    comparisons = 0
    for i in range(len(values)):
        comparisons += 1
        if values[i] == target:
            return i, comparisons
    return -1, comparisons
