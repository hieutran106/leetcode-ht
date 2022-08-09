import unittest
from .solution import Solution

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()

    def test_case1(self):
        actual = self.s.minDistance("horse", "ros")
        self.assertEqual(actual, 3)

    def test_case2(self):
        actual = self.s.minDistance("intention", "execution")
        self.assertEqual(actual, 5)

    def test_case3(self):
        actual = self.s.minDistance("abcd", "")
        self.assertEqual(actual, 4)

    def test_case4(self):
        actual = self.s.minDistance("", "abcde")
        self.assertEqual(actual, 5)

    def test_case5(self):
        actual = self.s.minDistance("", "")
        self.assertEqual(actual, 0)

if __name__ == '__main__':
    unittest.main()

