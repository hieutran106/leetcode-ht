import unittest
from .solution import Solution, Solution2, Solution3

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()
        # self.s = Solution3()

    def test_case1(self):
        actual = self.s.maxProfit([7,1,5,3,6,4])
        self.assertEqual(actual, 7)

    def test_case2(self):
        actual = self.s.maxProfit([1,2,3,4,5])
        self.assertEqual(actual, 4)

    def test_case3(self):
        actual = self.s.maxProfit([7,6,4,3,1])
        self.assertEqual(actual, 0)

    def test_case4(self):
        actual = self.s.maxProfit([7])
        self.assertEqual(actual, 0)

    def test_case5(self):
        actual = self.s.maxProfit([7, 8])
        self.assertEqual(actual, 1)

if __name__ == '__main__':
    unittest.main()

