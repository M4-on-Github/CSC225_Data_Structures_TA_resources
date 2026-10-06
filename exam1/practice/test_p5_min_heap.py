# Tests for Problem 5. Run from this folder, the repository root, or its parent:
#
#     python -m unittest discover -s . -p "test_p5_min_heap.py" -v
#
# Every expected list in here was produced by running the reference implementation, not
# typed from memory. If one of these disagrees with what you worked out on paper, the
# useful move is to find the single step where you and it part company.

import unittest

from p5_min_heap import (parent_index, left_index, right_index, MinHeap,
                         build_heap, heap_sort, heap_sort_in_place)


def heap_property_holds(items):
    # Every node is <= both of its children. Checking the children of each node is the
    # same work as checking the parent of each node, and reads better.
    for i in range(len(items)):
        for child in (left_index(i), right_index(i)):
            if child < len(items) and items[i] > items[child]:
                return False
    return True


class TestIndexArithmetic(unittest.TestCase):

    def test_left_and_right(self):
        self.assertEqual(left_index(0), 1)
        self.assertEqual(right_index(0), 2)
        self.assertEqual(left_index(4), 9)
        self.assertEqual(right_index(4), 10)

    def test_parent(self):
        self.assertEqual(parent_index(1), 0)
        self.assertEqual(parent_index(2), 0)
        self.assertEqual(parent_index(4), 1)
        self.assertEqual(parent_index(9), 4)
        self.assertEqual(parent_index(10), 4)

    def test_parent_of_root_is_negative_one(self):
        # Integer floor division gives -1, which is why every sift-up loop guards with
        # "while i > 0" instead of trusting the arithmetic.
        self.assertEqual(parent_index(0), -1)

    def test_the_formulas_are_inverses(self):
        for i in range(1, 50):
            with self.subTest(i=i):
                self.assertEqual(parent_index(left_index(i)), i)
                self.assertEqual(parent_index(right_index(i)), i)


class TestEmptyHeap(unittest.TestCase):

    def test_new_heap_is_empty(self):
        h = MinHeap()
        self.assertTrue(h.is_empty())
        self.assertEqual(h.size(), 0)

    def test_peek_on_empty_returns_none(self):
        # The pop-on-empty convention: return None, do not raise.
        self.assertIsNone(MinHeap().peek())

    def test_remove_min_on_empty_returns_none(self):
        self.assertIsNone(MinHeap().remove_min())

    def test_to_list_on_empty(self):
        self.assertEqual(MinHeap().to_list(), [])


class TestInsert(unittest.TestCase):

    def test_the_traced_sequence(self):
        # Insert 5, 3, 8, 1, 9, 2 into an empty min-heap, in that order.
        expected = [
            [5],
            [3, 5],
            [3, 5, 8],
            [1, 3, 8, 5],
            [1, 3, 8, 5, 9],
            [1, 3, 2, 5, 9, 8],
        ]
        h = MinHeap()
        for value, want in zip([5, 3, 8, 1, 9, 2], expected):
            h.insert(value)
            self.assertEqual(h.to_list(), want,
                             "after inserting " + str(value))

    def test_inserting_four_costs_no_swaps(self):
        # Worth knowing: a new item only climbs if it is smaller than its parent.
        # 4 lands at index 6, whose parent (index 2) holds 2, so it stays put.
        h = MinHeap()
        for value in [5, 3, 8, 1, 9, 2]:
            h.insert(value)
        h.insert(4)
        self.assertEqual(h.to_list(), [1, 3, 2, 5, 9, 8, 4])

    def test_insert_returns_none(self):
        # Duplicates are allowed in a heap, so there is no False-on-duplicate rule.
        h = MinHeap()
        self.assertIsNone(h.insert(5))
        self.assertIsNone(h.insert(5))
        self.assertEqual(h.size(), 2)

    def test_peek_is_always_the_minimum(self):
        h = MinHeap()
        for value in [42, 17, 93, 4, 55, 1, 70]:
            h.insert(value)
            self.assertEqual(h.peek(), min(h.to_list()))

    def test_heap_property_after_every_insert(self):
        h = MinHeap()
        for value in [9, 4, 7, 1, 8, 2, 6, 3, 5, 0]:
            h.insert(value)
            self.assertTrue(heap_property_holds(h.to_list()),
                            "heap property broken after inserting " + str(value))

    def test_the_list_is_not_sorted(self):
        # The headline fact of the topic: index 0 is the minimum, but the heap property
        # does not promise that the whole list is sorted.
        h = MinHeap()
        for value in [5, 3, 8, 1, 9, 2]:
            h.insert(value)
        self.assertEqual(h.to_list(), [1, 3, 2, 5, 9, 8])
        self.assertNotEqual(h.to_list(), sorted(h.to_list()))


