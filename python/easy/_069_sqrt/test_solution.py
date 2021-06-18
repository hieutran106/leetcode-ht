import unittest
from .solution import Solution

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()

    def test_case1(self):
        actual = self.s.mySqrt(4)
        self.assertEqual(actual, 2)

    def test_case2(self):
        actual = self.s.mySqrt(8)
        self.assertEqual(actual, 2)

    def test_case3(self):
        actual = self.s.mySqrt(10)
        self.assertEqual(actual, 3)

    def test_case4(self):
        actual = self.s.mySqrt(0)
        self.assertEqual(actual, 0)

    def test_case5(self):
        actual = self.s.mySqrt(1)
        self.assertEqual(actual, 1)

    def test_case6(self):
        actual = self.s.mySqrt(17)
        self.assertEqual(actual, 4)

    def test_case7(self):
        actual = self.s.mySqrt(24)
        self.assertEqual(actual, 4)

if __name__ == '__main__':
    unittest.main()

