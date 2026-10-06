# PROBLEM 4 -- Topic 4: sorting, in class form
#
# Check your work:   python test_p4_sortable_list.py
# Reference answer:  solutions/p4_sortable_list.py  (try first; consult one section if stuck)
#
# Do Problem 3 first. This problem assumes p3_sorts.py works, because it imports from it.
#
# ---------------------------------------------------------------------------
# WHY THIS PROBLEM EXISTS. This combines the sorting algorithms with the class-writing
# skills from the prerequisite course. Problem 3 covers the algorithms. This problem
# puts the same algorithms into methods on a class.
#
# Write a SortableList class holding a list of numbers in self.values.
#
#   __init__(self, values)
#       Store a COPY: self.values = list(values). Not self.values = values.
#       If you store the caller's list directly, sorting this object silently reorders
#       their list too -- the mutable-argument trap from Topic 1 in a different coat.
#       There is a test for exactly this.
#
#   size(self)        how many items
#   is_sorted(self)   True if self.values is in non-decreasing order. An empty list and
#                     a one-item list both count as sorted.
#
#   selection_sort(self)
#   bubble_sort(self)
#   insertion_sort(self)
#       Write these out as real methods, operating on self.values directly. They sort in
#       place, so there is no second list anywhere. Each returns self.values.
#
#   merge_sort(self)
#   quick_sort(self)
#       Do NOT rewrite the recursion as methods. merge and quick recurse on SUBLISTS,
#       which are plain lists, not SortableLists -- a self-recursive version would build
#       a new object per recursive call for no reason.
#
#       Instead: call the module-level function from p3_sorts, and ADOPT the list it
#       returns:
#
#           self.values = merge_sort(self.values)
#
#       That assignment is the step students miss. For inputs of two or more items,
#       the function returns a new list and leaves the argument unchanged. Without the
#       assignment, the object keeps its old unsorted data and the method looks like
#       it did nothing.
#
#       The division of labour -- the method owns the data, the function owns the
#       algorithm -- is the part worth copying into your own code.
#
# Every one of the five methods returns self.values when it is done.
# ---------------------------------------------------------------------------

from p3_sorts import merge_sort, quick_sort


class SortableList:

    def __init__(self, values):
        pass  # TODO

    def size(self):
        pass  # TODO

    def is_sorted(self):
        pass  # TODO

    def selection_sort(self):
        pass  # TODO

    def bubble_sort(self):
        pass  # TODO

    def insertion_sort(self):
        pass  # TODO

    def merge_sort(self):
        pass  # TODO

    def quick_sort(self):
        pass  # TODO
