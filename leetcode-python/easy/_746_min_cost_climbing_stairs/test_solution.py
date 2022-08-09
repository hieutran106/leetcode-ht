import unittest
from .solution import Solution


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()

    def test_case1(self):
        actual = self.s.minCostClimbingStairs([10, 15, 20])
        self.assertEqual(actual, 15)

    def test_case2(self):
        actual = self.s.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1])
        self.assertEqual(actual, 6)

    def test_case3(self):
        actual = self.s.minCostClimbingStairs([1, 2])
        self.assertEqual(actual, 1)

    def test_case4(self):
        actual = self.s.minCostClimbingStairs([1, 2, 1])
        self.assertEqual(actual, 2)


if __name__ == "__main__":
    unittest.main()
