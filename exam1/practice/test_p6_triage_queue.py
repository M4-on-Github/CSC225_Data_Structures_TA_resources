# Tests for Problem 6. Run from this folder, the repository root, or its parent:
#
#     python -m unittest discover -s . -p "test_p6_triage_queue.py" -v
#
# This problem is about USING a heap, so most of these tests check an order of names
# rather than a list of numbers. Every expected order below came from running the
# reference implementation.

import unittest

from p6_triage_queue import TriageQueue

# Urgency 1 is the most urgent. Arrival order is the order of this list.
ARRIVALS = [
    ("Ruiz", 3),
    ("Okafor", 1),
    ("Lindqvist", 2),
    ("Adams", 3),
    ("Baptiste", 1),
]


def full_room():
    q = TriageQueue()
    for name, urgency in ARRIVALS:
        q.arrive(name, urgency)
    return q


class TestEmptyRoom(unittest.TestCase):

    def test_new_room_is_empty(self):
        q = TriageQueue()
        self.assertTrue(q.is_empty())
        self.assertEqual(q.waiting(), 0)

    def test_peek_on_empty_returns_none(self):
        self.assertIsNone(TriageQueue().peek_next())

    def test_treat_on_empty_returns_none(self):
        # Matches the pop-on-empty convention: an empty room is not an error.
        self.assertIsNone(TriageQueue().treat_next())

    def test_treat_all_on_empty(self):
        self.assertEqual(TriageQueue().treat_all(), [])


class TestWaitingCount(unittest.TestCase):

    def test_arrivals_increase_the_count(self):
        q = TriageQueue()
        for i, (name, urgency) in enumerate(ARRIVALS, start=1):
            q.arrive(name, urgency)
            self.assertEqual(q.waiting(), i)

    def test_treating_decreases_the_count(self):
        q = full_room()
        q.treat_next()
        self.assertEqual(q.waiting(), 4)

    def test_is_empty_after_treating_everyone(self):
        q = full_room()
        q.treat_all()
        self.assertTrue(q.is_empty())


class TestPriorityOrder(unittest.TestCase):

    def test_most_urgent_is_next(self):
        q = full_room()
        self.assertEqual(q.peek_next(), "Okafor")

    def test_peek_does_not_treat(self):
        q = full_room()
        q.peek_next()
        q.peek_next()
        self.assertEqual(q.waiting(), 5, "peek_next must not remove anyone")

    def test_the_full_treatment_order(self):
        self.assertEqual(full_room().treat_all(),
                         ["Okafor", "Baptiste", "Lindqvist", "Ruiz", "Adams"])

    def test_urgency_beats_arrival(self):
        # Ruiz arrived first and is treated fourth. Arrival order alone is wrong.
        order = full_room().treat_all()
        self.assertLess(order.index("Okafor"), order.index("Ruiz"))

    def test_ties_break_on_arrival_not_on_name(self):
        # The subtle one. Okafor and Baptiste are both urgency 1; Okafor arrived first,
        # so Okafor goes first. If your tuple is (urgency, name), the heap tie-breaks
        # alphabetically and Baptiste jumps the queue for no medical reason.
        order = full_room().treat_all()
        self.assertLess(order.index("Okafor"), order.index("Baptiste"))

        # Same check at urgency 3, where alphabetical order would reverse the pair.
        self.assertLess(order.index("Ruiz"), order.index("Adams"))

    def test_the_order_is_not_alphabetical(self):
        order = full_room().treat_all()
        self.assertNotEqual(order, sorted(order))

    def test_the_order_is_not_arrival_order(self):
        order = full_room().treat_all()
        self.assertNotEqual(order, [name for name, _ in ARRIVALS])


class TestInterleavedArrivalsAndTreatments(unittest.TestCase):
    # The real emergency room: people arrive while others are being treated. This is
    # what rules out "sort the list once at the start".

    def test_interleaved_sequence(self):
        q = TriageQueue()
        q.arrive("Ruiz", 3)
        q.arrive("Okafor", 1)
        self.assertEqual(q.treat_next(), "Okafor")

        q.arrive("Lindqvist", 2)
        q.arrive("Adams", 3)
        self.assertEqual(q.treat_next(), "Lindqvist")

        q.arrive("Baptiste", 1)
        self.assertEqual(q.treat_all(), ["Baptiste", "Ruiz", "Adams"])

    def test_a_new_urgent_arrival_goes_to_the_front(self):
        q = TriageQueue()
        q.arrive("Ruiz", 3)
        q.arrive("Adams", 3)
        self.assertEqual(q.peek_next(), "Ruiz")
        q.arrive("Okafor", 1)
        self.assertEqual(q.peek_next(), "Okafor",
                         "a more urgent arrival should become next immediately")

    def test_treating_everyone_twice_over(self):
        q = TriageQueue()
        for name, urgency in ARRIVALS:
            q.arrive(name, urgency)
        first = q.treat_all()
        for name, urgency in ARRIVALS:
            q.arrive(name, urgency)
        second = q.treat_all()
        self.assertEqual(first, second, "the queue should be reusable")


class TestSameUrgencyBehavesLikeAQueue(unittest.TestCase):

    def test_all_equal_urgency_is_first_in_first_out(self):
        q = TriageQueue()
        names = ["one", "two", "three", "four", "five"]
        for name in names:
            q.arrive(name, 2)
        self.assertEqual(q.treat_all(), names,
                         "with one urgency level the heap should behave like a FIFO queue")


if __name__ == "__main__":
    unittest.main(verbosity=2)
