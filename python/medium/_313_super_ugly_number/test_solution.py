import unittest
from .solution import Solution

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()

    def test_case1(self):
        actual = self.s.nthSuperUglyNumber(12, [2,7,13,19])
        self.assertEqual(actual, 32)

    def test_case2(self):
        actual = self.s.nthSuperUglyNumber(1, [2, 3, 5])
        self.assertEqual(actual, 1)

    def test_case3(self):
        actual = self.s.nthSuperUglyNumber(2, [3])
        self.assertEqual(actual, 3)

        actual = self.s.nthSuperUglyNumber(3, [3])
        self.assertEqual(actual, 9)

if __name__ == '__main__':
    unittest.main()

