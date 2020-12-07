import unittest
from .solution import Solution

class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()

    def test_case1(self):
        actual = self.s.solve([4, 5, 1], [1, 2, 3], 4)
        self.assertEqual(actual, 3)

    def test_case2(self):
        actual = self.s.solve([4, 5, 6], [1, 2, 3], 3)
        self.assertEqual(actual, 0)

    def test_case3(self):
        actual = self.s.solve([10, 20 , 30], [60, 100, 120], 50)
        self.assertEqual(actual, 220)

if __name__ == '__main__':
    unittest.main()
