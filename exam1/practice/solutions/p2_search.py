# Reference solution -- Problem 2. Topic 3 (arrays) and Topic 2 (Big-O).
#
# Both searches are Dr. Smith's, from the efficiency deck s28-s30. binary_search is
# given in full on s30 but was never set as a lab, which is why it is here.
#
# Conventions: the parameter is "values", a miss returns -1, no imports.


def linear_search(values, target):
    for i in range(len(values)):
        if values[i] == target:
            return i
    return -1


def binary_search(values, element):
    # REQUIRES a sorted list. On an unsorted list this returns a wrong answer rather
    # than an error, which is the trap worth remembering.
    low = 0
    high = len(values) - 1

    while low <= high:
        mid = (low + high) // 2
        if values[mid] == element:
            return mid
        elif values[mid] < element:
            low = mid + 1
        else:
            high = mid - 1

    return -1


def binary_search_count(values, element):
    # The same search, reporting how many comparisons it made. Run it on lists of
    # 1,000 and 1,000,000 items: the count goes up by 10, not by 1,000. That is what
    # O(log n) means in numbers rather than in words.
    low = 0
    high = len(values) - 1
    comparisons = 0

    while low <= high:
        mid = (low + high) // 2
        comparisons = comparisons + 1
        if values[mid] == element:
            return mid, comparisons
        elif values[mid] < element:
            low = mid + 1
        else:
            high = mid - 1

    return -1, comparisons


def linear_search_count(values, target):
    comparisons = 0
    for i in range(len(values)):
        comparisons = comparisons + 1
        if values[i] == target:
            return i, comparisons
    return -1, comparisons
