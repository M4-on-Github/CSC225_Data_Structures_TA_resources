# Tests for Problem 2. Run from the repository root or its parent:
# python -m unittest discover -s . -p "test_p2_search.py" -v

import unittest

from p2_search import linear_search, linear_search_count


class TestLinearSearch(unittest.TestCase):
    def test_first_middle_last_and_missing(self):
        values = [4, 8, 15, 16, 23, 42]
        self.assertEqual(linear_search(values, 4), 0)
        self.assertEqual(linear_search(values, 16), 3)
        self.assertEqual(linear_search(values, 42), 5)
        self.assertEqual(linear_search(values, 99), -1)

    def test_empty_unsorted_and_duplicates(self):
        self.assertEqual(linear_search([], 1), -1)
        self.assertEqual(linear_search([9, 3, 7, 1], 7), 2)
        self.assertEqual(linear_search([5, 5, 5], 5), 0)


class TestComparisonCounts(unittest.TestCase):
    def test_first_last_and_missing(self):
        values = [9, 3, 7, 1]
        self.assertEqual(linear_search_count(values, 9), (0, 1))
        self.assertEqual(linear_search_count(values, 1), (3, 4))
        self.assertEqual(linear_search_count(values, 8), (-1, 4))

    def test_empty_and_first_duplicate(self):
        self.assertEqual(linear_search_count([], 1), (-1, 0))
        self.assertEqual(linear_search_count([5, 5, 5], 5), (0, 1))

    def test_counts_agree_with_plain_search(self):
        values = list(range(0, 100, 3))
        for target in [0, 3, 48, 99, 100, -5]:
            self.assertEqual(linear_search_count(values, target)[0],
                             linear_search(values, target))


if __name__ == "__main__":
    unittest.main(verbosity=2)
