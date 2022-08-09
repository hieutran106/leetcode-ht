import unittest
from .solution import Solution

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()

    def test_case_1(self):
        actual = self.s.numSquares(12)
        self.assertEqual(actual, 3)

    def test_case_2(self):
        actual = self.s.numSquares(13)
        self.assertEqual(actual, 2)

    def test_case_3(self):
        actual = self.s.numSquares(3)
        self.assertEqual(actual, 3)

    def test_case_4(self):
        actual = self.s.numSquares(4)
        self.assertEqual(actual, 1)

    def test_case_5(self):
        actual = self.s.numSquares(101)
        self.assertEqual(actual, 2)

if __name__ == '__main__':
    unittest.main()

