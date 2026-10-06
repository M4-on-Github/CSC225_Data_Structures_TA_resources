# Reference solution -- Problem 6. Topic 5 (heaps), applied.
#
# This is the "apply the structure to a problem" problem. You are not writing a heap
# here -- Problem 5 is the heap. You are deciding how to USE one, which is the harder
# and more examinable skill.
#
# THE PROBLEM. An emergency room treats the most urgent waiting patient next. Patients
# arrive constantly and are treated constantly. Urgency is an integer where 1 is the
# most urgent. Among patients of equal urgency, whoever arrived first is treated first.
#
# WHY A HEAP. The operations the room actually performs are "add a patient" and "take
# the most urgent one out", over and over, in no predictable order. That is insert and
# remove_min, O(log n) each. Keeping a sorted list instead would make each arrival an
# O(n) insert; re-sorting after every arrival would be O(n log n) per arrival. The heap
# wins because it never does the work of a total order it does not need -- which is the
# whole point of Topic 5.
#
# THE TRICK, and the thing worth remembering: Python compares tuples left to right, so
# a heap of tuples prioritises the first element, then the second, and so on. Putting
# urgency first is what makes the heap a priority queue. Putting the arrival counter
# SECOND is what makes equal urgencies come out in arrival order -- without it, the heap
# would silently tie-break on the patient's name, and "Adams" would beat "Zhang" for no
# medical reason at all.

from p5_min_heap import MinHeap


class TriageQueue:

    def __init__(self):
        self._heap = MinHeap()
        # Counts arrivals so ties in urgency are broken by who got here first.
        # It only ever goes up, so it can never tie either.
        self._arrivals = 0

    def arrive(self, name, urgency):
        self._heap.insert((urgency, self._arrivals, name))
        self._arrivals = self._arrivals + 1

    def peek_next(self):
        # Who WOULD be treated next, without treating them. O(1).
        item = self._heap.peek()
        if item is None:
            return None
        return item[2]

    def treat_next(self):
        # Treat the most urgent waiting patient and return their name. O(log n).
        # Returns None on an empty room, matching the pop-on-empty convention.
        item = self._heap.remove_min()
        if item is None:
            return None
        return item[2]

    def waiting(self):
        return self._heap.size()

    def is_empty(self):
        return self._heap.is_empty()

    def treat_all(self):
        # Drain the room, returning names in treatment order. Useful for checking your
        # own reasoning: the order out follows urgency, then arrival order.
        order = []
        while not self._heap.is_empty():
            order.append(self.treat_next())
        return order
