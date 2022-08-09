import unittest
from .solution import Solution

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()

    def test_case1(self):
        actual = self.s.maxProfit([1,3,2,8,4,9], 2)
        self.assertEqual(actual, 8)

    def test_case2(self):
        actual = self.s.maxProfit([1,3,7,5,10,3], 3)
        self.assertEqual(actual, 6)

    def test_case3(self):
        actual = self.s.maxProfit([1, 3], 3)
        self.assertEqual(actual, 0)

if __name__ == '__main__':
    unittest.main()

