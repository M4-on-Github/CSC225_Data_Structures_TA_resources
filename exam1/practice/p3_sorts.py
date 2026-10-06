# PROBLEM 3 -- Topic 4: sorting
#
# Check your work:   python test_p3_sorts.py
# Reference answer:  solutions/p3_sorts.py  (try first; consult one section if stuck)
#
# ---------------------------------------------------------------------------
# All five sorts, the way the lecture writes them. Sorting is the largest topic in this
# package, and this is the problem to do first if you only do one.
#
# THE RULES:
#   - each of the five sorts takes a parameter named "values" and RETURNS a sorted list
#   - no sort(), no sorted(), no imports -- that is the course rule, not a stylistic one
#
# THE RETURN CONVENTIONS, which differ per sort and ARE tested:
#   - selection, bubble, insertion   sort IN PLACE and return THE SAME LIST OBJECT
#   - merge, quick                   leave the argument untouched and return A NEW LIST
#                                    for inputs of two or more items; the base case may
#                                    return the original empty or one-item list
#   The tests check this with assertIs / assertIsNot, so "it sorted correctly" is not
#   enough to pass. This is the distinction students most often lose marks on.
#
# WHAT EACH ONE DOES:
#
#   selection_sort(values)
#       Find the smallest item in the unsorted part, swap it into place, repeat.
#       Use the tuple swap:  a[i], a[j] = a[j], a[i]
#
#   bubble_sort(values)
#       Repeatedly sweep, swapping neighbours that are out of order. Use the three-line
#       temp swap, and keep a "swapped" flag so a pass with no swaps breaks out early.
#       That flag is the only reason bubble sort has an O(n) best case.
#
#   insertion_sort(values)
#       Take each item in turn and shift the bigger items to its left one place right,
#       then drop it into the gap. Use a while loop, not a swap loop.
#
#   merge_sort(values)
#       Split in half, sort each half recursively, then merge. Compare the two halves
#       with "<=" and not "<" -- on a tie the LEFT item must go first, which is what
#       makes merge sort stable.
#
#   quick_sort(values)
#       Take the pivot as values[-1] (the LAST item -- that is the lecture's choice, and
#       the mock's worst-case question depends on it). Split into three lists: items
#       less than the pivot, items equal to it, items greater. Recurse on the outer two
#       and concatenate. The three-way split is what stops duplicates from recursing
#       forever.
#
#   selection_sort_count(values)
#       The same selection sort, reporting its own work. Return a tuple:
#       (values, comparisons, swaps). Count one comparison per inner-loop test, and
#       only count a swap when min_index differs from the current starting index.
#
#       Then run it on a sorted list and on a reversed list of the same length. The
#       comparison counts come out IDENTICAL -- that is the result worth knowing, and
#       it is why even selection sort's best case takes O(n**2) comparisons.
#
#   bubble_sort_passes(values)
#       Return a list of snapshots: a copy of the list after each completed pass. Use
#       this to check the trace questions on paper. It should stop early on the same
#       pass that bubble_sort does.
# ---------------------------------------------------------------------------


def selection_sort(values):
    pass  # TODO


def bubble_sort(values):
    pass  # TODO


def insertion_sort(values):
    pass  # TODO


def merge_sort(values):
    pass  # TODO


def quick_sort(values):
    pass  # TODO


def selection_sort_count(values):
    pass  # TODO


def bubble_sort_passes(values):
    pass  # TODO
