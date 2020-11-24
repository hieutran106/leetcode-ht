import unittest
from .solution import Solution

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()

    def test_case1(self):
        actual = self.s.destCity([["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]])
        self.assertEqual(actual, "Sao Paulo")

    def test_case2(self):
        actual = self.s.destCity([["B","C"],["D","B"],["C","A"]])
        self.assertEqual(actual, "A")

    def test_case3(self):
        actual = self.s.destCity([["A","Z"]])
        self.assertEqual(actual, "Z")

if __name__ == '__main__':
    unittest.main()

