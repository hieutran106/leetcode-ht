import unittest
from .solution import Solution

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()

    def test_case1(self):
        strs = ["10","0001","111001","1","0"]
        m = 5
        n = 3
        actual = self.s.findMaxForm(strs, m, n)
        self.assertEqual(actual, 4)

    def test_case2(self):
        strs = ["10","0","1"]
        m = 1
        n = 1
        actual = self.s.findMaxForm(strs, m, n)
        self.assertEqual(actual, 2)

    def test_case3(self):
        strs = ["10", "0001", "111001", "1", "0"]
        m = 4
        n = 3
        actual = self.s.findMaxForm(strs, m, n)
        self.assertEqual(actual, 3)

if __name__ == '__main__':
    unittest.main()

