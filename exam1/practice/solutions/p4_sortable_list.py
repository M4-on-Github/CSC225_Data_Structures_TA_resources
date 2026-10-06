# Reference solution -- Problem 4. Topic 4 (sorting), in class form.
#
# A coding question on this material is most likely to be set as a class, since that is
# the part of the prerequisite course people struggle with most. Problem 3 is the
# algorithms; this is the same material in that shape.
#
# The asymmetry below IS the lesson, not an inconsistency:
#   - selection / bubble / insertion are written out as real methods. They sort
#     self.values in place, so they need no second list.
#   - merge / quick recurse on SUBLISTS, which are plain lists and not SortableLists.
#     Writing them as self-recursive methods would construct a new object per recursive
#     call for no reason. So the method owns the data and calls the module-level function
#     to do the algorithm. That division is the thing worth copying.

from p3_sorts import merge_sort, quick_sort


class SortableList:

    def __init__(self, values):
        # A COPY, not the caller's list. Two SortableLists built from one list should not
        # fight over it. This is the mutable-argument trap from Topic 1 in another coat.
        self.values = list(values)

    def size(self):
        return len(self.values)

    def is_sorted(self):
        for i in range(1, len(self.values)):
            if self.values[i - 1] > self.values[i]:
                return False
        return True

    def selection_sort(self):
        n = len(self.values)
        for start in range(n):
            min_index = start
            for j in range(start + 1, n):
                if self.values[j] < self.values[min_index]:
                    min_index = j
            self.values[start], self.values[min_index] = \
                self.values[min_index], self.values[start]
        return self.values

    def bubble_sort(self):
        n = len(self.values)
        for pass_num in range(n - 1):
            swapped = False
            for i in range(n - 1 - pass_num):
                if self.values[i] > self.values[i + 1]:
                    temp = self.values[i]
                    self.values[i] = self.values[i + 1]
                    self.values[i + 1] = temp
                    swapped = True
            if not swapped:
                break
        return self.values

    def insertion_sort(self):
        for i in range(1, len(self.values)):
            current = self.values[i]
            j = i - 1
            while j >= 0 and self.values[j] > current:
                self.values[j + 1] = self.values[j]
                j -= 1
            self.values[j + 1] = current
        return self.values

    def merge_sort(self):
        # The function returns a NEW list; the method's job is to adopt it.
        self.values = merge_sort(self.values)
        return self.values

    def quick_sort(self):
        self.values = quick_sort(self.values)
        return self.values
