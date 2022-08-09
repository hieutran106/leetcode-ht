import unittest
from .solution import Solution

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()

    def test_case1(self):
        actual = self.s.climbStairs(2)
        self.assertEqual(actual, 2)

    def test_case2(self):
        actual = self.s.climbStairs(3)
        self.assertEqual(actual, 3)

if __name__ == '__main__':
    unittest.main()

