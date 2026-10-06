# Tests for Problem 3. Run from this folder, the repository root, or its parent:
#
#     python -m unittest discover -s . -p "test_p3_sorts.py" -v
#
# These tests check three separate things:
#   1. does it sort
#   2. does it return the SAME list object or a NEW one -- the lecture conventions differ
#      per sort
#   3. does it match the expected counts, snapshots and duplicate handling

import unittest

from p3_sorts import (selection_sort, bubble_sort, insertion_sort,
                      merge_sort, quick_sort, selection_sort_count,
                      bubble_sort_passes)

IN_PLACE = [selection_sort, bubble_sort, insertion_sort]
NEW_LIST = [merge_sort, quick_sort]
ALL_SORTS = IN_PLACE + NEW_LIST

CASES = [
    [],
    [1],
    [2, 1],
    [1, 2],
    [5, 3, 8, 1, 9, 2, 8],
    [5, 1, 4, 2, 8],
    [1, 2, 3, 4, 5],
    [5, 4, 3, 2, 1],
    [7, 7, 7, 7],
    [3, -1, 0, -7, 12, 3],
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0],
]


class TestTheySort(unittest.TestCase):

    def test_every_sort_on_every_case(self):
        for sort in ALL_SORTS:
            for case in CASES:
                with self.subTest(sort=sort.__name__, case=case):
                    expected = sorted(case)
                    got = sort(list(case))
                    self.assertEqual(got, expected)


class TestReturnConventions(unittest.TestCase):
    # In-place sorts return the list they were given; merge and quick build a new one
    # for inputs of two or more items and leave the argument alone.

    def test_in_place_sorts_return_the_same_object(self):
        for sort in IN_PLACE:
            with self.subTest(sort=sort.__name__):
                original = [5, 3, 8, 1]
                result = sort(original)
                self.assertIs(result, original,
                              sort.__name__ + " should return the SAME list object")

    def test_in_place_sorts_modify_the_caller_list(self):
        for sort in IN_PLACE:
            with self.subTest(sort=sort.__name__):
                original = [5, 3, 8, 1]
                sort(original)
                self.assertEqual(original, [1, 3, 5, 8],
                                 sort.__name__ + " should sort the caller's list")

    def test_new_list_sorts_return_a_different_object(self):
        for sort in NEW_LIST:
            with self.subTest(sort=sort.__name__):
                original = [5, 3, 8, 1]
                result = sort(original)
                self.assertIsNot(result, original,
                                 sort.__name__ + " should return a NEW list")

    def test_new_list_sorts_leave_the_argument_alone(self):
        for sort in NEW_LIST:
            with self.subTest(sort=sort.__name__):
                original = [5, 3, 8, 1]
                sort(original)
                self.assertEqual(original, [5, 3, 8, 1],
                                 sort.__name__ + " must not modify its argument")


class TestLectureBehaviour(unittest.TestCase):

    def test_merge_sort_is_stable(self):
        # This checks tuple sorting. Python compares both tuple fields, so these data
        # alone cannot establish stability for items with equal comparison keys.
        pairs = [(1, "a"), (0, "b"), (1, "c"), (0, "d"), (1, "e")]
        result = merge_sort(list(pairs))
        ones = [tag for key, tag in result if key == 1]
        self.assertEqual(ones, ["a", "c", "e"],
                         "merge sort should keep equal items in their original order")

    def test_quick_sort_handles_duplicates_of_the_pivot(self):
        # The three-way split puts every copy of the pivot in the middle group, so
        # duplicates cannot cause infinite recursion.
        self.assertEqual(quick_sort([4, 4, 4, 4]), [4, 4, 4, 4])
        self.assertEqual(quick_sort([9, 1, 9, 1, 9]), [1, 1, 9, 9, 9])

    def test_bubble_sort_first_pass(self):
        # Drill 4.2 on paper. The first pass drags the largest item to the end.
        passes = bubble_sort_passes([5, 1, 4, 2, 8])
        self.assertEqual(passes[0], [1, 4, 2, 5, 8])

    def test_bubble_sort_early_exit_on_sorted_input(self):
        # The "swapped" flag earns bubble sort its O(n) best case: one pass, then stop.
        passes = bubble_sort_passes([1, 2, 3, 4, 5])
        self.assertEqual(len(passes), 1,
                         "an already-sorted list should take exactly one pass")

    def test_bubble_sort_no_early_exit_on_reversed_input(self):
        passes = bubble_sort_passes([5, 4, 3, 2, 1])
        self.assertEqual(len(passes), 4)
        self.assertEqual(passes[-1], [1, 2, 3, 4, 5])


class TestSelectionSortCount(unittest.TestCase):

    def test_comparison_count_is_n_times_n_minus_one_over_two(self):
        for n in [1, 2, 5, 10, 20]:
            with self.subTest(n=n):
                values = list(range(n, 0, -1))
                _, comparisons, _ = selection_sort_count(values)
                self.assertEqual(comparisons, n * (n - 1) // 2)

    def test_sorted_and_reversed_cost_the_same_comparisons(self):
        # The result worth remembering: selection sort does not care about the input
        # order. Its inner loop never stops early, so even the best case is quadratic.
        _, sorted_comparisons, sorted_swaps = selection_sort_count(list(range(1, 11)))
        _, reversed_comparisons, reversed_swaps = selection_sort_count(list(range(10, 0, -1)))
        self.assertEqual(sorted_comparisons, reversed_comparisons)
        self.assertEqual(sorted_comparisons, 45)

    def test_sorted_input_needs_no_swaps(self):
        _, _, swaps = selection_sort_count(list(range(1, 11)))
        self.assertEqual(swaps, 0, "an already-sorted list needs no swaps")

    def test_reversed_input_does_swap(self):
        _, _, swaps = selection_sort_count(list(range(10, 0, -1)))
        self.assertEqual(swaps, 5)

    def test_it_still_sorts(self):
        values, _, _ = selection_sort_count([5, 3, 8, 1])
        self.assertEqual(values, [1, 3, 5, 8])


if __name__ == "__main__":
    unittest.main(verbosity=2)