class TestRemoveMin(unittest.TestCase):

    def test_the_traced_removals(self):
        h = MinHeap()
        h._items = [1, 3, 2, 5, 9, 8]

        self.assertEqual(h.remove_min(), 1)
        self.assertEqual(h.to_list(), [2, 3, 8, 5, 9])

        self.assertEqual(h.remove_min(), 2)
        self.assertEqual(h.to_list(), [3, 5, 8, 9])

    def test_removals_come_out_in_order(self):
        data = [5, 3, 8, 1, 9, 2, 8, 0, 11]
        h = MinHeap()
        for value in data:
            h.insert(value)
        # Counted rather than written as "while not h.is_empty()" on purpose: an
        # unfinished is_empty() would make that loop run forever instead of failing.
        out = []
        for _ in data:
            out.append(h.remove_min())
        self.assertEqual(out, [0, 1, 2, 3, 5, 8, 8, 9, 11])
        self.assertTrue(h.is_empty())

    def test_heap_property_after_every_removal(self):
        data = [9, 4, 7, 1, 8, 2, 6, 3, 5, 0]
        h = MinHeap()
        for value in data:
            h.insert(value)
        for _ in data:
            h.remove_min()
            self.assertTrue(heap_property_holds(h.to_list()))
        self.assertTrue(h.is_empty())

    def test_size_shrinks(self):
        h = MinHeap()
        for value in [3, 1, 2]:
            h.insert(value)
        h.remove_min()
        self.assertEqual(h.size(), 2)

    def test_last_removal_empties_the_heap(self):
        h = MinHeap()
        h.insert(7)
        self.assertEqual(h.remove_min(), 7)
        self.assertTrue(h.is_empty())
        self.assertEqual(h.to_list(), [])


class TestBuildHeap(unittest.TestCase):

    def test_the_traced_build(self):
        self.assertEqual(build_heap([9, 7, 5, 3, 1, 8, 2]).to_list(),
                         [1, 3, 2, 9, 7, 8, 5])

    def test_an_already_sorted_list_is_already_a_heap(self):
        # Not a bug. Every ascending list satisfies the min-heap property, because
        # values[i] <= values[2i+1] follows from being sorted. The converse is false,
        # which is the whole asymmetry of the topic.
        self.assertEqual(build_heap([1, 2, 3, 4, 5]).to_list(), [1, 2, 3, 4, 5])

    def test_build_heap_does_not_modify_its_argument(self):
        original = [9, 7, 5, 3, 1, 8, 2]
        build_heap(original)
        self.assertEqual(original, [9, 7, 5, 3, 1, 8, 2])

    def test_heap_property_on_many_inputs(self):
        cases = [
            [], [1], [2, 1], [5, 4, 3, 2, 1], [1, 2, 3, 4, 5],
            [9, 7, 5, 3, 1, 8, 2], [4, 4, 4, 4], [0, -3, 7, -8, 2],
            list(range(20, 0, -1)),
        ]
        for case in cases:
            with self.subTest(case=case):
                self.assertTrue(heap_property_holds(build_heap(case).to_list()))

    def test_build_heap_keeps_every_value(self):
        values = [9, 7, 5, 3, 1, 8, 2]
        self.assertEqual(sorted(build_heap(values).to_list()), sorted(values))

    def test_empty_build(self):
        self.assertEqual(build_heap([]).to_list(), [])


class TestHeapSort(unittest.TestCase):

    CASES = [
        [], [1], [2, 1], [5, 3, 8, 1, 9, 2, 8], [1, 2, 3, 4, 5],
        [5, 4, 3, 2, 1], [7, 7, 7], [0, -3, 7, -8, 2],
    ]

    def test_heap_sort_sorts(self):
        for case in self.CASES:
            with self.subTest(case=case):
                self.assertEqual(heap_sort(list(case)), sorted(case))

    def test_heap_sort_returns_a_new_list(self):
        # Same convention as merge and quick sort.
        original = [5, 3, 8, 1]
        result = heap_sort(original)
        self.assertIsNot(result, original)
        self.assertEqual(original, [5, 3, 8, 1],
                         "heap_sort must not modify its argument")

    def test_in_place_version_sorts(self):
        for case in self.CASES:
            with self.subTest(case=case):
                self.assertEqual(heap_sort_in_place(list(case)), sorted(case))

    def test_in_place_version_returns_the_same_object(self):
        original = [5, 3, 8, 1]
        result = heap_sort_in_place(original)
        self.assertIs(result, original)
        self.assertEqual(original, [1, 3, 5, 8])

    def test_both_versions_agree(self):
        for case in self.CASES:
            with self.subTest(case=case):
                self.assertEqual(heap_sort(list(case)),
                                 heap_sort_in_place(list(case)))

    def test_ascending_in_place_needs_a_max_heap(self):
        # Sanity check on the direction. If you build a MIN-heap and run the same
        # shrink loop, this comes out descending.
        self.assertEqual(heap_sort_in_place([5, 3, 8, 1, 9, 2, 8]),
                         [1, 2, 3, 5, 8, 8, 9])


if __name__ == "__main__":
    unittest.main(verbosity=2)
