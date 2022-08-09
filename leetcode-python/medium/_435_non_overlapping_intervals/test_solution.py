import unittest
from .solution import Solution

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()

    def test_case1(self):
        actual = self.s.eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]])
        self.assertEqual(actual, 1)

    def test_case2(self):
        actual = self.s.eraseOverlapIntervals([[1,2],[1,2],[1,2]])
        self.assertEqual(actual, 2)

    def test_case3(self):
        actual = self.s.eraseOverlapIntervals([[1,2],[2,3]])
        self.assertEqual(actual, 0)

    def test_case4(self):
        actual = self.s.eraseOverlapIntervals([[1,5], [1,2], [1,3], [2,3]])
        self.assertEqual(actual, 2)

    def test_case5(self):
        actual = self.s.eraseOverlapIntervals([[0,2],[1,3],[1,3],[2,4],[3,5],[3,5],[4,6]])
        self.assertEqual(actual, 4)
if __name__ == '__main__':
    unittest.main()

