import unittest
from .solution import Solution

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()

    def test_case1(self):
        actual = self.s.maxProfit([1,2,3,0,2])
        self.assertEqual(actual, 3)

    def test_case2(self):
        actual = self.s.maxProfit([1])
        self.assertEqual(actual, 0)

if __name__ == '__main__':
    unittest.main()

