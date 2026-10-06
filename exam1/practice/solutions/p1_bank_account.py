# Reference solution -- Problem 1. Topic 1 (Python review: classes, argument passing).
#
# Conventions from the slides, not generic Python:
#   - BankAccount is the lecture's encapsulation example (Crash Course 1 s23, Crash Course 2 s12).
#   - The internal balance is _balance; callers read it through get_balance().
#   - deposit guards with "if amount > 0" and returns True/False rather than raising.
#   - No type hints, no docstrings in student-facing code -- that matches the decks.


class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self._balance = balance

    def deposit(self, amount):
        if amount > 0:
            self._balance = self._balance + amount
            return True
        return False

    def withdraw(self, amount):
        if amount > 0 and amount <= self._balance:
            self._balance = self._balance - amount
            return True
        return False

    def get_balance(self):
        return self._balance

    def transfer(self, other, amount):
        # The guard is the whole point: money may only appear in the other account if it
        # actually left this one. Deposit SECOND, and only if the withdrawal succeeded.
        if self.withdraw(amount):
            other.deposit(amount)
            return True
        return False

    def __str__(self):
        return self.owner + ": " + str(self._balance)


# --- mutate vs. rebind (Crash Course 2 s31 and s33) --------------------------
#
# This pair is the single most-tested idea in the Python-review topic. A function
# receives a reference to the SAME list object. Changing the object is visible to the
# caller; pointing the local name at a different object is not.

def mutate_list(values):
    # Mutates the object the caller handed in. The caller sees it.
    values.append(100)


def rebind_list(values):
    # Points the local name at a brand-new list. The caller's list is untouched.
    values = [100]


def add_with_plus_equal(values):
    # += on a list calls list.__iadd__, which EXTENDS IN PLACE. The caller sees it.
    values += [4]


def add_with_plus(values):
    # values + [4] builds a new list; the assignment rebinds the local name only.
    values = values + [4]
