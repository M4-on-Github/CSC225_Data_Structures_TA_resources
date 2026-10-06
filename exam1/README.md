# Data Structures — Exam 1 study package

Five topics. For each one: a **review sheet** that teaches it, a **mock test** that examines
it, and a **solutions file** you check yourself against. Plus six **practice coding
problems** that check themselves by running a test file.

Everything is here at once — the papers and the answers together. That is deliberate, and it
puts one thing on you: **attempt a paper before you open its solutions.** Reading the
answers feels like studying and is not. What an exam measures is whether you can produce
an answer, and you cannot practise that by recognising one.

---

## The five topics

| # | Topic | Review | Mock | Solutions | In the mock |
|---|---|---|---|---|---|
| 1 | Python review — classes and argument passing | [review](topics/1-python-review/review.md) | [mock](topics/1-python-review/mock.md) | [solutions](topics/1-python-review/solutions.md) | 8 drills, 3 questions |
| 2 | Big-O and counting operations | [review](topics/2-big-o/review.md) | [mock](topics/2-big-o/mock.md) | [solutions](topics/2-big-o/solutions.md) | 5 drills, 5 questions |
| 3 | Arrays, Python lists, and search | [review](topics/3-arrays/review.md) | [mock](topics/3-arrays/mock.md) | [solutions](topics/3-arrays/solutions.md) | 8 drills, 4 questions |
| 4 | Sorting — all five algorithms | [review](topics/4-sorting/review.md) | [mock](topics/4-sorting/mock.md) | [solutions](topics/4-sorting/solutions.md) | 10 drills, 9 questions |
| 5 | Heaps | [review](topics/5-heaps/review.md) | [mock](topics/5-heaps/mock.md) | [solutions](topics/5-heaps/solutions.md) | 11 drills, 5 questions |

**Nothing here is scored.** There are no marks on any question, because the real paper's
marking is your instructor's to decide and inventing a number would only tell you something
false. The mocks exist to show you whether you understand the topic. No mock prints a time
limit either: work until you are done, note how long it took, and compare that with
however long you get.

Work them in order. Topic 1 is the vocabulary everything else is written in, Topic 2 is the
cost language, and Topics 3–5 apply both. Topic 4 is the biggest and the likeliest to carry
a coding question.

---

## The practice problems

[`practice/`](practice/README.md) holds six coding problems. You write the code, run the
test file, and it tells you whether you got it right — no answer key to read off, and nobody
has to be in the room.

| # | File | Topic |
|---|---|---|
| 1 | `p1_bank_account.py` | 1 — classes and argument passing |
| 2 | `p2_search.py` | 3 — linear and binary search, with counting versions |
| 3 | `p3_sorts.py` | 4 — all five sorts as functions |
| 4 | `p4_sortable_list.py` | 4 — the same five as methods on a class |
| 5 | `p5_min_heap.py` | 5 — `MinHeap`, `build_heap`, both heap sorts |
| 6 | `p6_triage_queue.py` | 5 — applying a heap to a problem |

```
cd practice
python test_p3_sorts.py      # check one problem
python check.py              # check all six, with a summary
```

Do problem 3 after Topic 4's review sheet, problem 4 after problem 3, and problem 6 after
problem 5. **If you only have time for one problem in the whole package, do problem 3.**

---

## How to use a topic

1. Read `review.md`. It teaches the topic, quotes the slides where they say something
   exactly, and ends with a checklist and a "where people go wrong" list.
2. Close it and work `mock.md` on paper. Write out the traces; do not do them in your head.
3. Check yourself against `solutions.md`. Each answer is followed by **what a complete
   answer needs** — usually the justification rather than the answer itself, which is the
   part people leave out.
4. Read the **If you got it wrong** section at the end of the solutions. It says which
   slides to go back to for each question you missed.
5. Write the matching practice problem.

A question you got wrong is worth more than one you got right. The point of printing what a
complete answer needs is that you can see *why* a half-answer is only half.

---

## Two things to know about the content

**It is drawn from the slides, not from a textbook.** Every fact, cost and quote traces
back to one of the eight lecture decks, cited by deck and slide number so you can go and
check it. Nothing here is invented to look hard.

**With one flagged exception: heaps.** There is no heap lecture deck in this course.
The slides give the heap *property* and three *costs* on Deck 6 s32 and s35 and refer to a
"heap data structure lecture" whose slides are not among the eight. Topic 5 teaches heaps
in full anyway — the index arithmetic, both sifts, `build_heap`, both heap sorts — and
**every page of it says plainly which parts come from the slides and which are your TA's.**
**Confirm with your instructor that heaps are on the exam** before spending serious time there.

## What is not in here

Linked lists, stacks, queues, priority queues and binary search trees are **out of scope**
for Exam 1 and appear nowhere in this package. Their decks are still in `slides/` if you
want them for later in the course.

---

## What else is in this folder

- `slides/` — the eight lecture decks, as handed out. The source for everything above.
- `coverage-map.md` — a slide-by-slide map of all eight decks, with what each one covers.
  Useful if you want to find the slide behind a particular claim, or to check what a deck
  contains before reading it.

---

*Questions, or something here that looks wrong? Tell your TA. If
`python practice/check.py --solutions` ever reports a failure, that is a bug in the
reference answers, not in your work — say so.*
