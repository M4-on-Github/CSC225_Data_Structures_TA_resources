# Reference solution -- Problem 3. Topic 4 (sorting).
#
# All five sorts the way the lecture writes them. The conventions below are graded,
# so they are not negotiable style choices:
#   - every sort takes a parameter named "values" and RETURNS it
#   - selection, bubble and insertion sort IN PLACE and return the SAME list object
#   - merge and quick BUILD AND RETURN A NEW LIST, leaving the argument alone
#   - bubble uses the three-line temp swap and the "swapped" early exit (sorting s9)
#   - selection uses the tuple swap (efficiency s11)
#   - quick takes its pivot as values[-1] and does a three-way split (sorting s22)
#   - merge compares with "<=", which is what makes it stable (sorting s15)
#   - no sort(), no sorted(), no imports anywhere -- the course rule, sorting s8


def selection_sort(values):
    n = len(values)
    for start in range(n):
        min_index = start
        for j in range(start + 1, n):
            if values[j] < values[min_index]:
                min_index = j
        values[start], values[min_index] = values[min_index], values[start]
    return values


def bubble_sort(values):
    n = len(values)
    for pass_num in range(n - 1):
        swapped = False
        for i in range(n - 1 - pass_num):
            if values[i] > values[i + 1]:
                temp = values[i]
                values[i] = values[i + 1]
                values[i + 1] = temp
                swapped = True
        # The early exit. On an already-sorted list this breaks after one pass, which
        # is the only reason bubble sort has an O(n) best case.
        if not swapped:
            break
    return values


def insertion_sort(values):
    for i in range(1, len(values)):
        current = values[i]
        j = i - 1
        # Shift bigger items right to open a slot, then drop current into it.
        while j >= 0 and values[j] > current:
            values[j + 1] = values[j]
            j -= 1
        values[j + 1] = current
    return values


def merge_sort(values):
    if len(values) <= 1:
        return values

    mid = len(values) // 2
    left = merge_sort(values[:mid])
    right = merge_sort(values[mid:])

    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        # "<=" and not "<". On a tie the LEFT item goes first, which is what keeps
        # equal items in their original order -- the definition of a stable sort.
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


def quick_sort(values):
    if len(values) <= 1:
        return values

    pivot = values[-1]
    left = []
    middle = []
    right = []

    for item in values:
        if item < pivot:
            left.append(item)
        elif item == pivot:
            middle.append(item)
        else:
            right.append(item)

    return quick_sort(left) + middle + quick_sort(right)


def selection_sort_count(values):
    # Efficiency deck s36: the same sort, reporting its own work.
    #
    # Run it on a sorted list and on a reversed list of the same length. The comparison
    # count is IDENTICAL -- n(n-1)/2 either way, because the inner loop never stops
    # early. Only the swap count changes. That is the point of the exercise.
    n = len(values)
    comparisons = 0
    swaps = 0
    for start in range(n):
        min_index = start
        for j in range(start + 1, n):
            comparisons = comparisons + 1
            if values[j] < values[min_index]:
                min_index = j
        if min_index != start:
            values[start], values[min_index] = values[min_index], values[start]
            swaps = swaps + 1
    return values, comparisons, swaps


def bubble_sort_passes(values):
    # Returns a list of snapshots: the state of the list after each completed pass.
    # This is the function to run when a trace question says "write the list after
    # each pass" and you want to check your paper answer.
    n = len(values)
    passes = []
    for pass_num in range(n - 1):
        swapped = False
        for i in range(n - 1 - pass_num):
            if values[i] > values[i + 1]:
                temp = values[i]
                values[i] = values[i + 1]
                values[i + 1] = temp
                swapped = True
        passes.append(list(values))
        if not swapped:
            break
    return passes
