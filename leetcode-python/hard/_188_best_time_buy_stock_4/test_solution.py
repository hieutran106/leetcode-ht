import unittest
from .solution import Solution


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()

    def test_case1(self):
        actual = self.s.maxProfit(2, [3, 3, 5, 0, 0, 3, 1, 4])
        self.assertEqual(actual, 6)

    def test_case2(self):
        actual = self.s.maxProfit(2, [1, 2, 3, 4, 5])
        self.assertEqual(actual, 4)

    def test_case3(self):
        actual = self.s.maxProfit(2, [7, 6, 4, 3, 1])
        self.assertEqual(actual, 0)

    def test_case4(self):
        actual = self.s.maxProfit(2, [2, 4, 1])
        self.assertEqual(actual, 2)

    def test_case5(self):
        actual = self.s.maxProfit(2, [3, 2, 6, 5, 0, 3])
        self.assertEqual(actual, 7)

    def test_case6(self):
        actual = self.s.maxProfit(3, [2, 6, 8, 7, 8, 7, 9, 4, 1, 2, 4, 5, 8])
        self.assertEqual(actual, 15)


if __name__ == "__main__":
    unittest.main()
