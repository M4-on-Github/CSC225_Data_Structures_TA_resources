# Topic 2 — Big-O and counting work

Big-O describes how an algorithm's work grows with input size `n`. Count operations
instead of measuring seconds. For this review and the foundation check, give the
**worst-case** cost unless a question says otherwise.

## Recognize the pattern

| Work | Worst-case cost | Why |
|---|---|---|
| One index lookup | O(1) | One operation |
| Repeated halving | O(log n) | The remaining range halves each step |
| One loop over `n` items | O(n) | Visits each item once |
| `n` searches, each halving a range | O(n log n) | `n` times `log n` |
| Two fully nested loops over `n` items | O(n²) | `n` times `n` |
| Doubling branches at each of `n` levels | O(2ⁿ) | Work doubles each level |

Sequential loops **add** their costs: O(n) + O(n) = O(n). Fully nested loops
**multiply**: n outer iterations × n inner iterations = O(n²). Drop constants and
smaller terms: 3n² + 7n + 2 is O(n²).

If the inner loop gets shorter each time, count `(n−1) + (n−2) + ... + 1 = n(n−1)/2`.
This is still O(n²); selection sort makes exactly this many comparisons. Binary search
discards about half the remaining sorted range each step, so it needs O(log n) checks.

## Check yourself

- Can you explain why two consecutive loops are O(n), while two nested loops are O(n²)?
- Can you derive `n(n−1)/2` instead of recalling it?
- Can you explain why halving gives a logarithm?

Try the [mock](mock.md) and [solutions](solutions.md). Next, use these costs in [arrays
and search](../3-arrays/review.md). Source: Algorithm Efficiency Introduction, Deck 3
slides 9–32.
