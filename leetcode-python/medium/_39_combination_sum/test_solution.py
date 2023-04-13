import unittest
from .solution import Solution

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()

    def test_case_1(self):
        actual = self.s.combinationSum(candidates = [2,3,6,7], target = 7)
        self.assertEqual([[2,2,3],[7]], actual)

    def test_case_2(self):
        actual = self.s.combinationSum(candidates = [2,3,5], target = 8)
        self.assertEqual([[2,2,2,2],[2,3,3],[3,5]], actual)

if __name__ == '__main__':
    unittest.main()

