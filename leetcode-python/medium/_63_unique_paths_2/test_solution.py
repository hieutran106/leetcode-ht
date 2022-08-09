import unittest
from .solution import Solution


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()

    def test_case1(self):
        actual = self.s.uniquePathsWithObstacles([[0,1],[0,0]])
        self.assertEqual(actual, 1)

    def test_case2(self):
        actual = self.s.uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]])
        self.assertEqual(actual, 2)

    def test_case3(self):
        actual = self.s.uniquePathsWithObstacles([[1]])
        self.assertEqual(actual, 0)

    def test_case4(self):
        actual = self.s.uniquePathsWithObstacles([[0]])
        self.assertEqual(actual, 1)






if __name__ == '__main__':
    unittest.main()

