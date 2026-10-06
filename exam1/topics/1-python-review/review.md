# Topic 1 — Python review: classes and argument passing

## What this topic is

Two halves that look unrelated and are really the same idea: **building objects**, and
**what happens when you pass an object to a function**. Writing a class is the single most
likely thing to be asked of you, so this topic comes first and is the longest.

This is a review topic, not a full Python refresher. Loops, strings, files and
dictionaries are assumed. Classes and argument passing are the parts that get examined.

---

## The ideas, in the order they depend on each other

- **A class is a blueprint; an object is one thing built from it.** The class is written
  once; objects are made from it many times, each with its own attribute values.
- **`__init__` runs automatically** when you create an instance of these classes. You do
  not need to call it by name. Its job is to initialise attributes on `self`.
- **`self` is the current object.** Python supplies it, which is why a method defined
  with two parameters is called with one argument.
- **Encapsulation** is a leading underscore plus discipline: `_balance` says "go through
  `deposit` and `withdraw`", and those methods can refuse a bad amount. Python does not
  enforce it; the convention is the whole mechanism.
- **Inheritance, for vocabulary only.** A child class inherits the parent's methods;
  `super().__init__(...)` runs the parent's setup; redefining a method **overrides** it;
  calling the same method on different types and getting different behaviour is
  **polymorphism**. Nothing in the drills, mock paper or practice problems here tests
  inheritance — know the four words and move on.
- **Mutability belongs to the object, not the name.** Lists and dictionaries can be
  changed in place; ints, floats, strings and tuples cannot.
- **Mutating is not rebinding.** `items.append(4)` changes the object the caller is
  holding. `items = [9, 9, 9]` points the local name somewhere else and leaves the
  caller's object untouched.

---

## The pattern to know

The guarded class, which is the shape most likely to be asked for:

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

1. `self.owner` is public and `self._balance` is internal **by convention**. The
   difference is that the balance has a **rule** attached to it and the owner's name does
   not.
2. The guard `if amount <= 0: return False` comes **before** the assignment. A guard
   placed after the assignment protects nothing.
3. `deposit` is written with two parameters and called with one argument:
   `account.deposit(50)` is equivalent to `BankAccount.deposit(account, 50)`.

## The four functions to know

These cover every mutate-versus-rebind pattern, and all four are on the mock paper for
this topic:

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
mutates in place (like `extend`); the second builds a new list and rebinds the local
name. Similar-looking code, different outcomes.

The question to ask before you trace anything:

> *"Did the code change the object, or did it move the local name?"*

---

## Say it this way

Six sentences worth having word for word. They are the course's own phrasing, and a
written answer that uses them is hard to mark down.

- A class is a blueprint. An object is one thing built from that blueprint.
- `self` means the current object. Inside a method, use `self.attribute` to reach the data
  stored in that object.
- A variable is a name tag attached to an object.
- Mutability is about the object, not the variable name.
- Did the code change the object, or did it move the local name?
- The object `10` did not turn into `20`. The name `x` moved.

The name-tag image is worth keeping. Rebinding moves the tag to a different object.
Mutating alters the thing the tag is stuck to, so **everyone** holding a tag on that
object sees the change.

---

## Where people go wrong

- Leaving `self` off a method's parameter list, then being confused by *"takes 0
  positional arguments but 1 was given"*.
- Writing `balance = balance + amount` inside `deposit`. That tries to read an
  uninitialised local variable and raises `UnboundLocalError`; it does not update the
  object. Use `self._balance = self._balance + amount`.
- Letting a guard "fail" silently: check the condition, then `return` **before** the
  assignment, not after it.
- Answering a mutate-versus-rebind question by running the code in your head without
  deciding which of the two it is. Ask that question first, then trace.
- Assuming an overriding `__init__` automatically runs the parent's `__init__`. It does
  not: call `super().__init__(...)` when the parent's setup is needed. A child that does
  not override `__init__` inherits it.
- Thinking `+=` and `x = x + ...` are the same thing. On a list they are not.

---

## Checklist

Tick these off from memory, not by rereading.

- [ ] `__init__`, `self`, attributes, methods
- [ ] Encapsulation: the `_name` convention, guarded setters
- [ ] Mutable versus immutable objects
- [ ] Passing arguments: mutate versus rebind
- [ ] `+=` versus `x = x + ...` on a list
- [ ] Inheritance, `super()`, overriding, polymorphism — vocabulary only

---

## Next

- Work [mock.md](mock.md) with this page closed, then check yourself against
  [solutions.md](solutions.md).
- Write the code: `practice/p1_bank_account.py`, checked by
  `python -m unittest discover -s . -p "test_p1_bank_account.py" -v`. It is this topic's two halves as one file — the
  guarded class and the four argument-passing functions.
