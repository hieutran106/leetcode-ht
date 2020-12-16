import unittest
from .solution import Solution

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()

    def test_case1(self):
        actual = self.s.countPrimes(10)
        self.assertEqual(actual, 4)

    def test_case2(self):
        actual = self.s.countPrimes(0)
        self.assertEqual(actual, 0)

    def test_case3(self):
        actual = self.s.countPrimes(1)
        self.assertEqual(actual, 0)

    def test_case1(self):
        actual = self.s.countPrimes(12)
        self.assertEqual(actual, 5)

if __name__ == '__main__':
    unittest.main()

