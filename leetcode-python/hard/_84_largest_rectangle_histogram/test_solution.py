import unittest
from .solution import Solution

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()

    def test_case1(self):
        actual = self.s.largestRectangleArea([2,1,5,6,2,3])
        self.assertEqual(actual, 10)

    def test_case2(self):
        actual = self.s.largestRectangleArea([2, 4])
        self.assertEqual(actual, 4)

if __name__ == '__main__':
    unittest.main()

