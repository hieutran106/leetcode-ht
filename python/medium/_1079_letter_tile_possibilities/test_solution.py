import unittest
from .solution import Solution

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()

    def test_case1(self):
        actual = self.s.numTilePossibilities("AAB")
        self.assertEqual(actual, 8)

    def test_case2(self):
        actual = self.s.numTilePossibilities("AAABBC")
        self.assertEqual(actual, 188)

    def test_case3(self):
        actual = self.s.numTilePossibilities("V")
        self.assertEqual(actual, 1)

    def test_case4(self):
        actual = self.s.numTilePossibilities("AAA")
        self.assertEqual(actual, 3)

if __name__ == '__main__':
    unittest.main()

