# Tests for Problem 2. Run from this folder, the repository root, or its parent:
#
#     python -m unittest discover -s . -p "test_p2_search.py" -v

import unittest

from p2_search import (linear_search, binary_search,
                       binary_search_count, linear_search_count)


class TestLinearSearch(unittest.TestCase):

    def test_finds_first_item(self):
        self.assertEqual(linear_search([4, 8, 15, 16, 23, 42], 4), 0)

    def test_finds_middle_item(self):
        self.assertEqual(linear_search([4, 8, 15, 16, 23, 42], 16), 3)

    def test_finds_last_item(self):
        self.assertEqual(linear_search([4, 8, 15, 16, 23, 42], 42), 5)

    def test_miss_returns_minus_one(self):
        self.assertEqual(linear_search([4, 8, 15, 16, 23, 42], 99), -1)

    def test_empty_list(self):
        self.assertEqual(linear_search([], 1), -1)

    def test_works_on_unsorted(self):
        # The one thing linear search can do that binary search cannot.
        self.assertEqual(linear_search([9, 3, 7, 1], 7), 2)

    def test_returns_first_of_duplicates(self):
        self.assertEqual(linear_search([5, 5, 5], 5), 0)


class TestBinarySearch(unittest.TestCase):

    def test_finds_middle_item(self):
        self.assertEqual(binary_search([4, 8, 15, 16, 23, 42], 15), 2)

    def test_finds_first_item(self):
        self.assertEqual(binary_search([4, 8, 15, 16, 23, 42], 4), 0)

    def test_finds_last_item(self):
        self.assertEqual(binary_search([4, 8, 15, 16, 23, 42], 42), 5)

    def test_miss_below_range(self):
        self.assertEqual(binary_search([4, 8, 15, 16, 23, 42], 1), -1)

    def test_miss_above_range(self):
        self.assertEqual(binary_search([4, 8, 15, 16, 23, 42], 99), -1)

    def test_miss_inside_range(self):
        # A miss inside the range of values. Correct bound updates must eventually
        # exhaust the search interval and return -1.
        self.assertEqual(binary_search([4, 8, 15, 16, 23, 42], 20), -1)

    def test_empty_list(self):
        self.assertEqual(binary_search([], 1), -1)

    def test_single_item_hit(self):
        self.assertEqual(binary_search([7], 7), 0)

    def test_single_item_miss(self):
        self.assertEqual(binary_search([7], 8), -1)

    def test_every_item_in_a_long_list(self):
        values = list(range(0, 200, 2))
        for i, v in enumerate(values):
            self.assertEqual(binary_search(values, v), i)

    def test_every_miss_in_a_long_list(self):
        values = list(range(0, 200, 2))
        for v in range(1, 200, 2):
            self.assertEqual(binary_search(values, v), -1)


class TestComparisonCounts(unittest.TestCase):
    # This is where Topic 2 meets Topic 3: the costs stop being words and become numbers.

    def test_binary_search_is_logarithmic(self):
        # Searching 1,000 items needs at most 10 probes: 2**10 is just over 1,000.
        values = list(range(1000))
        _, comparisons = binary_search_count(values, 999)
        self.assertLessEqual(comparisons, 10,
                             "binary search on 1,000 items should need about 10 comparisons")

    def test_a_thousand_times_more_data_costs_ten_more_comparisons(self):
        # The headline result of the whole topic. 1,000x the data, 10 more comparisons.
        small = list(range(1000))
        big = list(range(1000000))
        _, c_small = binary_search_count(small, -1)
        _, c_big = binary_search_count(big, -1)
        self.assertLessEqual(c_big - c_small, 11)

    def test_linear_search_is_linear(self):
        # The contrast: the last item costs one comparison per item.
        values = list(range(1000))
        _, comparisons = linear_search_count(values, 999)
        self.assertEqual(comparisons, 1000)

    def test_linear_search_worst_case_is_a_miss(self):
        values = list(range(1000))
        index, comparisons = linear_search_count(values, 5000)
        self.assertEqual(index, -1)
        self.assertEqual(comparisons, 1000)

    def test_counts_agree_with_the_plain_versions(self):
        values = list(range(0, 100, 3))
        for target in [0, 3, 48, 99, 100, -5]:
            self.assertEqual(binary_search_count(values, target)[0],
                             binary_search(values, target))
            self.assertEqual(linear_search_count(values, target)[0],
                             linear_search(values, target))


if __name__ == "__main__":
    unittest.main(verbosity=2)
