import unittest
from .solution import Solution

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()

    def testCase1(self):
        actual = self.s.uniquePathsIII([[1,0,0,0],[0,0,0,0],[0,0,2,-1]])
        self.assertEqual(actual, 2)

    def testCase2(self):
        actual = self.s.uniquePathsIII([[1,0,0,0],[0,0,0,0],[0,0,0,2]])
        self.assertEqual(actual, 4)

    def testCase3(self):
        actual = self.s.uniquePathsIII([[0,1],[2,0]])
        self.assertEqual(actual, 0)

    def testCase4(self):
        actual = self.s.uniquePathsIII([[1,0,0,0],[0,0,0,0],[0,0,2,0]])
        self.assertEqual(actual, 0)

if __name__ == '__main__':
    unittest.main()

