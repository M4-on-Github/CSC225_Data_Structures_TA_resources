# Reference solution -- Problem 5. Topic 5 (heaps).
#
# PROVENANCE WARNING. No dedicated heap deck was available for this package. Deck 6 s32 says
# "Recall the central idea from our heap data structure lecture" and states three costs
# -- peek O(1), insert O(log n), remove O(log n) -- and s35 says a heap list is not
# fully sorted. Those are the heap property and costs cited by this package.
#
# Everything below the cost statements is standard material written for this package by
# your TA. It is correct and it is tested. It is not a prediction of what will be asked.
# Confirm with your instructor that heaps are on the exam before relying on this topic.
#
# Conventions kept from the decks even though the content is new:
#   - the backing store is self._items, a plain list, as the decks name theirs
#   - size() and is_empty() are methods, not properties
#   - peek() and remove_min() return None on an empty heap rather than raising,
#     matching the pop-on-empty convention
#   - no imports, no heapq, no sort() / sorted() anywhere
#   - insert() returns None: duplicates are allowed in a heap, so unlike a BST there
#     is no False-on-duplicate rule


# --- the index arithmetic, which is the whole trick ---------------------------
#
# A heap is a complete binary tree, so it fits in an array with no links at all.
# For the node at index i:
#
#       parent(i) = (i - 1) // 2        left(i) = 2i + 1        right(i) = 2i + 2
#
#              3                        index:  0  1  2  3  4  5
#            /   \                      value:  3  8  5  12 9  7
#           8     5
#          / \   /
#        12   9 7
#
# These three are module-level and tiny on purpose: they are the thing to memorise, and
# a student who can write them can rebuild the rest of the class from scratch.

def parent_index(i):
    return (i - 1) // 2


def left_index(i):
    return 2 * i + 1


def right_index(i):
    return 2 * i + 2


class MinHeap:
    # A min-heap: the smallest element is always at index 0.
    #
    # The heap property is LOCAL -- every node is <= both of its children. Nothing is
    # promised between a left child and a right child, or between cousins. That is much
    # weaker than being sorted, which is why a heap is cheap to maintain, and why
    # reading the list from index 0 to the end does NOT give you sorted order.

    def __init__(self):
        self._items = []

    def size(self):
        return len(self._items)

    def is_empty(self):
        return len(self._items) == 0

    def peek(self):
        # O(1): the minimum is already at index 0. This is the whole reason to use a heap.
        if self.is_empty():
            return None
        return self._items[0]

    def insert(self, element):
        # Append -- the only spot that keeps the tree complete -- then let it climb.
        # O(log n), because the climb is bounded by the height of the tree.
        self._items.append(element)
        self._sift_up(len(self._items) - 1)

    def remove_min(self):
        # Two steps before any sifting: save the root, then move the LAST item into
        # index 0 (again, to keep the tree complete). Only then does it sink. O(log n).
        if self.is_empty():
            return None

        smallest = self._items[0]
        last = self._items.pop()

        if not self.is_empty():
            self._items[0] = last
            self._sift_down(0)

        return smallest

    def _sift_up(self, i):
        # Climb while this node is smaller than its parent.
        while i > 0:
            p = parent_index(i)
            if self._items[i] < self._items[p]:
                self._items[i], self._items[p] = self._items[p], self._items[i]
                i = p
            else:
                break

    def _sift_down(self, i):
        # Sink while this node is bigger than its SMALLER child. Swapping with the
        # smaller child is the step students get wrong -- choosing either child arbitrarily
        # can break the heap property on the other side.
        n = len(self._items)
        while True:
            left = left_index(i)
            right = right_index(i)
            smallest = i

            if left < n and self._items[left] < self._items[smallest]:
                smallest = left
            if right < n and self._items[right] < self._items[smallest]:
                smallest = right

            if smallest == i:
                break

            self._items[i], self._items[smallest] = self._items[smallest], self._items[i]
            i = smallest

    def to_list(self):
        # The array as it actually sits in memory -- level by level, left to right.
        # Use this to check your paper traces.
        return list(self._items)


def build_heap(values):
    # Heapify an existing list in O(n), not O(n log n).
    #
    # Inserting n items one at a time costs O(n log n) in the worst case. Sifting DOWN
    # from the last parent back to index 0 costs O(n), because most nodes are near the bottom of the
    # tree and barely move. That gap is the classic heap result and the reason this
    # function exists at all.
    heap = MinHeap()
    heap._items = list(values)

    # Everything from the last parent back to index 0. Leaves need no work.
    start = parent_index(len(heap._items) - 1)
    for i in range(start, -1, -1):
        heap._sift_down(i)

    return heap


def heap_sort(values):
    # Build a heap, then drain it. Returns a NEW list.
    #
    # O(n log n) in the worst case, unlike quick sort's O(n^2) worst case.
    # Actual work can vary: with all values equal, sifts stop immediately and this
    # implementation takes O(n) time.
    #
    # Note the return convention: like merge and quick sort, this BUILDS A NEW LIST and
    # leaves the argument alone. heap_sort_in_place below is the other half of the pair.
    heap = build_heap(values)
    result = []
    while not heap.is_empty():
        result.append(heap.remove_min())
    return result


def heap_sort_in_place(values):
    # Sort the list itself, with no second list anywhere. Returns the SAME object.
    #
    # This uses a MAX-heap, not a min-heap, and that is forced: repeatedly moving the
    # LARGEST item to the back grows a sorted region at the END of the same array the
    # heap lives in. With a min-heap you would get descending order.
    #
    # After k removals the array is [ heap of n-k items | k largest items, sorted ].
    n = len(values)

    # Build a max-heap over the whole list, bottom-up.
    for i in range(parent_index(n - 1), -1, -1):
        _sift_down_max(values, i, n)

    # Shrink the heap one slot at a time; each evicted root lands in its final place.
    for end in range(n - 1, 0, -1):
        values[0], values[end] = values[end], values[0]
        _sift_down_max(values, 0, end)

    return values


def _sift_down_max(values, i, limit):
    # The same sink as MinHeap._sift_down, but comparing the other way and over only
    # values[0:limit] -- everything from limit onwards is sorted and must not move.
    while True:
        left = left_index(i)
        right = right_index(i)
        largest = i

        if left < limit and values[left] > values[largest]:
            largest = left
        if right < limit and values[right] > values[largest]:
            largest = right

        if largest == i:
            break

        values[i], values[largest] = values[largest], values[i]
        i = largest
