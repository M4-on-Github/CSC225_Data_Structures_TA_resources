# PROBLEM 1 -- Topic 1: classes and argument passing
#
# Check your work:   python test_p1_bank_account.py
# Reference answer:  solutions/p1_bank_account.py  (open it AFTER the tests pass)
#
# ---------------------------------------------------------------------------
# PART A -- BankAccount
#
# Write a BankAccount class with:
#
#   __init__(self, owner, balance)   stores the owner's name and the opening balance.
#                                    The owner is public; the balance is internal and
#                                    named _balance.
#   deposit(self, amount)            adds the amount ONLY if it is greater than zero.
#                                    Returns True if it happened, False if it did not.
#   withdraw(self, amount)           removes the amount only if it is greater than zero
#                                    AND the account holds at least that much.
#                                    Returns True or False the same way.
#   get_balance(self)                returns the balance. This is how the outside world
#                                    reads it -- nobody touches _balance directly.
#   transfer(self, other, amount)    moves money into another BankAccount, but ONLY if
#                                    the withdrawal from this account succeeds.
#                                    Returns True or False.
#   __str__(self)                    returns "Ada: 100" for an account owned by Ada
#                                    holding 100.
#
# The order of operations inside transfer is the whole question. Think about what a test
# would see if you credited the other account first and the withdrawal then failed.
#
# PART B -- argument passing
#
# Four one-line functions. None of them returns anything. For each one, the question the
# tests ask is: after the call, what does the CALLER's list look like?
#
#   mutate_list(values)         append 100 to it
#   rebind_list(values)         assign [100] to the parameter name
#   add_with_plus_equal(values) use  values += [4]
#   add_with_plus(values)       use  values = values + [4]
#
# Two of these are visible to the caller and two are not. Predict which before you run
# the tests -- that prediction is the thing being examined, not the typing.
#
# Conventions: no type hints, no imports, no docstrings. Match the lecture style.
# ---------------------------------------------------------------------------


class BankAccount:

    def __init__(self, owner, balance):
        pass  # TODO

    def deposit(self, amount):
        pass  # TODO

    def withdraw(self, amount):
        pass  # TODO

    def get_balance(self):
        pass  # TODO

    def transfer(self, other, amount):
        pass  # TODO

    def __str__(self):
        pass  # TODO


def mutate_list(values):
    pass  # TODO


def rebind_list(values):
    pass  # TODO


def add_with_plus_equal(values):
    pass  # TODO


def add_with_plus(values):
    pass  # TODO
