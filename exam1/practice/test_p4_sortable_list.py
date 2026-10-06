# Tests for Problem 4. Run from this folder:
#
#     python test_p4_sortable_list.py
#
# Problem 3 was the algorithms. This is the same algorithms in the likelier exam form:
# methods on a class, operating on self.values.

import unittest

from p4_sortable_list import SortableList

METHOD_NAMES = ["selection_sort", "bubble_sort", "insertion_sort",
                "merge_sort", "quick_sort"]

CASES = [
    [],
    [1],
    [2, 1],
    [5, 3, 8, 1, 9, 2, 8],
    [1, 2, 3, 4, 5],
    [5, 4, 3, 2, 1],
    [7, 7, 7],
    [4, -2, 0, 11, -2],
]


class TestConstructor(unittest.TestCase):

    def test_values_are_stored(self):
        sl = SortableList([3, 1, 2])
        self.assertEqual(sl.values, [3, 1, 2])

    def test_constructor_copies_the_caller_list(self):
        # Topic 1's mutable-argument lesson, wearing a different coat. If __init__ does
        # self.values = values instead of list(values), sorting the object silently
        # reorders the caller's list too.
        original = [3, 1, 2]
        sl = SortableList(original)
        sl.selection_sort()
        self.assertEqual(original, [3, 1, 2],
                         "__init__ should copy: self.values = list(values)")

    def test_two_objects_from_one_list_are_independent(self):
        original = [3, 1, 2]
        a = SortableList(original)
        b = SortableList(original)
        a.bubble_sort()
        self.assertEqual(b.values, [3, 1, 2])


class TestSizeAndIsSorted(unittest.TestCase):

    def test_size(self):
        self.assertEqual(SortableList([1, 2, 3]).size(), 3)
        self.assertEqual(SortableList([]).size(), 0)

    def test_is_sorted_true(self):
        self.assertTrue(SortableList([1, 2, 2, 3]).is_sorted())

    def test_is_sorted_false(self):
        self.assertFalse(SortableList([1, 3, 2]).is_sorted())

    def test_empty_and_single_count_as_sorted(self):
        self.assertTrue(SortableList([]).is_sorted())
        self.assertTrue(SortableList([9]).is_sorted())


class TestEveryMethodSorts(unittest.TestCase):

    def test_all_five_on_all_cases(self):
        for name in METHOD_NAMES:
            for case in CASES:
                with self.subTest(method=name, case=case):
                    sl = SortableList(case)
                    getattr(sl, name)()
                    self.assertEqual(sl.values, sorted(case),
                                     name + " should leave self.values sorted")

    def test_every_method_returns_self_values(self):
        # Each method returns the sorted list as well as storing it, so a caller can
        # use the result directly.
        for name in METHOD_NAMES:
            with self.subTest(method=name):
                sl = SortableList([4, 2, 7, 1])
                result = getattr(sl, name)()
                self.assertEqual(result, [1, 2, 4, 7])
                self.assertIs(result, sl.values,
                              name + " should return self.values")

    def test_is_sorted_agrees_after_each_method(self):
        for name in METHOD_NAMES:
            with self.subTest(method=name):
                sl = SortableList([9, 3, 7, 1, 8])
                self.assertFalse(sl.is_sorted())
                getattr(sl, name)()
                self.assertTrue(sl.is_sorted())


class TestTheMergeAndQuickWiring(unittest.TestCase):
    # merge_sort and quick_sort as FUNCTIONS return a new list. The methods have to
    # adopt that list -- self.values = merge_sort(self.values) -- or the object keeps
    # its old unsorted data and the sort appears to do nothing.

    def test_merge_sort_method_updates_the_object(self):
        sl = SortableList([5, 3, 8, 1])
        sl.merge_sort()
        self.assertEqual(sl.values, [1, 3, 5, 8],
                         "the method must adopt the new list the function returns")

    def test_quick_sort_method_updates_the_object(self):
        sl = SortableList([5, 3, 8, 1])
        sl.quick_sort()
        self.assertEqual(sl.values, [1, 3, 5, 8])

    def test_sorting_twice_is_harmless(self):
        for name in METHOD_NAMES:
            with self.subTest(method=name):
                sl = SortableList([3, 1, 2])
                getattr(sl, name)()
                getattr(sl, name)()
                self.assertEqual(sl.values, [1, 2, 3])


if __name__ == "__main__":
    unittest.main(verbosity=2)
