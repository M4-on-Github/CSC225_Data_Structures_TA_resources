# Topic 1 — solutions: classes and argument passing

Answers to [mock.md](mock.md), in order, each followed by what a complete answer needs.
**Attempt the paper first.** Every code answer here has been executed, not typed from memory.

---

## Part 1 — Drills

**1.1** `account = BankAccount("Ada", 100)` then `account.deposit(50)`. Note you pass
**two** arguments to a 3-parameter `__init__`, and **one** to a 2-parameter `deposit`:
`self` is supplied by Python. (Deck 2 s9.)

**1.2** It runs **automatically, once, the moment an object is created** — you never call
it by name. It returns nothing; its job is to attach attributes to `self`. (Deck 2 s7–s8.)

**1.3** The underscore is a **convention meaning "internal — don't touch from outside"**.
Python does not enforce it. The point is that the balance should only change through
`deposit` and `withdraw`, which can refuse a bad amount; `owner` has no such rule to
protect. (Deck 2 s11.)

**1.4** `[1, 2, 3, 4]`. `append` **mutates** the list the caller still points at, so the
change is visible outside the function. (Deck 2 s31, his side-by-side pair.)

**1.5** `[1, 2, 3]`. The assignment **rebinds the local name** `items` to a brand-new
list. The caller's `nums` was never touched. (Deck 2 s31, the other half of the same pair.)

**1.6** `+=` on a list is **in-place mutation**, so the caller sees `[1, 2, 3, 4]`.
`values = values + [4]` **builds a new list and rebinds the local name**, so the caller
still sees `[1, 2, 3]`. His diagnostic question is exactly this: *"Did the code change the
object, or did it move the local name?"* (Deck 2 s31–s32.)

**1.7** `x` is still **5**. Integers are **immutable**: there is no operation that changes
a 5 into a 6, so `y = 6` can only rebind. With a list, rebinding and mutating are two
different things you have to tell apart. *Mutability is about the object, not the variable
name.* (Deck 2 s23, s27.)

**1.8** **Rebinding** points a name at a different object; the old object is unchanged and
anyone else holding it sees nothing. **Mutating** changes the object itself, so every name
pointing at it sees the change. A variable is a **name tag attached to an object** —
rebinding moves the tag, mutating alters the thing the tag is stuck to. (Deck 2 s61.)

---

## Part 2 — Exam-style questions

### Q1 — Classes and objects
**(a)** A class is a **blueprint**; an object is **one thing built from that blueprint**.
(Deck 2 s7.)

**(b)** `self` is passed **automatically** by Python: it is the object the method was
called on. `account.deposit(50)` becomes `deposit(account, 50)`, so the one visible
argument lands in `amount`. (Deck 2 s9.)

**(c)** The leading underscore is a **convention meaning "internal, do not touch from
outside"**. Python does not enforce it. The point is that the balance should only change
through `deposit` and `withdraw`, which can refuse a bad amount. `owner` has no such rule
to protect. (Deck 2 s11.)

**What a complete answer needs**

- (a) Both blanks. "Blueprint / instance" is fine.
- (b) `self` named as **the object**, and the fact that Python supplies it for you.
  "`self` is the class" is the standard confusion — if you wrote that, reread Deck 2 s9.
- (c) Either "convention, not enforced" **or** "so it can only change through the guarded
  methods". The second is the better answer, because it says what the convention is *for*.

### Q2 — Code reading
```
[1, 2, 3, 99]
[1, 2, 3]
[1, 2, 3, 99]
[1, 2, 3]
```

**`mutate`** changes the list the caller still points at — visible outside. **`rebind`**
points the local name at a brand-new list; the caller's list was never touched.
(Deck 2 s27–s34.)

**`plus_equal`** is the surprising one: `items += [99]` **mutates in place** (it is
`extend`, not an assignment), so the caller sees it. **`plus`** builds a new list and
rebinds, so the caller does not. `+=` and `x = x + ...` are **not** the same operation on
a list. (Deck 2 s32.)

**What a complete answer needs**

- All three lines, in order.
- Lines 1 and 2 are the baseline — most people get these.
- Line 3 (`+=` giving `[1, 2, 3, 99]`) is the one that separates understanding from
  guessing. Miss it and Deck 2 s32 is the first thing to go back to.

### Q3 — Code writing
**(a)** and **(b)**:

```python
class Thermostat:

    def __init__(self, target, readings):
        self._target = target
        self._readings = list(readings)

    def get_target(self):
        return self._target

    def set_target(self, degrees):
        if degrees < 10 or degrees > 30:
            return False
        self._target = degrees
        return True

    def warmer(self, degrees):
        return self.set_target(self._target + degrees)

    def readings_count(self):
        return len(self._readings)
```

`warmer` is one line because it **delegates**. The rule about what counts as a legal
target lives in exactly one place, so there is exactly one place to get it wrong and one
place to change it. Writing the bounds check a second time inside `warmer` gives the same
test results today and two copies of the rule to maintain — and the two copies drift.

Note `set_target` returns `True` or `False` rather than raising, and because `warmer`
returns whatever `set_target` returned, `warmer(5)` correctly reports `False` when the
result would be 33.

**(c)** `__init__` must store a **copy**: `self._readings = list(readings)`. The obvious
thing — `self._readings = readings` — stores the caller's own list object, so the
`Thermostat` and the caller are holding the same list under two names. The caller's
`history.append(100)` then shows up inside the object, and `readings_count()` returns 3
instead of 2. That is drill 1.4 wearing a different hat: `append` mutates the object that
both names point at.

**What a complete answer needs**

- (a) Five separate things, and each one is a place people slip:
  - `__init__` stores both attributes, under internal names (`_target`, `_readings`).
  - `get_target` returns `self._target` and nothing else.
  - `set_target` checks **both** bounds, 10 and 30, **inclusive**. An exclusive bound
    (`degrees > 10`) is wrong at the edge, and off by one on one side is just as wrong.
  - `set_target` returns **before** assigning on a refusal, and returns `True` or `False`.
    A version that assigns first and then returns `False` looks right and is not — the
    assertion `t.get_target() == 25` after a refused change is what catches it.
  - `warmer` goes **through** `set_target` and returns its result. Reassigning
    `self._target` directly, or re-writing the bounds check inside `warmer`, misses the
    point of the question even when every assertion passes.
- (b) `return len(self._readings)`.
- (c) `list(readings)` or any explicit copy, **and** the aliasing bug named: the object and
  the caller share one list, so the caller's later mutation is visible inside the object.
  "It would be wrong" with no mechanism means you spotted it without understanding it.

**Where the real content is.** Parts (a) and (b) are typing; part (c) is the topic. Writing
all five methods perfectly with `self._readings = readings` gets you working code with a
live bug in it, and that is exactly the shape of the argument-passing questions in Part 1.

---

## If you got it wrong

- Anything wrong in **1.4 to 1.8 or Q2** — Deck 2 s27–s34, then redo them. This family is
  half the topic.
- Anything wrong in **Q1 or Q3** — Deck 2 s7–s12 for the mechanics, s11 for the
  underscore.
- Then write it: `practice/p1_bank_account.py`, checked by
  `python test_p1_bank_account.py`. The `transfer` method there is Q3's delegation idea
  with money at stake.
