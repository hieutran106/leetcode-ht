import unittest
from .solution import Solution

class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()

    def test_case1(self):
        actual = self.s.integerBreak(2)
        self.assertEqual(1, actual)

    def test_case2(self):
        actual = self.s.integerBreak(10)
        self.assertEqual(36, actual)

    def test_case3(self):
        actual = self.s.integerBreak(3)
        self.assertEqual(actual, 2)

        actual = self.s.integerBreak(4)
        self.assertEqual(actual, 4)

        actual = self.s.integerBreak(6)
        self.assertEqual(actual, 9)

    def test_case6(self):
        actual = self.s.integerBreak(9)
        self.assertEqual(actual, 27)

    def test_case5(self):
        actual = self.s.integerBreak(13)
        self.assertEqual(actual, 108)

    def test_case4(self):
        actual = self.s.integerBreak(15)
        self.assertEqual(actual, 243)


if __name__ == '__main__':
    unittest.main()

