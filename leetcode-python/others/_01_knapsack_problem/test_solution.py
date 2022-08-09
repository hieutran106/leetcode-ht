import unittest
from .solution import Solution, Solution3, Solution4, Solution5, Solution6

class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution6()

    def test_case1(self):
        values = [4, 5, 3, 7 ]
        weights = [2, 3, 1, 4 ]
        actual = self.s.solve(values, weights, capacity=5)
        self.assertEqual(actual, 10)

    def test_case2(self):
        values = [1, 6, 10, 16]
        weights = [1, 2, 3, 5]
        actual = self.s.solve(values, weights, capacity=7)
        self.assertEqual(actual, 22)

    def test_case3(self):
        values = [1, 6, 10, 16]
        weights = [1, 2, 3, 5]
        actual = self.s.solve(values, weights, capacity=6)
        self.assertEqual(actual, 17)


if __name__ == '__main__':
    unittest.main()
