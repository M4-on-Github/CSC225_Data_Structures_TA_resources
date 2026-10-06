# PROBLEM 2 -- Topic 3 (arrays) and Topic 2 (Big-O)
#
# Check your work:   python -m unittest discover -s . -p "test_p2_search.py" -v
# Reference answer:  solutions/p2_search.py  (try first; consult one section if stuck)
#
# ---------------------------------------------------------------------------
# Four functions. The first two are the searches from the efficiency deck; the last two
# are the same searches with a counter, which is how O(log n) stops being a phrase and
# becomes a number you can look at.
#
#   linear_search(values, target)
#       Walk the list from index 0. Return the index of the first match, or -1.
#       Works on any list, sorted or not.
#
#   binary_search(values, element)
#       REQUIRES a list sorted in ascending order. Keep low and high bounds, look at
#       the middle, and throw away half the range each time. Return the index, or -1.
#
#       Two details that decide whether this works:
#         - the loop condition is  while low <= high,  not  low < high
#         - mid is  (low + high) // 2  with integer division
#       Using < can miss a match. Using / instead of // produces a float index and
#       raises TypeError. That is why the tests check misses as well as hits.
#
#   linear_search_count(values, target)
#       Return a TUPLE: (index, comparisons). Count one comparison per item examined.
#
#   binary_search_count(values, element)
#       Return a TUPLE: (index, comparisons). Count one middle-item probe per loop
#       iteration, not each individual == or < test.
#
# WHEN THEY PASS, do this -- it is the point of the problem:
# run binary_search_count on list(range(1000)) and then on list(range(1000000)),
# using -1 as the target both times. Predict both counts BEFORE you run it. A thousand
# times more data costs ten more probes here, illustrating logarithmic growth.
#
# Conventions: a miss returns -1, the parameter is "values", no imports.
# ---------------------------------------------------------------------------


def linear_search(values, target):
    pass  # TODO


def binary_search(values, element):
    pass  # TODO


def linear_search_count(values, target):
    pass  # TODO


def binary_search_count(values, element):
    pass  # TODO
