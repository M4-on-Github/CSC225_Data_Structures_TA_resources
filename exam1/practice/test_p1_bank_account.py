# Tests for Problem 1. Run from this folder:
#
#     python test_p1_bank_account.py
#
# Read the failures. A unittest failure identifies the assertion that failed and usually
# shows the actual and expected values. Check the named test to see its input.

import unittest

from p1_bank_account import (BankAccount, mutate_list, rebind_list,
                             add_with_plus_equal, add_with_plus)


class TestConstructor(unittest.TestCase):

    def test_owner_is_public(self):
        a = BankAccount("Ada", 100)
        self.assertEqual(a.owner, "Ada")

    def test_balance_is_stored_privately(self):
        a = BankAccount("Ada", 100)
        self.assertEqual(a.get_balance(), 100,
                         "get_balance() should report the opening balance")

    def test_underscore_name(self):
        # Encapsulation is a naming convention here, not enforcement -- the problem
        # expects the convention, so the test expects it too.
        a = BankAccount("Ada", 100)
        self.assertTrue(hasattr(a, "_balance"),
                        "the internal balance should be named _balance")

    def test_two_accounts_are_independent(self):
        a = BankAccount("Ada", 100)
        b = BankAccount("Bo", 50)
        a.deposit(10)
        self.assertEqual(b.get_balance(), 50, "accounts must not share state")


class TestDeposit(unittest.TestCase):

    def test_deposit_increases_balance(self):
        a = BankAccount("Ada", 100)
        a.deposit(50)
        self.assertEqual(a.get_balance(), 150)

    def test_deposit_returns_true(self):
        a = BankAccount("Ada", 100)
        self.assertIs(a.deposit(50), True)

    def test_deposit_rejects_zero(self):
        a = BankAccount("Ada", 100)
        self.assertIs(a.deposit(0), False)
        self.assertEqual(a.get_balance(), 100, "a rejected deposit must change nothing")

    def test_deposit_rejects_negative(self):
        a = BankAccount("Ada", 100)
        self.assertIs(a.deposit(-25), False)
        self.assertEqual(a.get_balance(), 100)


class TestWithdraw(unittest.TestCase):

    def test_withdraw_reduces_balance(self):
        a = BankAccount("Ada", 100)
        a.withdraw(40)
        self.assertEqual(a.get_balance(), 60)

    def test_withdraw_returns_true(self):
        a = BankAccount("Ada", 100)
        self.assertIs(a.withdraw(40), True)

    def test_withdraw_exact_balance_is_allowed(self):
        a = BankAccount("Ada", 100)
        self.assertIs(a.withdraw(100), True)
        self.assertEqual(a.get_balance(), 0)

    def test_overdraft_is_refused(self):
        a = BankAccount("Ada", 100)
        self.assertIs(a.withdraw(101), False)
        self.assertEqual(a.get_balance(), 100, "a refused withdrawal must change nothing")

    def test_withdraw_rejects_negative(self):
        # Without the amount > 0 guard, withdrawing -50 would ADD 50.
        a = BankAccount("Ada", 100)
        self.assertIs(a.withdraw(-50), False)
        self.assertEqual(a.get_balance(), 100)


class TestTransfer(unittest.TestCase):

    def test_successful_transfer_moves_money(self):
        a = BankAccount("Ada", 100)
        b = BankAccount("Bo", 20)
        self.assertIs(a.transfer(b, 30), True)
        self.assertEqual(a.get_balance(), 70)
        self.assertEqual(b.get_balance(), 50)

    def test_failed_transfer_moves_nothing(self):
        # The one that catches a wrong answer: if you deposit before checking the
        # withdrawal, money appears in Bo's account out of nowhere.
        a = BankAccount("Ada", 100)
        b = BankAccount("Bo", 20)
        self.assertIs(a.transfer(b, 500), False)
        self.assertEqual(a.get_balance(), 100)
        self.assertEqual(b.get_balance(), 20,
                         "a failed transfer must not credit the other account")

    def test_total_money_is_conserved(self):
        a = BankAccount("Ada", 100)
        b = BankAccount("Bo", 20)
        a.transfer(b, 30)
        a.transfer(b, 999)
        b.transfer(a, 5)
        self.assertEqual(a.get_balance() + b.get_balance(), 120)


class TestStr(unittest.TestCase):

    def test_str_format(self):
        a = BankAccount("Ada", 100)
        self.assertEqual(str(a), "Ada: 100")


class TestArgumentPassing(unittest.TestCase):
    # Topic 1's central idea. Each test asks only one thing: after the call, what does
    # the CALLER see?

    def test_mutate_is_visible(self):
        nums = [1, 2, 3]
        mutate_list(nums)
        self.assertEqual(nums, [1, 2, 3, 100],
                         "append mutates the caller's list")

    def test_rebind_is_invisible(self):
        nums = [1, 2, 3]
        rebind_list(nums)
        self.assertEqual(nums, [1, 2, 3],
                         "assigning to the parameter only moves the local name")

    def test_plus_equal_is_visible(self):
        nums = [1, 2, 3]
        add_with_plus_equal(nums)
        self.assertEqual(nums, [1, 2, 3, 4],
                         "+= on a list extends it in place")

    def test_plus_is_invisible(self):
        nums = [1, 2, 3]
        add_with_plus(nums)
        self.assertEqual(nums, [1, 2, 3],
                         "values + [4] builds a new list and rebinds the local name")

    def test_the_pair_differs(self):
        # Similar-looking lines, different outcomes. This is the distinction to explain.
        a = [1, 2, 3]
        b = [1, 2, 3]
        add_with_plus_equal(a)
        add_with_plus(b)
        self.assertNotEqual(a, b)


if __name__ == "__main__":
    unittest.main(verbosity=2)
