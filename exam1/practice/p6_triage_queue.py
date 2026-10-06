# PROBLEM 6 -- Topic 5: applying a heap to a problem
#
# Check your work:   python test_p6_triage_queue.py
# Reference answer:  solutions/p6_triage_queue.py  (open it AFTER the tests pass)
#
# Do Problem 5 first. This one imports MinHeap from it.
#
# The heap provenance warning at the top of p5_min_heap.py applies to this problem too:
# confirm with Dr. Smith that heaps are on the exam before relying on it.
#
# ---------------------------------------------------------------------------
# THE PROBLEM
#
# An emergency room. Patients arrive one at a time, each with an urgency rating where
# 1 is the most urgent. The next patient treated is always the most urgent one waiting,
# and when two patients are equally urgent the one who arrived FIRST goes first.
# Patients keep arriving while others are being treated.
#
# This is the shape of question Dr. Smith described: "code one of the data structures
# and use it to solve a problem." The data structure is the heap; the problem is the
# waiting room.
#
# WHY A HEAP. Think about the two obvious alternatives before you write anything:
#   - a plain list, searched for the minimum each time: the search is O(n) per patient
#   - a list kept sorted on arrival: the insertion has to shift items, also O(n)
# A heap does both halves in O(log n), and arrivals interleaved with treatments are
# exactly the case where that matters. If everyone arrived before anyone was treated,
# you could just sort once -- the tests deliberately interleave them so you cannot.
#
# WHAT TO WRITE
#
#   TriageQueue
#     __init__(self)               an empty room, holding a MinHeap
#     arrive(self, name, urgency)  a patient arrives
#     peek_next(self)              the name of the next patient to treat, without
#                                  removing them. None if the room is empty.
#     treat_next(self)             remove and return the name of the next patient.
#                                  None if the room is empty.
#     waiting(self)                how many patients are waiting
#     is_empty(self)               True when nobody is waiting
#     treat_all(self)              treat everyone, returning the list of names in the
#                                  order they were treated. The room ends up empty.
#
# THE TRICK THAT MAKES IT WORK
#
# A MinHeap compares whole items. Push a TUPLE and Python compares it left to right,
# so the first element decides and later elements only break ties. You want:
#
#       (urgency, arrival_counter, name)
#
# Keep a counter on the object, starting at 0, and increment it on every arrival.
#
# The ORDER of those three parts is the whole question, and it is what the tests check
# hardest. With (urgency, name) the heap tie-breaks alphabetically, so two patients at
# urgency 1 are seen in alphabetical order -- "Adams" beats "Zhang" for no medical
# reason at all. Putting the counter second makes equal urgencies come out in arrival
# order, which is the rule the problem actually states.
#
# The name stays in the tuple so you can read it back out when you pop. Remember that
# treat_next returns the NAME, not the tuple.
#
# Conventions: peek_next and treat_next return None on an empty room rather than
# raising, matching peek and remove_min. No imports except MinHeap.
# ---------------------------------------------------------------------------

from p5_min_heap import MinHeap


class TriageQueue:

    def __init__(self):
        pass  # TODO

    def arrive(self, name, urgency):
        pass  # TODO

    def peek_next(self):
        pass  # TODO

    def treat_next(self):
        pass  # TODO

    def waiting(self):
        pass  # TODO

    def is_empty(self):
        pass  # TODO

    def treat_all(self):
        pass  # TODO
