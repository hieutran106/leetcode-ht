import unittest
from .solution import Solution

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()

    def test_case_0(self):
        actual = self.s.diffWaysToCompute("2-1")
        self.assertEqual(actual, [1])

    def test_case_1(self):
        actual = self.s.diffWaysToCompute("2-1-1")
        self.assertEqual(actual, [2, 0])

    def test_case_2(self):
        actual = self.s.diffWaysToCompute("2*3-4*5")
        self.assertEqual(actual, [-34, -10, -14, -10, 10])

    def test_case_3(self):
        actual = self.s.diffWaysToCompute("11")
        self.assertEqual(actual, [11])

    def test_case_4(self):
        actual = self.s.diffWaysToCompute("11+11")
        self.assertEqual(actual, [22])

if __name__ == '__main__':
    unittest.main()

