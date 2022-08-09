import unittest
from .solution import Solution

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()

    def test_case1(self):
        actual = self.s.coinChange([1, 2, 5], 11)
        self.assertEqual(actual, 3)

    def test_case2(self):
        actual = self.s.coinChange([2], 3)
        self.assertEqual(actual, -1)

    def test_case3(self):
        actual = self.s.coinChange([1], 0)
        self.assertEqual(actual, 0)

    def test_case4(self):
        actual = self.s.coinChange([2, 3, 7], 12)
        self.assertEqual(actual, 4)

if __name__ == '__main__':
    unittest.main()

