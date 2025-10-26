import unittest
from typing import List

# Date: 2025-10-26
# Problem: 2043 simple_bank_system
class Bank:

    def __init__(self, balance: List[int]):
        self.balance = balance

    def in_range(self, account):
        return 0< account <= len(self.balance)

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if not self.in_range(account1) or not self.in_range(account2):
            return False
        if self.balance[account1-1] < money:
            return False
        self.balance[account1-1] -= money
        self.balance[account2-1] += money
        return True

    def deposit(self, account: int, money: int) -> bool:
        if not self.in_range(account):
            return False
        self.balance[account-1] += money
        return True

    def withdraw(self, account: int, money: int) -> bool:
        if not self.in_range(account):
            return False
        if self.balance[account-1] < money:
            return False
        self.balance[account-1] -= money
        return True

class MyTestCase(unittest.TestCase):


    
    def test_case_1(self):
        b = Bank([10, 100, 20, 50, 30])
        res = b.withdraw(3, 10)
        self.assertEqual(True, res)
        res = b.transfer(5, 1, 20)
        self.assertEqual(True, res)
        res = b.deposit(5, 20)
        self.assertEqual(True, res)
        res = b.transfer(3, 4, 15)
        self.assertEqual(False, res)
        res = b.withdraw(10, 50)
        self.assertEqual(False, res)



if __name__ == '__main__':
    unittest.main()

