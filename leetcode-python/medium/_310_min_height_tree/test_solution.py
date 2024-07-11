import unittest
from .solution import Solution
from typing import List


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        return []


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()

    def test_case_1(self):
        actual = self.s.findMinHeightTrees(n=4, edges=[[1, 0], [1, 2], [1, 3]])
        self.assertEqual([1], actual)

    def test_case_2(self):
        actual = self.s.findMinHeightTrees(n=6, edges=[[3, 0], [3, 1], [3, 2], [3, 4], [5, 4]])
        self.assertEqual([3, 4], actual)


if __name__ == '__main__':
    unittest.main()
