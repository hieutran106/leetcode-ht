import unittest
from .solution import Solution

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()

    def test_case1(self):
        actual = self.s.maxProduct([2,3,-2,4])
        self.assertEqual(actual, 6)

    def test_case2(self):
        actual = self.s.maxProduct([-2,0,-1])
        self.assertEqual(actual, 0)

    def test_case3(self):
        actual = self.s.maxProduct([1, 2, 3, 4])
        self.assertEqual(actual, 24)

    def test_case4(self):
        actual = self.s.maxProduct([-1, -2, -3])
        self.assertEqual(actual, 6)

    def test_case5(self):
        actual = self.s.maxProduct([-2])
        self.assertEqual(actual, -2)

if __name__ == '__main__':
    unittest.main()

