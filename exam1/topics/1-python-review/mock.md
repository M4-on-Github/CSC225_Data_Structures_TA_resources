# Topic 1 — mock test: classes and argument passing

Part 1 is eight quick drills, Part 2 is three exam-style questions.

**Try each question before opening [solutions.md](solutions.md).** If stuck, read one relevant explanation, close it, and retry. You may type or write your answers.

No time limit is printed here on purpose. Work until you are done, note how long it took,
and compare that with however long you get in the real exam.

---

## Part 1 — Drills

Short answers. One or two sentences, or the line of code asked for.

**1.1** Write the two lines that create a `BankAccount` for "Ada" with a balance of 100,
then deposit 50 into it.

**1.2** `__init__` is called when? And what does it return?

**1.3** Why is `self._balance` written with an underscore when `self.owner` is not?

**1.4** Trace it. What does the caller see?

```python
def f(items):
    items.append(4)

nums = [1, 2, 3]
f(nums)
print(nums)
```

**1.5** Now this one. What does the caller see?

```python
def f(items):
    items = [9, 9, 9]

nums = [1, 2, 3]
f(nums)
print(nums)
```

**1.6** `values += [4]` versus `values = values + [4]` inside a function, where `values`
is a list — which change does the caller see, and why?

**1.7** `x = 5; y = x; y = 6` — what is `x`? Why is this not the same situation as the
list case?

**1.8** The lecture exit ticket, word for word: **what is the difference between rebinding a
variable and mutating an object?**

---

## Part 2 — Exam-style questions

### Q1 — Classes and objects
**(a)** A class is a ____ and an object is ____. Fill both blanks.

**(b)** `deposit` is defined as `def deposit(self, amount)` but called as
`account.deposit(50)` with one argument. Explain.

**(c)** Why is the balance stored as `self._balance` rather than `self.balance`?

### Q2 — Code reading
What are the four lines of output?

```python
def mutate(items):
    items.append(99)

def rebind(items):
    items = [99]

def plus_equal(items):
    items += [99]

def plus(items):
    items = items + [99]

for function in (mutate, rebind, plus_equal, plus):
    nums = [1, 2, 3]
    function(nums)
    print(nums)
```

### Q3 — Code writing
Write real, runnable Python. Keep the signatures given. No imports.

A `Thermostat` holds a target temperature and a list of recent readings. A target is
legal only if it is **between 10 and 30 inclusive**. Assume the initial `target` is legal.

```python
class Thermostat:
    def __init__(self, target, readings):
        # your code here

    def get_target(self):
        # your code here

    def set_target(self, degrees):
        # your code here

    def warmer(self, degrees):
        # your code here


# it must satisfy all of these
t = Thermostat(20, [19, 21])
assert t.get_target() == 20
assert t.set_target(25) is True
assert t.get_target() == 25
assert t.set_target(45) is False
assert t.get_target() == 25            # a refused change must change nothing
assert t.warmer(3) is True
assert t.get_target() == 28
assert t.warmer(5) is False
assert t.get_target() == 28

history = [19, 21]
t2 = Thermostat(20, history)
history.append(100)
assert t2.readings_count() == 2        # the caller's later change must not reach t2
```

**(a)** Write `__init__`, `get_target`, `set_target` and `warmer`. `warmer` raises the
target by `degrees` and returns `True` if the result is still legal; otherwise, it returns
`False` and leaves the target unchanged. It must go **through** `set_target`, not assign
to the attribute itself.

**(b)** Write `readings_count`, the method the last assertion calls.

**(c)** The last three lines of the test are about `__init__`, not about
`readings_count`. What must `__init__` do with `readings` to make that assertion pass, and
what is the bug if it does the obvious thing instead?

---

## Part 3 — Write the code

This topic's practice problem is `practice/p1_bank_account.py` — the guarded class and
the four argument-passing functions, checked by `python -m unittest discover -s . -p "test_p1_bank_account.py" -v` from the
`practice/` folder. Q3 above is the written version of the same skill; the practice
problem is the one a computer checks for you.
