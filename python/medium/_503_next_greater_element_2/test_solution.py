import unittest
from .solution import Solution

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()

    def test_case1(self):
        actual = self.s.nextGreaterElements([1, 2, 1])
        self.assertEqual(actual, [2, -1, 2])

    def test_case2(self):
        actual = self.s.nextGreaterElements([3, 1, 2, 4])
        self.assertEqual(actual, [4, 2, 4, -1])

    def test_case3(self):
        actual = self.s.nextGreaterElements([3, 5, 2, 1])
        self.assertEqual(actual, [5, -1, 3, 3])

if __name__ == '__main__':
    unittest.main()

