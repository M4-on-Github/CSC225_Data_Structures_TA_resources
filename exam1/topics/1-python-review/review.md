# Topic 1 — Python classes and argument passing

Review these ideas, then try the [mock questions](mock.md). You are expected to know
basic loops and lists already.

## Classes

A class defines how to make objects. Each object stores its own attributes. Python calls
`__init__` when you create an object; use `self.attribute` to store data on that object.
Python supplies `self` when you call a method: `account.deposit(50)` passes the account
as `self`.

A leading underscore, as in `_balance`, signals that callers should use methods rather
than change the attribute directly. Python does not enforce this convention. Check a
deposit amount *before* updating the balance.

For vocabulary: a child class **inherits** methods; `super().__init__(...)` calls the
parent's setup; redefining a method **overrides** it. Calling the same method on
different object types is **polymorphism**.

## Mutation and rebinding

| Operation inside a function | Caller sees a changed list? | Reason |
|---|---|---|
| `items.append(99)` | Yes | Changes the shared list |
| `items += [99]` | Yes | Extends that list |
| `items = [99]` | No | Moves only the local name |
| `items = items + [99]` | No | Creates a new list, then moves the local name |

Draw a name pointing to a list if this feels unclear. Ask whether the object changed or
only the name changed. An integer cannot be changed in place; a list can.

## Check yourself

- Can you create two objects and explain why changing one object's attribute leaves the other alone?
- Can you trace `append`, `+=`, and `items = items + [...]` without running the code?
- Can you explain why `balance = balance + amount` does not update `self._balance`?

Try the [mock](mock.md), then check [solutions](solutions.md). Code [problem
1](../../practice/p1_bank_account.py) after you can explain the traces.
