# Topic 1 — Python review: classes and argument passing

**Source:** Crash Course 1 and 2 (95 slides). **Lecture weight:** heaviest.

---

## Why this topic is first

The professor's note about the exam names exactly one topic:

> *"I will most likely have them use a class (since they struggled with that in 130)."*

So this is first and it is longest. It has two halves that students usually treat as
unrelated and which are in fact the same idea: **building objects**, and **what happens
when you pass an object to a function**. Thirty-one of Deck 2's sixty-one slides are
these two halves.

This is a review topic, not a full CSC130 refresher. Loops, strings, files and
dictionaries are assumed. Classes and argument passing are the parts that get examined.

---

## The ideas, in the order they depend on each other

- **A class is a blueprint; an object is one thing built from it.** The class is written
  once; objects are made from it many times, each with its own attribute values.
- **`__init__` runs automatically** the moment an object is created. You never call it by
  name. Its job is to attach attributes to `self`.
- **`self` is the current object.** Python supplies it, which is why a method defined
  with two parameters is called with one argument.
- **Encapsulation** is a leading underscore plus discipline: `_balance` says "go through
  `deposit` and `withdraw`", and those methods can refuse a bad amount. Python does not
  enforce it; the convention is the whole mechanism.
- **Inheritance, for vocabulary only.** A child class gets everything the parent has;
  `super().__init__(...)` runs the parent's setup; redefining a method **overrides** it;
  calling the same method on different types and getting different behaviour is
  **polymorphism**. Nothing in this package's drills, mock papers or practice problems
  tests inheritance — know the four words and move on.
- **Mutability belongs to the object, not the name.** Lists and dictionaries can be
  changed in place; ints, floats, strings and tuples cannot.
- **Mutating is not rebinding.** `items.append(4)` changes the object the caller is
  holding. `items = [9, 9, 9]` points the local name somewhere else and leaves the
  caller's object untouched.

---

## The pattern he writes

Drawing on Deck 2 s7–s12 and the encapsulation pattern on s11 (Deck 1 s23 shows the same
idea):

```python
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner          # public: no rule to protect
        self._balance = balance     # internal: only methods should touch it

    def deposit(self, amount):
        if amount <= 0:             # the guard is the point of the method
            return False
        self._balance = self._balance + amount
        return True

    def get_balance(self):
        return self._balance
```

Three things to notice, because all three are easy to get wrong:

1. `self.owner` is public and `self._balance` is not. The difference is that the balance
   has a **rule** attached to it and the owner's name does not.
2. The guard `if amount <= 0: return False` comes **before** the assignment. A guard
   placed after the assignment protects nothing.
3. `deposit` is written with two parameters and called with one argument:
   `account.deposit(50)` becomes `deposit(account, 50)`.

## The pattern he contrasts

The four one-line functions from Deck 2 s31–s32. These are the entire
mutate-versus-rebind family, and one of them is on the mock paper for this topic:

```python
def mutate(items):
    items.append(99)        # the caller sees it

def rebind(items):
    items = [99]            # the caller sees nothing

def plus_equal(items):
    items += [99]           # the caller sees it -- this is the surprising one

def plus(items):
    items = items + [99]    # the caller sees nothing
```

`items += [99]` is **not** shorthand for `items = items + [99]` on a list. The first
mutates in place (it is `extend`); the second builds a new list and rebinds the local
name. One character of difference, opposite outcomes.

His diagnostic question, and the one to ask before you trace anything:

> *"Did the code change the object, or did it move the local name?"*

---

## How he says it

| | |
|---|---|
| "A class is a blueprint. An object is one thing built from that blueprint." | Deck 2 s7 |
| "`self` means the current object. Inside a method, use `self.attribute` to access data stored in that object." | Deck 2 s9 |
| "A variable is a name tag attached to an object." | Deck 2 s28 |
| "Mutability is about the object, not the variable name." | Deck 2 s23 |
| "Did the code change the object, or did it move the local name?" | Deck 2 s31 |
| "The object 10 did not turn into 20. The name `x` moved." | Deck 2 s27 |

The name-tag image on s28 is worth keeping. Rebinding moves the tag to a different
object. Mutating alters the thing the tag is stuck to, so **everyone** holding a tag on
that object sees the change.

---

## Where people go wrong

- Leaving `self` off a method's parameter list, then being confused by *"takes 0
  positional arguments but 1 was given"*.
- Writing `balance = balance + amount` inside a method. That creates a local variable and
  the object never changes. It must be `self._balance`.
- Letting a guard "fail" silently: check the condition, then `return` **before** the
  assignment, not after it.
- Answering a mutate-versus-rebind question by running the code in your head without
  deciding which of the two it is. Ask his question first, then trace.
- Assuming a child class automatically runs the parent's `__init__`. It does not, unless
  you call `super().__init__(...)`.
- Thinking `+=` and `x = x + ...` are the same thing. On a list they are not.

---

## Checklist

Tick these off from memory, not by rereading.

- [ ] `__init__`, `self`, attributes, methods — Deck 2 s7–s12
- [ ] Encapsulation: the `_name` convention, guarded setters — Deck 2 s11
- [ ] Mutable versus immutable objects — Deck 2 s23
- [ ] Passing arguments: mutate versus rebind — Deck 2 s27–s34
- [ ] `+=` versus `x = x + ...` on a list — Deck 2 s32
- [ ] Inheritance, `super()`, overriding, polymorphism — vocabulary only — Deck 2 s15–s20

---

## Next

- Work [mock.md](mock.md) with this page closed, then check yourself against
  [solutions.md](solutions.md).
- Write the code: `practice/p1_bank_account.py`, checked by
  `python test_p1_bank_account.py`. It is this topic's two halves as one file — the
  guarded class and the four argument-passing functions.
