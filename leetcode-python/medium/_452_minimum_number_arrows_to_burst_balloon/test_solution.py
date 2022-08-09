import unittest
from .solution import Solution

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()

    def test_case1(self):
        actual = self.s.findMinArrowShots([[1,2],[3,4],[5,6],[7,8]])
        self.assertEqual(actual, 4)

    def test_case2(self):
        actual = self.s.findMinArrowShots([[10,16],[2,8],[1,6],[7,12]])
        self.assertEqual(actual, 2)

    def test_case3(self):
        actual = self.s.findMinArrowShots([[1,2],[3,4],[5,6],[7,8]])
        self.assertEqual(actual, 4)

    def test_case4(self):
        actual = self.s.findMinArrowShots([[1,2],[2,3],[3,4],[4,5]])
        self.assertEqual(actual, 2)

if __name__ == '__main__':
    unittest.main()

