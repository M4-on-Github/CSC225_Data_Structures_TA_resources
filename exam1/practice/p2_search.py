# PROBLEM 2 -- Topic 3 (arrays) and Topic 2 (Big-O)
#
# Check your work:   python test_p2_search.py
# Reference answer:  solutions/p2_search.py  (open it AFTER the tests pass)
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
#       REQUIRES a sorted list. Keep low and high bounds, look at the middle, and throw
#       away half the range each time. Return the index, or -1.
#
#       Two details that decide whether this works:
#         - the loop condition is  while low <= high,  not  low < high
#         - mid is  (low + high) // 2  with integer division
#       Get either wrong and the function still returns answers, just wrong ones on
#       some inputs. That is why the tests check misses as well as hits.
#
#   linear_search_count(values, target)
#       Return a TUPLE: (index, comparisons). Count one comparison per item examined.
#
#   binary_search_count(values, element)
#       Return a TUPLE: (index, comparisons). Count one comparison per loop iteration.
#
# WHEN THEY PASS, do this -- it is the point of the problem:
# run binary_search_count on list(range(1000)) and then on list(range(1000000)).
# Predict both comparison counts BEFORE you run it. A thousand times more data costs
# about ten more comparisons, and that gap is the entire argument for Big-O.
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
