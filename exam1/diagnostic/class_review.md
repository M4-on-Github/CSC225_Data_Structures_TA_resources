# Foundation check in a 45 minute review

Give students the four-page [question sheet](questions.pdf). Hold the [answer guide](answers.pdf) until self-checking. Use worst-case efficiency only and plain-language pseudocode for sorting. Students draw and update a heap on paper if heaps are included; a text description of the tree is also acceptable. Speed and total score are not readiness measures.

| Minutes | Activity |
|---|---|
| 0 to 3 | Explain the goal: identify one or two concepts to practise. Point out the sorting table on page 4; heaps are optional. |
| 3 to 25 | Independent attempt. Suggest about 13 minutes for questions 1 to 12, 3 for the heap drawing if included, and 6 for question 13. Remind students to reach page 4 even if earlier answers are unfinished. These are pacing suggestions, not limits on accommodations. |
| 25 to 30 | Reveal the guide. Students flag incorrect answers, guesses and unclear derivations. Ask for the most uncertain sorting row or heap step. |
| 30 to 40 | Teach the two most common gaps. Trace sorting pseudocode on a worst-case input and count its work. If heap structure is a common gap, draw the tree and show removal one swap at a time. |
| 40 to 45 | Close the guide. Give one fresh retry below. Students explain it and name their next review activity. |

## Choose the explanation from the evidence

- Wrong table and weak reasoning: rebuild the algorithm's steps on a small list.
- Correct table but weak reasoning: ask where the sum or recursion levels come from.
- Sound reasoning with a wrong cell: check arithmetic, notation or the implementation assumption.
- A confident error: ask for the rule the student used, then show a counterexample.

Avoid assigning an entire topic as a weakness from one response. Use the retry to check the suspected gap. If students need longer, keep the last five minutes for choosing a next step and let them finish the attempt later.

## Fresh exit questions

Choose one that matches the discussion; students need not complete all three.

1. Bubble sort receives [4, 3, 2, 1]. Trace the passes on paper. Explain why the worst-case cost is quadratic for n items.
2. Write selection-sort pseudocode for a list of 8 items. How many comparisons does it make in the worst case? Generalize to n.
3. The taught quick sort receives [2, 4, 6, 8, 10]. Identify the first pivot and partition sizes. Explain what happens if this pattern repeats for n items.

Answers: 1. Passes end [3, 2, 1, 4], [2, 1, 3, 4], [1, 2, 3, 4]. The shrinking passes make (n - 1) + ... + 1 comparisons: O(n squared). 2. Repeatedly scan the unsorted region for its minimum and swap it into place; 28 comparisons for 8 items and n(n - 1)/2 in general. 3. Pivot 10, left size 4 and right size 0; repeated one-item reductions give O(n squared) total work.

End with: “The concept I will practise next is ____. I will check it by ____.” Use the [study paths](../study_paths.md) to choose a specific activity.
