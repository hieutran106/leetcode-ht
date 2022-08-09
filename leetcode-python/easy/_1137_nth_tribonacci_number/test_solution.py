import unittest
from .solution import Solution

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()

    def test_case1(self):
        actual = self.s.tribonacci(25)
        self.assertEqual(actual, 1389537)

    def test_case2(self):
        actual = self.s.tribonacci(0)
        self.assertEqual(actual, 0)

    def test_case3(self):
        actual = self.s.tribonacci(1)
        self.assertEqual(actual, 1)

    def test_case4(self):
        actual = self.s.tribonacci(2)
        self.assertEqual(actual, 1)

    def test_case5(self):
        actual = self.s.tribonacci(4)
        self.assertEqual(actual, 4)

if __name__ == '__main__':
    unittest.main()

