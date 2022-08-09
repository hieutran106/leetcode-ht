import unittest
from .solution import Solution

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()

    def test_case_1(self):
        actual = self.s.uniquePaths(3, 7)
        self.assertEqual(actual, 28)

    def test_case_2(self):
        actual = self.s.uniquePaths(3, 2)
        self.assertEqual(actual, 3)

    def test_case_3(self):
        actual = self.s.uniquePaths(2, 2)
        self.assertEqual(actual, 2)

    def test_case_4(self):
        actual = self.s.uniquePaths(1, 1)
        # ??
        self.assertEqual(actual, 1)

    def test_case_5(self):
        actual = self.s.uniquePaths(1, 2)
        self.assertEqual(actual, 1)

    def test_case_6(self):
        actual = self.s.uniquePaths(2, 1)
        self.assertEqual(actual, 1)

    def test_case_7(self):
        actual = self.s.uniquePaths(2, 3)
        self.assertEqual(actual, 3)

if __name__ == '__main__':
    unittest.main()

