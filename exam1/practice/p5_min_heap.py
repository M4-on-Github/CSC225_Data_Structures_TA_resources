# PROBLEM 5 -- Topic 5: heaps
#
# Check your work:   python test_p5_min_heap.py
# Reference answer:  solutions/p5_min_heap.py  (open it AFTER the tests pass)
#
# ---------------------------------------------------------------------------
# WHERE THIS CAME FROM -- read this before you spend an evening on it.
#
# There is no heap lecture deck in this course. The entire slide record for heaps is
# three slides at the end of the stacks/queues deck: the heap PROPERTY, and three COSTS
# (insert, remove-min, build). Those slides point at a "heap data structure lecture"
# that is not among the eight decks we have.
#
# Everything else in this problem -- the index arithmetic, sifting up and down,
# build_heap, and both heap sorts -- was written by your TA to fill that gap, in the
# lecture's style. It is the standard treatment and it is consistent with the three
# slides, but it is NOT copied from anything Dr. Smith handed out.
#
# So: CONFIRM WITH DR. SMITH THAT HEAPS ARE ON THE EXAM before relying on this topic.
# If he says yes, this is good preparation. If he says no, skip it.
# ---------------------------------------------------------------------------
#
# PART A -- the index arithmetic
#
# A heap is stored in a plain list. The tree structure is arithmetic, not pointers.
#
#            index:  0   1   2   3   4   5   6
#                    1   3   2   5   9   8   4
#
#                          1(0)
#                        /      \
#                     3(1)      2(2)
#                    /    \     /   \
#                 5(3)  9(4)  8(5)  4(6)
#
#   parent_index(i)   returns the index of i's parent
#   left_index(i)     returns the index of i's left child
#   right_index(i)    returns the index of i's right child
#
# Work the three formulas out from the diagram above rather than looking them up -- the
# written exam can ask you for them with no computer in the room.
#
# One trap: parent_index(0) comes out as -1, which is a VALID Python index pointing at
# the last item. That is exactly why _sift_up's loop condition is "while i > 0" and not
# a check on the parent's value.
#
# PART B -- MinHeap
#
#   __init__(self)      an empty heap. The list is internal: self._items
#   size(self)          how many items
#   is_empty(self)      True when there are none
#   peek(self)          the smallest item, WITHOUT removing it. None on an empty heap.
#   insert(self, item)  add the item and restore the heap property. Returns None --
#                       a heap allows duplicates, so there is nothing to refuse.
#   remove_min(self)    remove and return the smallest item. None on an empty heap.
#   to_list(self)       a copy of the internal list, so tests can look at the layout
#
#   _sift_up(self, i)   the new item walks UP while it is smaller than its parent
#   _sift_down(self, i) the item walks DOWN, swapping with its SMALLER child
#
# How insert works: append at the end, then sift up from the last index.
# How remove_min works: remember item 0, move the LAST item into slot 0, pop the end,
# then sift down from 0. Moving the last item is what keeps the list gap-free.
#
# _sift_down must compare against the smaller of the two children, and must handle a
# node with only a left child. Getting that wrong gives a list that looks sorted-ish and
# fails the heap property three levels down.
#
# THE PROPERTY IS LOCAL: every parent is <= its children. That is all. A heap is NOT
# sorted -- [1, 3, 2, 5, 9, 8] is a perfectly good heap. Only index 0 is guaranteed.
#
# PART C -- build_heap and the two heap sorts
#
#   build_heap(values)
#       Turn an arbitrary list into a heap IN PLACE and return it. Do not insert the
#       items one at a time -- start at the LAST PARENT and sift down, walking backwards
#       to index 0. The leaves need no work; they are already one-item heaps.
#       That is why this is O(n) while n inserts cost O(n log n). The exam can ask you
#       which is cheaper and why.
#
#   heap_sort(values)
#       Returns a NEW sorted list: push everything into a MinHeap, then pull it back out
#       with remove_min. Smallest out first, so the result is ascending.
#
#   heap_sort_in_place(values)
#       Sorts the SAME list object and returns it, using no second heap.
#       Here is the twist worth understanding: to sort ASCENDING in place you need a
#       MAX heap, not a min heap. The largest item sits at index 0, you swap it to the
#       END of the list, shrink the heap by one, and sift down. Each pass parks one more
#       item in its final place at the back. A min heap would sort descending.
#       Write the max-heap sift as a separate helper, _sift_down_max(values, i, size).
#
# Heap sort is O(n log n) regardless of the input order -- there is no lucky case and no
# unlucky one, which is the property that distinguishes it from quick sort.
#
# Conventions: self._items, size()/is_empty() as methods, peek and remove_min return
# None rather than raising, insert returns None, no imports.
# ---------------------------------------------------------------------------


def parent_index(i):
    pass  # TODO


def left_index(i):
    pass  # TODO


def right_index(i):
    pass  # TODO


class MinHeap:

    def __init__(self):
        pass  # TODO

    def size(self):
        pass  # TODO

    def is_empty(self):
        pass  # TODO

    def peek(self):
        pass  # TODO

    def insert(self, item):
        pass  # TODO

    def remove_min(self):
        pass  # TODO

    def to_list(self):
        pass  # TODO

    def _sift_up(self, i):
        pass  # TODO

    def _sift_down(self, i):
        pass  # TODO


def build_heap(values):
    pass  # TODO


def heap_sort(values):
    pass  # TODO


def heap_sort_in_place(values):
    pass  # TODO


def _sift_down_max(values, i, size):
    pass  # TODO
