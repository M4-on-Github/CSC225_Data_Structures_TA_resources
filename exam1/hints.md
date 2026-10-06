# Hints and worked answers

Read one hint, return to [guided practice](guided_practice.md), and try again. Use the answer only when you need it. Then close both pages and retry.

## Python

Hint: draw two arrows to the same list. Appending changes that list. Assignment moves one arrow.

Answer: a is [2, 5] after both steps. `append` mutates; `b = [8]` rebinds b.

## Complexity

Hint: count the inner loop once for each outer iteration. Separate loops add their work.

Answer: 12 prints; n squared for nested loops; 2n for consecutive loops.

## Arrays and search

Hint: resize only when all slots are occupied. In binary search, discard the middle value too when it is too small.

Answer: second append gives size 2, capacity 2, one old item copied. Third gives size 3, capacity 4, two copied. The search updates low to 3; the next middle index is 3, holding 7.

## Sorting

Hint: bubble compares neighbours. Merge combines already-sorted lists by taking the smaller front item.

Answer: bubble reaches [2, 1, 3], placing 3 at the end. The recursive merge returns [1, 2], then the final merge returns [1, 2, 3].

## Heaps

Hint: min-heap insertion compares upward. In-place heap sort excludes each finished tail item from later sifts.

Answer: insertion goes through [2, 1, 4, 5] to [1, 2, 4, 5]. The active max-heap [2, 1] needs no sift swap. Its next root swap produces [1, 2, 3].
